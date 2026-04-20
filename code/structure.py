from numpy import zeros, arange, linspace, max
from sklearn.manifold import MDS
from warnings import filterwarnings

filterwarnings("ignore")

colors = ["#555555", "#CD8F5B", "#A671D1", "#28ACB6", "#A94823", "#EEEEEE"]
infos = [(3, 1), (1, 5), (1, 2), (1, 0), (1, 4), (1, 0), (1, 0), (1, 5),
         (4, 5), (1, 4), (1, 5), (1, 0), (1, 5), (1, 2), (1, 5),
         (4, 5), (3, 1), (1, 5), (1, 4), (1, 5), (2, 1), (1, 5), (5, 2),
         (1, 0), (1, 3), (1, 0), (1, 5), (1, 4), (1, 5), (1, 0), (1, 5), (1, 3), (1, 0), (1, 0), (1, 5),
         (8, 5), (1, 4), (1, 5), (2, 0), (1, 5), (1, 4), (1, 5),
         (4, 5), (6, 1), (1, 5), (1, 4), (1, 5)]

matrix = zeros(shape=(78, 78))
for index in range(78):
    matrix[index + 0, index + 0] = 1
    if index + 1 < 78:
        matrix[index + 1, index + 0] = 0.6
        matrix[index + 0, index + 1] = 0.6
    if index + 2 < 78:
        matrix[index + 2, index + 0] = 0.2
        matrix[index + 0, index + 2] = 0.2
segment_locations = []
last = 0
for addition, value in infos:
    segment_locations.append((last, last + addition))
    last += addition
item_number = len(segment_locations)
for former, latter in [(4, 27),
                       (9, 36), (9, 45), (13, 36), (13, 45), (40, 36), (40, 45),
                       (24, 18), (27, 18), (31, 18),
                       (18, 40)]:
    for bias, value in zip(arange(10), linspace(1.0, 0.0, 10)):
        if former < latter:
            if 0 <= former + bias < item_number and 0 <= latter - bias < item_number:
                length_1 = segment_locations[former + bias][1] - segment_locations[former + bias][0]
                length_2 = segment_locations[latter - bias][1] - segment_locations[latter - bias][0]
                positions_1 = arange(segment_locations[former + bias][0],
                                     segment_locations[former + bias][0] + max([length_1, length_2]) + 1)
                positions_2 = arange(segment_locations[latter - bias][0],
                                     segment_locations[latter - bias][0] + max([length_1, length_2]) + 1)
                for index_1, index_2 in zip(positions_1, positions_2):
                    if index_1 >= 78 or index_2 >= 78:
                        continue
                    matrix[index_1, index_2] = max([matrix[index_1, index_2], value])
                    matrix[index_2, index_1] = max([matrix[index_2, index_1], value])
        else:
            if 0 <= former - bias < item_number and 0 <= latter + bias < item_number:
                length_1 = segment_locations[former - bias][1] - segment_locations[former - bias][0]
                length_2 = segment_locations[latter + bias][1] - segment_locations[latter + bias][0]
                positions_1 = arange(segment_locations[former - bias][0],
                                     segment_locations[former - bias][0] + max([length_1, length_2]) + 1)
                positions_2 = arange(segment_locations[latter + bias][0],
                                     segment_locations[latter + bias][0] + max([length_1, length_2]) + 1)
                for index_1, index_2 in zip(positions_1[::-1], positions_2):
                    if index_1 >= 78 or index_2 >= 78:
                        continue
                    matrix[index_1, index_2] = max([matrix[index_1, index_2], value])
                    matrix[index_2, index_1] = max([matrix[index_2, index_1], value])


coordinates = MDS(n_components=3, dissimilarity="precomputed", random_state=2025).fit_transform(1.0 - matrix)
with open("output.pdb", "w") as file:
    for i, (x, y, z) in enumerate(coordinates, start=1):
        file.write(
            "ATOM  {:5d}  CA  DUM A{:4d}    {:8.3f}{:8.3f}{:8.3f}  1.00  0.00\n".format(
                i, i, x * 7, y * 7, z * 7
            )
        )
    file.write("END\n")

color_collection = []
residue_collection = []
last = 0
for addition, value in infos:
    color = colors[value][1:]
    r = int(color[0:2], 16) / 255.0
    g = int(color[2:4], 16) / 255.0
    b = int(color[4:6], 16) / 255.0
    color_set_code = "set_color " + color + ", [" + str(r) + ", " + str(g) + ", " + str(b) + "]"
    if color_set_code not in color_collection:
        color_collection.append(color_set_code)
    if last + 1 < last + addition:
        residue_collection.append("color " + color + ", resi " + str(last + 1) + "-" + str(last + addition))
    else:
        residue_collection.append("color " + color + ", resi " + str(last + 1))
    last += addition
for color_code in color_collection:
    print(color_code)
for plot_info in residue_collection:
    print(plot_info)
print("png output.png, width=4000, height=4000, dpi=300, ray=1")
# TODO please paste styled content into PyMOL Software.