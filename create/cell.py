from pdfplumber import open
from numpy import array, min, max, savez


def task(data_path):
    curves = []
    min_x, max_x = None, None
    min_y, max_y = None, None
    with open(data_path + "cell.pdf") as pdf:
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

    save_data = {}
    x0, y0 = [], []
    x1, y1 = [], []
    for index, curve in enumerate(curves):
        curve[:, 0] -= min_x
        curve[:, 1] -= min_y
        curve[:, 0] /= (max_x - min_x)
        curve[:, 1] /= (max_y - min_y)
        curve[:, 1] -= 0.03987129025770687
        x0.append(min(curve[:, 0]))
        y0.append(min(curve[:, 1]))
        x1.append(max(curve[:, 0]))
        y1.append(max(curve[:, 1]))
        save_data["c-" + str(index + 1).zfill(2)] = curve
        print(index, min(curve[:, 0]), max(curve[:, 0]), min(curve[:, 1]), max(curve[:, 1]))

    savez(data_path + "cell.npz", **save_data)