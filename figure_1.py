"""
@Author      : Haoling Zhang
@Description : Figure 1
"""
from logging import getLogger, CRITICAL
from matplotlib import pyplot, rcParams
from numpy import array, load, linspace, arange, min, max, sum

from code import capsule, closed_curve, plot_shape
from code import random_scatters_g, random_scatters_lo, random_scatters_li, random_scatters_b
from warnings import filterwarnings

filterwarnings("ignore")

getLogger("matplotlib").setLevel(CRITICAL)

rcParams["font.family"] = "Arial"
rcParams["mathtext.fontset"] = "custom"
rcParams["mathtext.rm"] = "Linux Libertine"
rcParams["mathtext.cal"] = "Lucida Calligraphy"
rcParams["mathtext.it"] = "Linux Libertine:italic"
rcParams["mathtext.bf"] = "Linux Libertine:bold"


figure = pyplot.figure(figsize=(7.2, 2), tight_layout=True)

ax = pyplot.subplot(111)
pyplot.text(0.91, 1.60, "protein\nsequence\nuniverse", ha="center", va="center", fontweight="bold", fontsize=5)
pyplot.text(0.91, 1.25, "~$10^{44236}$\nprotein sequences", ha="center", va="center", fontsize=4.5)
for start in range(4):
    capsule(ax, (start + 1.10, 1.05), 0.80, 0.80, 0.75, "#9EABCF", "#E8EBF6", 0)
    if start == 1:
        pyplot.text(start + 1.50, 1.92, "stage " + str(start + 1) + " (current)", ha="center", va="center", fontsize=5)
    elif start == 2:
        pyplot.text(start + 1.50, 1.92, "stage " + str(start + 1) + " (next)", ha="center", va="center", fontsize=5)
    else:
        pyplot.text(start + 1.50, 1.92, "stage " + str(start + 1), ha="center", va="center", fontsize=5)

universe_data = load("./data/universe.npz")
counts = {
    15: [7, 6], 16: [2, 0], 17: [1, 1], 18: [3, 2], 19: [1, 1], 20: [1, 0],
    21: [3, 1], 22: [3, 1], 23: [2, 1], 24: [3, 2], 25: [1, 0], 26: [1, 1],
    27: [1, 0], 28: [6, 2], 29: [1, 0], 40: [2, 0], 41: [8, 3], 42: [1, 0],
    43: [2, 0], 44: [3, 1], 45: [4, 2], 46: [1, 0], 47: [5, 2], 48: [7, 2],
    49: [1, 0], 60: [2, 1], 61: [3, 1], 62: [5, 2], 63: [3, 1], 64: [1, 0],
    65: [5, 2], 66: [5, 2], 67: [3, 1], 68: [7, 2], 69: [3, 1], 70: [3, 1],
    71: [3, 1], 72: [3, 1], 73: [6, 2], 74: [3, 1]
}

# stage 1
saved_points, xs, y = None, [], None
for index in range(1, 81):
    if index in arange(15, 30) or index in arange(40, 50) or index in arange(60, 75):
        points = random_scatters_g(universe_data["c-" + str(index).zfill(2)], (1.12, 1.10), 0.76, 0.70,
                                   counts[index][0], 0.00, 2025)
        if index != 15:
            pyplot.scatter(points[:, 0], points[:, 1], ec="#000000", fc="#AAAAAA", lw=0.15, s=1.50, zorder=4)
        else:
            pyplot.scatter(points[:, 0], points[:, 1], ec="#000000", fc="#FFCA78", lw=0.15, s=1.50, zorder=4)
            pyplot.fill_between([min(points[:, 0]) - 0.01, max(points[:, 0]) + 0.01],
                                min(points[:, 1]) - 0.02, max(points[:, 1]) + 0.02, lw=0.25, ls=":",
                                ec="#000000", fc="none", zorder=5)
            saved_points, xs, y = points, [min(points[:, 0]) - 0.01, max(points[:, 0]) + 0.01], min(points[:, 1]) - 0.02
pyplot.plot([0.70, xs[0]], [0.75, y], lw=0.25, color="k", ls=":", zorder=5)
pyplot.plot([1.15, xs[1]], [0.75, y], lw=0.25, color="k", ls=":", zorder=5)
pyplot.text(1.15, 0.76, "sequences\nfrom a function", ha="right", va="bottom", fontsize=4)  # insulin family
pyplot.fill_between([0.70, 1.15], 0.15, 0.75, lw=0.25, ls=":", ec="#000000", fc="#E8EBF6", zorder=1)
saved_points[:, 0] -= min(saved_points[:, 0])
saved_points[:, 0] /= max(saved_points[:, 0])
saved_points[:, 0] *= 0.39
saved_points[:, 0] += 0.73
saved_points[:, 1] -= min(saved_points[:, 1])
saved_points[:, 1] /= max(saved_points[:, 1])
saved_points[:, 1] *= 0.48
saved_points[:, 1] += 0.21
pyplot.scatter(saved_points[:, 0], saved_points[:, 1], ec="#000000", fc="#FFCA78", lw=0.20, s=10, zorder=4)
for index, (point, location) in enumerate(zip(saved_points, linspace(0.17, 0.73, 7)[::-1])):
    pyplot.text(point[0], point[1] - 0.004, str(index + 1), ha="center", va="center", fontsize=2.5, zorder=5)
    pyplot.text(1.175, location, str(index + 1), ha="center", va="center", fontsize=2.3, zorder=5)
sequences = [
    "-ISSQHLCGSHLVEALNLVCGDRGFFYNPRGIVEQCCHRPCSIFELENYCN",
    "-ADPQHLCGSHLVDALYLVCGDRGFFYNPKGIVEQCCHRPCNIRVLENYCN",
    "-YVGQRLCGSQLVDTLYSVCKHRGFYRPSEGIVDQCCTNICSRNQLLTYCN",
    "-AANPHLCGSHLVEALYLVCGERGFFYQPKGIHZZCCHKPCBIFZLZBYCN",
    "MAPPQHLCGSHLVDALYLVCGDRGFFYN-SGIVEQCCHRPCDKFDLQSYCN",
    "-AAAQHLCGSHLVDALYLVCGEKGFFYNPKGIVEQCCHKPCNIFDLQNYCN",
    "-ISSQHLCGSHLVEALNLVCGDRGFFYNPRGIVEQCCHRPCSMFELENYCN",
]
for sequence, y_location in zip(sequences, linspace(0.17, 0.73, 7)[::-1]):
    for letter, x_location in zip(sequence, linspace(1.20, 1.90)):
        pyplot.text(x_location, y_location, letter, ha="center", va="center", fontsize=2, zorder=5)
conserved_points = []
for index in range(50):
    letters = []
    for sequence in sequences:
        letters.append(sequence[index])
    if len(set(letters)) == 1:
        conserved_points.append(index)
locations = linspace(1.20, 1.90)[array(conserved_points)]
for location in locations:
    pyplot.fill_between([location - 0.007, location + 0.007], 0.15, 0.78, fc="#DDDDDD", lw=0.00, zorder=2)
pyplot.plot([locations[0], locations[0], locations[-1], locations[-1]], [0.78, 0.85, 0.85, 0.78],
            lw=0.20, color="k", zorder=1)
pyplot.vlines(locations[1:-1], 0.85, 0.78, lw=0.20, color="k", zorder=0)
pyplot.text((locations[0] + locations[-1]) / 2.0, 0.90, "absolutely conserved residues",
            ha="center", va="center", fontsize=4)

# stage 2
saved_points, additions, xs, y = None, None, None, None
for index in range(1, 81):
    if index in arange(15, 30) or index in arange(40, 50) or index in arange(60, 75):
        points = random_scatters_g(universe_data["c-" + str(index).zfill(2)], (2.12, 1.10), 0.76, 0.70,
                                   sum(counts[index]), 0.00, 2025)

        pyplot.scatter(points[:counts[index][0], 0], points[:counts[index][0], 1],
                       ec="#000000", fc="#AAAAAA", lw=0.15, s=1.50, zorder=4)
        if index == 15:
            if counts[index][1] > 0:
                pyplot.scatter(points[-counts[index][1]:, 0], points[-counts[index][1]:, 1],
                               ec="#000000", fc="#FFCA78", lw=0.15, s=1.50, zorder=5)
            minimum_x, maximum_x = (min(points[:, 0]) + max(points[:, 0])) / 2.0, max(points[:, 0])
            minimum_y, maximum_y = min(points[:, 1]), (min(points[:, 1]) + max(points[:, 1])) / 2.0 - 0.04
            additions = random_scatters_b(minimum_x, maximum_x, minimum_y, maximum_y, 5, 1e-2, 2025)
            pyplot.scatter(additions[:, 0], additions[:, 1],
                           ec="k", fc="#FFCA78", lw=0.15, s=1.50, zorder=5)
            pyplot.fill_between([min(points[:, 0]) - 0.01, max(points[:, 0]) + 0.01],
                                min(points[:, 1]) - 0.02, max(points[:, 1]) + 0.02, lw=0.25, ls=":",
                                ec="#000000", fc="none", zorder=5)
            saved_points, xs, y = points, [min(points[:, 0]) - 0.01, max(points[:, 0]) + 0.01], min(points[:, 1]) - 0.02
pyplot.plot([2.10, xs[0]], [0.75, y], lw=0.25, color="k", ls=":", zorder=5)
pyplot.plot([2.60, xs[1]], [0.75, y], lw=0.25, color="k", ls=":", zorder=5)
pyplot.scatter([2.18], [0.80], ec="#000000", fc="#AAAAAA", lw=0.20, s=10)
pyplot.scatter([2.40], [0.80], ec="#000000", fc="#FFCA78", lw=0.20, s=10)
pyplot.text(2.21, 0.80, "natural", ha="left", va="center", fontsize=4)
pyplot.text(2.43, 0.80, "synthetic", ha="left", va="center", fontsize=4)
pyplot.fill_between([2.10, 2.60], 0.15, 0.75, lw=0.25, ls=":", ec="#000000", fc="#E8EBF6", zorder=1)
additions[:, 0] -= min(saved_points[:, 0])
saved_points[:, 0] -= min(saved_points[:, 0])
additions[:, 0] /= max(saved_points[:, 0])
saved_points[:, 0] /= max(saved_points[:, 0])
additions[:, 0] *= 0.44
saved_points[:, 0] *= 0.44
additions[:, 0] += 2.13
saved_points[:, 0] += 2.13
additions[:, 1] -= min(saved_points[:, 1])
saved_points[:, 1] -= min(saved_points[:, 1])
additions[:, 1] /= max(saved_points[:, 1])
saved_points[:, 1] /= max(saved_points[:, 1])
additions[:, 1] *= 0.48
saved_points[:, 1] *= 0.48
additions[:, 1] += 0.21
saved_points[:, 1] += 0.21
pyplot.scatter(saved_points[:counts[15][0], 0], saved_points[:counts[15][0], 1],
               ec="#000000", fc="#AAAAAA", lw=0.20, s=10, zorder=4)
for index, point in enumerate(saved_points[-counts[15][1]:]):
    if index != 2:
        pyplot.scatter([point[0]], [point[1]],
                       ec="#000000", fc="#FFCA78", lw=0.20, s=10, zorder=4)
    else:
        pyplot.scatter([point[0] + 0.01], [point[1]],
                       ec="#000000", fc="#FFCA78", lw=0.20, s=10, zorder=4)
pyplot.scatter(additions[:, 0], additions[:, 1],
               ec="#000000", fc="#FFCA78", lw=0.20, s=10, zorder=4)
for index, point in enumerate(saved_points[-counts[15][1]:]):
    if index != 2:
        if len(str(index)) == 1:
            pyplot.text(point[0], point[1] - 0.004, str(index + 1),
                        ha="center", va="center", fontsize=2.3, zorder=5)
        else:
            pyplot.text(point[0], point[1] - 0.004, "1", ha="center", va="center", fontsize=2.3, zorder=5)
            pyplot.text(point[0], point[1] - 0.004, str(index - 10), ha="center", va="center", fontsize=2.3, zorder=5)
    else:
        pyplot.text(point[0] + 0.01, point[1] - 0.004, str(index + 1),
                    ha="center", va="center", fontsize=2.3, zorder=5)
for index, point in enumerate(additions):
    pyplot.text(point[0], point[1] - 0.004, str(index + 7), ha="center", va="center", fontsize=2.3, zorder=5)
pyplot.text(2.77, 0.90, "fitness", ha="center", va="center", fontsize=4.0)
pyplot.plot([2.64, 2.64, 2.90, 2.90], [0.80, 0.85, 0.85, 0.80], lw=0.20, color="k", zorder=0)
locations = linspace(0.72, 0.17, 6)
fitnesses = ["1.00", "0.99", "0.97", "0.98", "0.95", "0.93", "0.96", "0.41", "0.12", "0.06", "0.17", "0.32"]
for index in range(12):
    location = locations[index % 6]
    if index < 6:
        if index != 0:
            pyplot.scatter([2.67], [location], ec="#000000", fc="#FFCA78", lw=0.20, s=10, zorder=4)
            pyplot.text(2.67, location - 0.004, str(index), ha="center", va="center", fontsize=2.3, zorder=5)
        else:
            pyplot.scatter([2.67], [location], ec="#000000", fc="#AAAAAA", lw=0.20, s=10, zorder=4)
        pyplot.text(2.70, location, fitnesses[index], ha="left", va="center", fontsize=2.3, zorder=5)
    else:
        pyplot.scatter([2.81], [location], ec="#000000", fc="#FFCA78", lw=0.20, s=10, zorder=4)
        if len(str(index)) == 1:
            pyplot.text(2.81, location - 0.004, str(index), ha="center", va="center", fontsize=2.3, zorder=5)
        else:
            pyplot.text(2.805, location - 0.004, "1", ha="center", va="center", fontsize=2.3, zorder=5)
            pyplot.text(2.815, location - 0.004, str(index - 10), ha="center", va="center", fontsize=2.3, zorder=5)
        pyplot.text(2.84, location, fitnesses[index], ha="left", va="center", fontsize=2.5, zorder=5)
pyplot.fill_between([2.78, 2.90], 0.13, 0.66, fc="#DDDDDD", lw=0.00, zorder=2)

# stage 3
xs, y = [], None
for index in range(1, 81):
    if index in arange(15, 30) or index in arange(40, 50) or index in arange(60, 75):
        if index != 15:
            points = random_scatters_g(universe_data["c-" + str(index).zfill(2)], (3.12, 1.10), 0.76, 0.70,
                                       sum(counts[index]), 0.00, 2025)
            pyplot.scatter(points[:, 0], points[:, 1], ec="#000000", fc="#AAAAAA", lw=0.15, s=1.50, zorder=4)
        else:  # 15 is investigated in stage 3
            curve = universe_data["c-" + str(index).zfill(2)]
            closed_curve(ax, curve, (3.12, 1.10), 0.76, 0.70, 0.25, "#000000", "#FFCA78", 1)
            adjusted_curve = curve.copy()
            adjusted_curve[:, 0] *= 0.76
            adjusted_curve[:, 1] *= 0.70
            adjusted_curve[:, 0] += 3.12
            adjusted_curve[:, 1] += 1.10
            pyplot.fill_between([min(adjusted_curve[:, 0]) - 0.02, max(adjusted_curve[:, 0]) + 0.02],
                                min(adjusted_curve[:, 1]) - 0.04, max(adjusted_curve[:, 1]) + 0.04,
                                lw=0.25, ls=":", ec="#000000", fc="none", zorder=5)
            xs = [min(adjusted_curve[:, 0]) - 0.02, max(adjusted_curve[:, 0]) + 0.02]
            y = min(adjusted_curve[:, 1]) - 0.04
pyplot.scatter([3.06], [0.90], ec="#000000", fc="#FFCA78", lw=0.20, s=10)
pyplot.scatter([3.06], [0.80], ec="#000000", fc="#AAAAAA", lw=0.20, s=10)
pyplot.text(3.09, 0.90, "functon presence", ha="left", va="center", fontsize=4)
pyplot.text(3.09, 0.80, "functon absence", ha="left", va="center", fontsize=4)
pyplot.fill_between([3.05, 3.40], 0.15, 0.75, lw=0.25, ls=":", ec="#000000", fc="#E8EBF6", zorder=1)
curve = universe_data["c-15"]
adjusted_curve = curve.copy()
adjusted_curve[:, 0] -= min(adjusted_curve[:, 0])
adjusted_curve[:, 0] /= max(adjusted_curve[:, 0])
adjusted_curve[:, 1] -= min(adjusted_curve[:, 1])
adjusted_curve[:, 1] /= max(adjusted_curve[:, 1])
adjusted_curve[:, 0] *= 0.25
adjusted_curve[:, 0] += 3.10
adjusted_curve[:, 1] *= 0.38
adjusted_curve[:, 1] += 0.26
points_1 = random_scatters_li(adjusted_curve, 60, 2.5e-2, 2025)
pyplot.scatter(points_1[:, 0], points_1[:, 1], ec="#000000", fc="#FFCA78", lw=0.15, s=3.0, zorder=5)
points_2 = random_scatters_lo(3.07, 3.38, 0.19, 0.71,
                              adjusted_curve, 65, 3.0e-2, points_1, 2025)
pyplot.scatter(points_2[:, 0], points_2[:, 1], ec="#000000", fc="#AAAAAA", lw=0.15, s=3.0, zorder=4)
pyplot.text(3.50, 0.53, "delineate", ha="center", va="center", fontsize=4, zorder=5)
pyplot.annotate("", xy=(3.40, 0.45), xytext=(3.60, 0.45),
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.20, mutation_scale=5))
pyplot.plot([3.60, xs[0]], [0.75, y], lw=0.25, color="k", ls=":", zorder=5)
pyplot.plot([3.95, xs[1]], [0.75, y], lw=0.25, color="k", ls=":", zorder=5)
pyplot.text(3.60, 0.76, "sequence galaxy", ha="left", va="bottom", fontsize=4, zorder=6)
pyplot.fill_between([3.60, 3.95], 0.15, 0.75, lw=0.25, ls=":", ec="#000000", fc="#E8EBF6", zorder=7)
curve = universe_data["c-15"]
adjusted_curve = curve.copy()
adjusted_curve[:, 0] -= min(adjusted_curve[:, 0])
adjusted_curve[:, 0] /= max(adjusted_curve[:, 0])
adjusted_curve[:, 1] -= min(adjusted_curve[:, 1])
adjusted_curve[:, 1] /= max(adjusted_curve[:, 1])
adjusted_curve[:, 0] *= 0.25
adjusted_curve[:, 0] += 3.65
adjusted_curve[:, 1] *= 0.38
adjusted_curve[:, 1] += 0.26
plot_shape(ax, adjusted_curve, 0.25, "#000000", "#FFCA78", 8)
pyplot.plot([3.97, 3.99, 3.99, 4.01, 4.01], [0.45, 0.45, 0.95, 0.95, 0.68], lw=0.20, color="k")
pyplot.annotate("", xy=(4.01, 0.68), xytext=(4.09, 0.68),
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.20, mutation_scale=5))
pyplot.text(4.00, 1.05, "represented by\nregular expression", ha="center", va="center", fontsize=4, zorder=8)

# stage 4
xs, y = [], None
for index in range(1, 81):
    if index in arange(15, 30) or index in arange(40, 50) or index in arange(60, 75):
        closed_curve(ax, universe_data["c-" + str(index).zfill(2)], (4.12, 1.10), 0.76, 0.70, 0.25,
                     "#000000", "#AAAAAA", 1)
    elif index == 52:
        curve = universe_data["c-" + str(index).zfill(2)]
        closed_curve(ax, curve, (4.12, 1.10), 0.76, 0.70, 0.25, "#000000", "#FFCA78", 1)
        adjusted_curve = curve.copy()
        adjusted_curve[:, 0] *= 0.76
        adjusted_curve[:, 1] *= 0.70
        adjusted_curve[:, 0] += 4.12
        adjusted_curve[:, 1] += 1.10
        pyplot.fill_between([min(adjusted_curve[:, 0]) - 0.02, max(adjusted_curve[:, 0]) + 0.02],
                            min(adjusted_curve[:, 1]) - 0.04, max(adjusted_curve[:, 1]) + 0.04,
                            lw=0.25, ls=":", ec="#000000", fc="none", zorder=5)
        xs = [min(adjusted_curve[:, 0]) - 0.02, max(adjusted_curve[:, 0]) + 0.02]
        y = min(adjusted_curve[:, 1]) - 0.04

locations = linspace(0.68, 0.22, 5)
for index, location in enumerate(locations[:3]):
    if index == 0:
        pyplot.text(4.20, location, "expression " + str(index + 1),
                    bbox=dict(fc="#CCCCCC", ec="k", lw=0.5, boxstyle="round,pad=0.3"),
                    va="center", ha="center", fontsize=3.0)
    else:
        pyplot.text(4.20, location, "expression " + str(index + 1), va="center", ha="center", fontsize=3.0)
pyplot.text(4.20, locations[-2], "· · ·", va="center", ha="center", fontsize=3.0)
pyplot.text(4.20, locations[-1], "expression n", va="center", ha="center", fontsize=3.0)
pyplot.plot([4.30, 4.32, 4.32, 4.30], [0.75, 0.75, 0.15, 0.15], lw=0.20, color="#000000")
pyplot.annotate("", xy=(4.32, 0.45), xytext=(4.51, 0.45),
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.20, mutation_scale=5))
pyplot.text(4.40, 0.52, "emerge", va="center", ha="center", fontsize=4.0)
pyplot.text(4.62, 0.45, "expression x",
            bbox=dict(fc="#FFCA78", ec="k", lw=0.5, boxstyle="round,pad=0.3"), va="center", ha="center", fontsize=3.0)
pyplot.text(4.73, 0.45, "=", va="center", ha="center", fontsize=3.0)
pyplot.plot([4.75, xs[0]], [0.75, y], lw=0.25, color="k", ls=":", zorder=5)
pyplot.plot([4.95, xs[1]], [0.75, y], lw=0.25, color="k", ls=":", zorder=5)
pyplot.fill_between([4.75, 4.95], 0.15, 0.75, lw=0.25, ls=":", ec="#000000", fc="#E8EBF6", zorder=7)
curve = universe_data["c-52"]
adjusted_curve = curve.copy()
adjusted_curve[:, 0] -= min(adjusted_curve[:, 0])
adjusted_curve[:, 0] /= max(adjusted_curve[:, 0])
adjusted_curve[:, 1] -= min(adjusted_curve[:, 1])
adjusted_curve[:, 1] /= max(adjusted_curve[:, 1])
adjusted_curve[:, 0] *= 0.08
adjusted_curve[:, 0] += 4.81
adjusted_curve[:, 1] *= 0.38
adjusted_curve[:, 1] += 0.26
plot_shape(ax, adjusted_curve, 0.25, "#000000", "#FFCA78", 8)

for start in range(3):
    pyplot.annotate("", xy=(start + 1.92, 1.45), xytext=(start + 2.08, 1.45),
                    arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.40))
    pyplot.text(start + 2.00, 1.60, "paradigm\nshift", ha="center", va="center", fontsize=4)
for index, label in enumerate(["Where in the sequence is function conserved?",
                               "How do variants affect the reference function?",
                               "What is the sequence galaxy of a given function?",
                               "Where can new functions be encoded in the universe?"]):
    pyplot.text(index + 1.50, 0.06, label, color="#C00000", ha="center", va="center", fontsize=4)

pyplot.xlim(0.70, 5.00)
pyplot.ylim(0.00, 2.00)
pyplot.axis("off")

pyplot.savefig("./plot/1.pdf", format="pdf", pad_inches=0.02, bbox_inches="tight", dpi=300)
pyplot.close()
