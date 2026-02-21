"""
@Author      : Haoling Zhang
@Description : Figure 6
"""
from logging import getLogger, CRITICAL
from matplotlib import pyplot, rcParams
from numpy import linspace, arange, zeros, max
from warnings import filterwarnings

from code import capsule

filterwarnings("ignore")

getLogger("matplotlib").setLevel(CRITICAL)

rcParams["font.family"] = "Arial"
rcParams["mathtext.fontset"] = "custom"
rcParams["mathtext.rm"] = "Linux Libertine"
rcParams["mathtext.cal"] = "Lucida Calligraphy"
rcParams["mathtext.it"] = "Linux Libertine:italic"
rcParams["mathtext.bf"] = "Linux Libertine:bold"


figure = pyplot.figure(figsize=(7.2, 3.0), tight_layout=True)

pyplot.subplot(1, 2, 1)

pyplot.fill_between([0.33, 0.67], 0.79, 1.00, ec="none", fc="#EEEEEE", zorder=1)

x_locations = linspace(0.35, 0.65, 59)[1::2]
y_locations = linspace(0.98, 0.80, 11)[1::2]

colors = ["#666666", "#CD8F5B", "#A671D1", "#28ACB6", "#A94823"]
plotted_indices = [1, 1, 1, 0, 2, 0, 4, 0, 0,
                   0, 0, 0, 0, 4, 0, 0, 0, 3,
                   0, 0, 0, 0, 1, 1, 1, 0, 4, 0, 1, 1, 0, 2, 2, 2, 2, 2, 0, 3, 0, 0, 4, 0, 0, 0, 3, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4,
                   0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 4]
strings = ["def f(i):",
           "    o = 1",
           "    for v in range(1, i + 1):",
           "        o *= v",
           "    return o"]
index = 0
for index_1, (string, y_location) in enumerate(zip(strings, y_locations)):
    for index_2, (info, x_location) in enumerate(zip(string, x_locations)):
        pyplot.text(x_location, y_location, info, va="center", ha="center",
                    color=colors[plotted_indices[index]], fontsize=4.5, fontweight="bold", zorder=2)
        index += 1
values, length = [], 0
for string in strings:
    value = "".join(format(byte, "08b") for byte in (string + "\n").encode("ascii"))
    values.append(value)
    length += len(value)

pyplot.hlines(0.79, 0.607, 0.670, lw=0.5, color="#AAAAAA", zorder=2)
pyplot.text(0.67, 0.78, "Python", va="top", ha="right", fontsize=5, zorder=2)

pyplot.annotate("", xy=(0.50, 0.79), xytext=(0.50, 0.72), zorder=0,
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.5, mutation_scale=5))
pyplot.text(0.49, 0.76, "binarize code lines (based on ASCII format)", va="center", ha="right", fontsize=4.5)

pyplot.fill_between([0.003, 0.997], 0.61, 0.72, ec="none", fc="#EEEEEE", zorder=1)

x_locations = linspace(0.02, 0.98, 481)[1::2]
y_locations = linspace(0.71, 0.62, 11)[1::2]
collection_0, collection_1 = [[], []], [[], []]
path, length = [[], []], 0
for index_1, (value, y_location) in enumerate(zip(values, y_locations)):
    path[0].append(x_locations[0] - 0.007)
    path[1].append(y_locations[index_1])
    x_location = None
    length += len(value)
    for index_2, (info, x_location) in enumerate(zip(value, x_locations)):
        if info == "0":
            collection_0[0].append(x_location)
            collection_0[1].append(y_location)
        else:
            collection_1[0].append(x_location)
            collection_1[1].append(y_location)
    path[0].append(x_location + 0.007)
    path[1].append(y_locations[index_1])
    if index_1 < 4:
        path[0].append(x_location + 0.007)
        path[1].append((y_locations[index_1] + y_locations[index_1 + 1]) / 2.0)
        path[0].append(x_locations[0] - 0.007)
        path[1].append((y_locations[index_1] + y_locations[index_1 + 1]) / 2.0)
pyplot.text(path[0][-1] + 0.005, path[1][-1] - 0.002, "%d bits (%d bytes)" % (length, length // 8),
            va="center", ha="left", fontsize=3)

pyplot.plot(path[0], path[1], lw=0.25, color="k", zorder=2)
pyplot.scatter(collection_0[0], collection_0[1], marker="s", ec="k", fc="w", lw=0.25, s=0.6, zorder=3)
pyplot.scatter(collection_1[0], collection_1[1], marker="s", ec="k", fc="k", lw=0.25, s=0.6, zorder=3)

pyplot.hlines(0.61, 0.794, 0.997, lw=0.5, color="#AAAAAA", zorder=2)
x_locations = linspace(0.7, 1.0, 4)[1:-1]
y_locations = [0.591, 0.591]
pyplot.scatter([x_locations[0]], [y_locations[0]], marker="s", ec="k", fc="w", lw=0.4, s=7, zorder=3)
pyplot.text(x_locations[0] + 0.01, y_locations[0] - 0.001, "0", va="center", ha="left", fontsize=4.5)
pyplot.scatter([x_locations[1]], [y_locations[1]], marker="s", ec="k", fc="k", lw=0.4, s=7, zorder=3)
pyplot.text(x_locations[1] + 0.01, y_locations[1] - 0.001, "1", va="center", ha="left", fontsize=4.5)

pyplot.annotate("", xy=(0.50, 0.61), xytext=(0.50, 0.54), zorder=0,
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.5, mutation_scale=5))
pyplot.text(0.49, 0.58, "highlight interaction relations in the bit form",
            va="center", ha="right", fontsize=4.5)

colors = ["#555555", "#CD8F5B", "#A671D1", "#28ACB6", "#A94823", "#FFFFFF"]
infos = [(3, 1), (1, 5), (1, 2), (1, 0), (1, 4), (1, 0), (1, 0), (1, 5),
         (4, 5), (1, 4), (1, 5), (1, 0), (1, 5), (1, 2), (1, 5),
         (4, 5), (3, 1), (1, 5), (1, 4), (1, 5), (2, 1), (1, 5), (5, 2),
         (1, 0), (1, 3), (1, 0), (1, 5), (1, 4), (1, 5), (1, 0), (1, 5), (1, 3), (1, 0), (1, 0), (1, 5),
         (8, 5), (1, 4), (1, 5), (2, 0), (1, 5), (1, 4), (1, 5),
         (4, 5), (6, 1), (1, 5), (1, 4), (1, 5)]

pyplot.fill_between([0.003, 0.997], 0.36, 0.54, ec="none", fc="#EEEEEE", zorder=1)
locations = linspace(0.02, 0.98, 79)
segment_locations = []
last = 0
for addition, value in infos:
    pyplot.fill_between([locations[last], locations[last + addition]], 0.47, 0.48,
                        ec="none", fc=colors[value], lw=0, zorder=2)
    if last + addition < len(locations):
        pyplot.vlines(locations[last + addition], 0.47, 0.48, lw=0.50, color="k", zorder=3)
    segment_locations.append((locations[last] + locations[last + addition]) / 2.0)
    last += addition
pyplot.fill_between([0.02, 0.98], 0.47, 0.48, ec="k", fc="none", lw=0.50, zorder=3)
pyplot.plot([segment_locations[4], segment_locations[4], segment_locations[27]],
            [0.48, 0.53, 0.53], lw=0.3, color="k", zorder=4)
pyplot.annotate("", xy=(segment_locations[27], 0.53), xytext=(segment_locations[27], 0.51), zorder=4,
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.3, mutation_scale=5))
pyplot.plot([segment_locations[9], segment_locations[9], segment_locations[45]],
            [0.48, 0.50, 0.50], lw=0.3, color="k", zorder=4)
pyplot.vlines([segment_locations[13], segment_locations[40]], 0.48, 0.50, lw=0.3, color="k", zorder=4)
pyplot.annotate("", xy=(segment_locations[36], 0.50), xytext=(segment_locations[36], 0.48), zorder=4,
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.3, mutation_scale=5))
pyplot.annotate("", xy=(segment_locations[45], 0.50), xytext=(segment_locations[45], 0.48), zorder=4,
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.3, mutation_scale=5))
pyplot.plot([segment_locations[31], segment_locations[31], segment_locations[18]],
            [0.47, 0.45, 0.45], lw=0.3, color="k", zorder=4)
pyplot.vlines([segment_locations[24], segment_locations[27]], 0.45, 0.47, lw=0.3, color="k", zorder=4)
pyplot.annotate("", xy=(segment_locations[18], 0.45), xytext=(segment_locations[18], 0.47), zorder=4,
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.3, mutation_scale=5))
pyplot.plot([segment_locations[18], segment_locations[18], segment_locations[40]],
            [0.44, 0.43, 0.43], lw=0.3, color="k", zorder=4)
pyplot.annotate("", xy=(segment_locations[40], 0.43), xytext=(segment_locations[40], 0.47), zorder=4,
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.3, mutation_scale=5))
locations = linspace(0.02, 0.98, 27)
labels = arange(0, 27 * 3 + 1, 3)
pyplot.hlines(0.42, 0.013, 0.987, lw=0.50, color="k")
for location, label in zip(locations, labels):
    pyplot.vlines(location, 0.413, 0.420, lw=0.25, color="k")
    pyplot.text(location, 0.397, str(label), va="center", ha="center", fontsize=4)
pyplot.text(0.500, 0.375, "byte order", va="center", ha="center", fontsize=4)

x_locations = linspace(0.7, 1.0, 4)[:-1]
pyplot.hlines(0.36, 0.694, 0.997, lw=0.5, color="#AAAAAA", zorder=2)
y_locations = [0.341, 0.311]
labels = ["symbol", "keyword", "function", "constant", "variable", "escape"]
for index_1, y_location in enumerate(y_locations):
    for index_2, x_location in enumerate(x_locations):
        index = index_1 * 3 + index_2
        pyplot.scatter([x_location], [y_location], marker="s", ec="k", fc=colors[index], lw=0.4, s=7, zorder=3)
        pyplot.text(x_location + 0.01, y_location - 0.001, labels[index], va="center", ha="left", fontsize=4.5)

pyplot.annotate("", xy=(0.50, 0.36), xytext=(0.50, 0.29), zorder=0,
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.5, mutation_scale=5))
pyplot.text(0.49, 0.33, "construct contact map and protein-like structure", zorder=2,
            va="center", ha="right", fontsize=4.5)

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
    if last + addition < len(locations):
        pyplot.vlines(locations[last + addition], 0.47, 0.48, lw=0.50, color="k", zorder=3)
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

pyplot.fill_between([0.06, 0.07], 0.09, 0.20, ec="k", fc="none", lw=0.5, zorder=2)
locations = linspace(0.09, 0.20, 51)
for former, latter, color in zip(locations[:-1], locations[1:], pyplot.get_cmap("binary")(linspace(0, 1))):
    pyplot.fill_between([0.06, 0.07], former, latter, ec="none", fc=color, lw=0, zorder=1)
locations = linspace(0.09, 0.20, 3)
for location, label in zip(linspace(0.09, 0.20, 3), ["0%", "50%", "100%"]):
    pyplot.hlines(location, 0.070, 0.075, lw=0.50, color="k")
    pyplot.text(0.08, location, label, va="center", ha="left", fontsize=4)
pyplot.text(0.065, 0.240, "interaction\nprobability", va="center", ha="center", fontsize=4)
pyplot.pcolormesh(linspace(0.18, 0.36, 79), linspace(0.04, 0.25, 79), matrix,
                  vmin=0, vmax=1, cmap="binary")

pyplot.annotate("", xy=(0.180, 0.040), xytext=(0.372, 0.040), zorder=1,
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.5, mutation_scale=5))
pyplot.annotate("", xy=(0.180, 0.040), xytext=(0.180, 0.264), zorder=1,
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.5, mutation_scale=5))
pyplot.text(0.164, 0.145, "byte order", va="center", ha="center", fontsize=4, rotation=90)
pyplot.text(0.270, 0.020, "byte order", va="center", ha="center", fontsize=4)

pyplot.text(0.50, 0.180, "multidimensional\nscaling", va="center", ha="center", fontsize=4)
pyplot.annotate("", xy=(0.410, 0.145), xytext=(0.590, 0.145), zorder=1,
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.5, mutation_scale=5))
pyplot.text(0.50, 0.105, "PyMOL software\n(with colouring)", va="center", ha="center", fontsize=4)

pyplot.fill_between([0.64, 0.82], 0.04, 0.25, ec="k", fc="none", lw=0.5, zorder=2)

pyplot.xlim(0, 1)
pyplot.ylim(0, 1)
pyplot.axis("off")

# noinspection PyTypeChecker
ax = pyplot.subplot(1, 2, 2)

colors = ["#555555", "#CD8F5B", "#A671D1", "#28ACB6", "#A94823"]
string_groups = [["def f(s):",
                  "    d = 0",
                  "    for c1, c2 in zip(s, \"GAATTC\"):",
                  "        if c1 != c2:",
                  "            d += 1",
                  "    return d"],
                 ["def f(s):",
                  "    p = []",
                  "    for i in range(len(s) - 2):",
                  "        if s[i: i + 3] == \"ATG\":",
                  "            p += [i]",
                  "    return p"],
                 ["def f(s):",
                  "    n = 0",
                  "    for c in s:",
                  "        if c in [\"C\", \"G\"]:",
                  "            n += 1",
                  "    return n"]]

plotted_index_groups = [
    [1, 1, 1, 0, 2, 0, 4, 0, 0,
     0, 0, 0, 0, 4, 0, 0, 0, 3,
     0, 0, 0, 0, 1, 1, 1, 0, 4, 4, 0, 0, 4, 4, 0, 1, 1, 0, 2, 2, 2, 0, 4, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 4, 4, 0, 0, 0, 0, 4, 4, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 3,
     0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 4],
    [1, 1, 1, 0, 2, 0, 4, 0, 0,
     0, 0, 0, 0, 4, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 1, 1, 1, 0, 4, 0, 1, 1, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 0, 4, 0, 0, 0, 0, 3, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 4, 0, 4, 0, 0, 4, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0,
     0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 4],
    [1, 1, 1, 0, 2, 0, 4, 0, 0,
     0, 0, 0, 0, 4, 0, 0, 0, 3,
     0, 0, 0, 0, 1, 1, 1, 0, 4, 0, 1, 1, 0, 4, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 4, 0, 1, 1, 0, 0, 3, 3, 3, 0, 0, 3, 3, 3, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 3,
     0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 4]
]

pyplot.annotate("", xy=(0.21, 0.97), xytext=(0.21, 0.93), zorder=0,
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.5, mutation_scale=5))
pyplot.text(0.21, 0.99, "observed 10,000,000 samples", va="center", ha="center", fontsize=4.5)
pyplot.fill_between([0.00, 0.42], 0.68, 0.93, ec="none", fc="#EEEEEE", zorder=1)
x_locations = linspace(0.02, 0.40, 71)[1::2]
y_locations = linspace(0.91, 0.69, 13)[1::2]
index = 0
for index_1, (string, y_location) in enumerate(zip(string_groups[0], y_locations)):
    for index_2, (info, x_location) in enumerate(zip(string, x_locations)):
        pyplot.text(x_location, y_location, info, va="center", ha="center",
                    color=colors[plotted_index_groups[0][index]], fontsize=4.5, fontweight="bold", zorder=2)
        index += 1

pyplot.annotate("", xy=(0.79, 0.97), xytext=(0.79, 0.93), zorder=0,
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.5, mutation_scale=5))

pyplot.text(0.79, 0.99, "observed 10,000,000 samples", va="center", ha="center", fontsize=4.5)
pyplot.fill_between([0.58, 1.00], 0.68, 0.93, ec="none", fc="#EEEEEE", zorder=1)
x_locations = linspace(0.60, 0.98, 71)[1::2]
y_locations = linspace(0.91, 0.69, 13)[1::2]
index = 0
for index_1, (string, y_location) in enumerate(zip(string_groups[1], y_locations)):
    for index_2, (info, x_location) in enumerate(zip(string, x_locations)):
        pyplot.text(x_location, y_location, info, va="center", ha="center",
                    color=colors[plotted_index_groups[1][index]], fontsize=4.5, fontweight="bold", zorder=2)
        index += 1

pyplot.scatter([0.48, 0.50, 0.52], [0.805, 0.805, 0.805], color="k", s=1)
pyplot.text(0.50, 0.63, "grammar factorisation", va="bottom", ha="center", fontsize=5)
pyplot.plot([0.21, 0.21, 0.79, 0.79], [0.68, 0.62, 0.62, 0.68], lw=0.5, color="k", zorder=0)
pyplot.scatter([0.50], [0.62], ec="k", fc="w", lw=0.5, s=3, zorder=2)
pyplot.annotate("", xy=(0.50, 0.62), xytext=(0.50, 0.58), zorder=0,
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.5, mutation_scale=5))
pyplot.text(0.50, 0.56, "modular grammar library", va="center", ha="center", fontsize=5)
capsule(ax, (0.16, 0.32), 0.70, 0.22, 0.50, "k", "#E8EBF6", 0)
rules = ["x(0,i)-def- -x(1,j)-(-x(1,k)-)-:-x(1,n)",
         "x(0,i)-for- -x(1,j)- -in- -range-(-x(1,k)-)-:-x(1,n)",
         "x(0,i)-if- -x(1,j)- -:-x(1,k)",
         "x(1,i)-[+-*/]-=-x(1,j)",
         "x(1,i)-[!=]-=-x(1,j)"]
colors = ["#AAAAAA", "#555555", "#CD8F5B", "#A671D1", "#28ACB6", "#A94823"]
color_groups = [
    [0, 0, 4, 0, 5, 0, 0,
     2, 2, 2, 0, 0, 0, 0, 0, 4, 0, 5, 0, 0, 1, 0, 0, 0, 4, 0, 5, 0, 0, 1, 0, 1,
     0, 0, 0, 4, 0, 5, 0],
    [0, 0, 4, 0, 5, 0, 0,
     2, 2, 2, 0, 0, 0, 0, 0, 4, 0, 5, 0, 0, 0, 0, 2, 2, 0, 0, 0,
     3, 3, 3, 3, 3, 0, 1, 0, 0, 0, 4, 0, 5, 0, 0, 1, 0, 1, 0,
     0, 0, 4, 0, 5, 0, 0],
    [0, 0, 4, 0, 5, 0, 0,
     2, 2, 0, 0, 0, 0, 0, 4, 0, 5, 0, 0, 0, 0, 1, 0,
     0, 0, 4, 0, 5, 0, 0],
    [0, 0, 4, 0, 5, 0, 0,
     0, 1, 1, 1, 1, 0, 0, 1, 0,
     0, 0, 4, 0, 5, 0, 0],
    [0, 0, 4, 0, 5, 0, 0,
     0, 1, 1, 0, 0, 1, 0,
     0, 0, 4, 0, 5, 0, 0]
]
values = linspace(0.31, 0.69, 71)[1::2]
bias = values[1] - values[0]
locations = [[0.62, 0.45], [0.48, 0.40], [0.40, 0.50], [0.37, 0.35], [0.64, 0.35]]
for location, rule, plotted_indices in zip(locations, rules, color_groups):
    if len(rule) % 2 == 0:
        bias_value = (len(rule) // 2 + 0.5) * bias
    else:
        bias_value = len(rule) // 2 * bias
    positions = linspace(location[0] - bias_value, location[0] + bias_value, len(rule))
    for index, (position, info) in enumerate(zip(positions, rule)):
        pyplot.text(position, location[1], info, va="center", ha="center",
                    color=colors[plotted_indices[index]], fontweight="bold", fontsize=4.5)

colors = ["#555555", "#CD8F5B", "#A671D1", "#28ACB6", "#A94823"]
pyplot.annotate("", xy=(0.50, 0.32), xytext=(0.50, 0.25), zorder=0,
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.5, mutation_scale=5))
pyplot.hlines(0.29, 0.50, 0.525, lw=0.5, color="k", zorder=0)
pyplot.scatter([0.50], [0.29], ec="k", fc="w", lw=0.5, s=3, zorder=2)
pyplot.text(0.535, 0.29, "observed 100,000 samples", va="center", ha="left", fontsize=4.5)
pyplot.fill_between([0.29, 0.71], 0.00, 0.25, ec="none", fc="#EEEEEE", zorder=1)
x_locations = linspace(0.31, 0.69, 71)[1::2]
y_locations = linspace(0.23, 0.01, 13)[1::2]
index = 0
for index_1, (string, y_location) in enumerate(zip(string_groups[2], y_locations)):
    for index_2, (info, x_location) in enumerate(zip(string, x_locations)):
        if index < len(plotted_index_groups[2]):
            pyplot.text(x_location, y_location, info, va="center", ha="center",
                        color=colors[plotted_index_groups[2][index]], fontsize=4.5, fontweight="bold", zorder=2)
        index += 1

pyplot.xlim(-0.05, 1)
pyplot.ylim(0, 1)
pyplot.axis("off")

figure.text(0.01, 0.98, "a", va="center", ha="center", fontsize=8)
figure.text(0.51, 0.98, "b", va="center", ha="center", fontsize=8)

pyplot.savefig("./plot/6.pdf", format="pdf", pad_inches=0.02, bbox_inches="tight", dpi=300)
pyplot.close()
