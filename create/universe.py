from matplotlib import pyplot
from numpy import ndarray, array, asarray, linspace, meshgrid, min, max, savez
from pdfplumber import open
from PIL import Image
from os import remove, path
from requests import get
from scipy.ndimage import gaussian_filter
from sklearn.neighbors import NearestNeighbors


url = "https://upload.wikimedia.org/wikipedia/commons/0/04/Cosmic_Microwave_Background_%28CMB%29.jpeg?download"


def invert_colormap(image_path: str,
                    cmap_name: str = "viridis",
                    color_number: int = 256) \
        -> ndarray:

    image = Image.open(image_path).convert("RGB")
    image_np = asarray(image) / 255.0
    h, w, _ = image_np.shape

    cmap = pyplot.get_cmap(cmap_name, color_number)
    gradient_vals = linspace(0, 1, color_number)
    colormap_rgb = cmap(gradient_vals)[:, :3]

    nn = NearestNeighbors(n_neighbors=1)
    nn.fit(colormap_rgb)

    pixels = image_np.reshape(-1, 3)

    _, indices = nn.kneighbors(pixels)

    matrix = (indices.flatten() / (color_number - 1)).reshape(h, w)

    return matrix


# noinspection PyTypeChecker,PyUnresolvedReferences
def task(data_path):
    if not path.exists(data_path + "universe.jpg"):
        response = get(url, stream=True)
        response.raise_for_status()
        with open(data_path + "universe.jpg", "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

    matrix = invert_colormap(data_path + "universe.jpg")
    matrix = gaussian_filter(matrix, sigma=20.0)
    matrix -= min(matrix)
    matrix /= max(matrix)
    grid_x = linspace(0, 2, matrix.shape[1])
    grid_y = linspace(0, 1, matrix.shape[0])
    mesh_x, mesh_y = meshgrid(grid_x, grid_y)

    pyplot.contour(mesh_x, mesh_y, matrix, levels=[0.30, 0.65], cmap="viridis_r",
                   linewidths=0.75, zorder=2)
    pyplot.axis("off")
    pyplot.xlim(-0.1, 2.1)
    pyplot.ylim(-0.1, 1.1)
    pyplot.savefig(data_path + "temp.pdf")

    curves = []
    min_x, max_x = None, None
    min_y, max_y = None, None
    with open(data_path + "temp.pdf") as pdf:
        page = pdf.pages[0]
        for index, data in enumerate(page.objects["curve"]):
            points = array(data["pts"])
            curves.append(points)
            if min_x is not None:
                if min_x > data["x0"]:
                    min_x = data["x0"]
            else:
                min_x = data["x0"]
            if max_x is not None:
                if max_x < data["x1"]:
                    max_x = data["x1"]
            else:
                max_x = data["x1"]
            if min_y is not None:
                if min_y > data["y0"]:
                    min_y = data["y0"]
            else:
                min_y = data["y0"]
            if max_y is not None:
                if max_y < data["y1"]:
                    max_y = data["y1"]
            else:
                max_y = data["y1"]

    remove(data_path + "temp.pdf")

    save_data = {}
    x0, y0 = [], []
    x1, y1 = [], []
    for index, curve in enumerate(curves):
        curve[:, 0] -= min_x
        curve[:, 1] -= min_y
        curve[:, 0] /= (max_x - min_x)
        curve[:, 1] /= (max_y - min_y)
        curve[:, 1] -= 0.03576498243836378
        curve[:, 1] /= (1.0357649824383637 - 0.03576498243836378)
        x0.append(min(curve[:, 0]))
        y0.append(min(curve[:, 1]))
        x1.append(max(curve[:, 0]))
        y1.append(max(curve[:, 1]))
        save_data["c-" + str(index + 1).zfill(2)] = curve
        print(index, min(curve[:, 0]), max(curve[:, 0]), min(curve[:, 1]), max(curve[:, 1]))

    savez(data_path + "universe.npz", **save_data)
