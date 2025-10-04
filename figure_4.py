"""
@Author      : Haoling Zhang
@Description : Figure 4
"""
from logging import getLogger, CRITICAL
from matplotlib import pyplot, rcParams
from numpy import array, load, linspace, arange, random, cos, pi

from code import plot_shape
from warnings import filterwarnings

filterwarnings("ignore")

getLogger("matplotlib").setLevel(CRITICAL)

rcParams["font.family"] = "Arial"
rcParams["mathtext.fontset"] = "custom"
rcParams["mathtext.rm"] = "Linux Libertine"
rcParams["mathtext.cal"] = "Lucida Calligraphy"
rcParams["mathtext.it"] = "Linux Libertine:italic"
rcParams["mathtext.bf"] = "Linux Libertine:bold"


ref_x, ref_y = linspace(0.00, 0.60, 7), linspace(1.00, 0.00, 11)[:-1] - 0.05

anchor_locations = array([[ref_x[2], ref_y[0]], [ref_x[4], ref_y[0]],
                          [ref_x[1], ref_y[1]], [ref_x[3], ref_y[1]], [ref_x[5], ref_y[1]],
                          [ref_x[1], ref_y[2]], [ref_x[3], ref_y[2]], [ref_x[5], ref_y[2]],
                          [ref_x[1], ref_y[3]], [ref_x[3], ref_y[3]], [ref_x[5], ref_y[3]],
                          [ref_x[1], ref_y[4]], [ref_x[3], ref_y[4]], [ref_x[5], ref_y[4]],
                          [ref_x[1], ref_y[5]], [ref_x[3], ref_y[5]], [ref_x[5], ref_y[5]],
                          [ref_x[1], ref_y[6]], [ref_x[3], ref_y[6]], [ref_x[5], ref_y[6]],
                          [ref_x[1], ref_y[7]], [ref_x[3], ref_y[7]], [ref_x[5], ref_y[7]],
                          [ref_x[1], ref_y[8]], [ref_x[3], ref_y[8]], [ref_x[5], ref_y[8]],
                          [ref_x[1], ref_y[9]], [ref_x[3], ref_y[9]], [ref_x[5], ref_y[9]]])

cell_data = load("./data/cell.npz")
colors = pyplot.get_cmap("RdYlBu")(linspace(0, 1, 27))

figure = pyplot.figure(figsize=(7.2, 2.8), tight_layout=True)

ax = pyplot.subplot(111)

for index, label in enumerate(["synthesize", "deliver", "observe"]):
    pyplot.annotate("", xy=(index + 0.87, 0.50), xytext=(index + 1.13, 0.50),
                    arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.50, mutation_scale=5))
    pyplot.text(index + 0.99, 0.51, label, va="bottom", ha="center", fontsize=5)


pyplot.fill_between([0.20 + anchor_locations[0, 0] - 0.05, 0.20 + anchor_locations[0, 0] + 0.05],
                    anchor_locations[0, 1] + 0.01, anchor_locations[0, 1] - 0.01, lw=0.5, ec="k", fc="none", zorder=1)
pyplot.fill_between([0.20 + anchor_locations[0, 0] - 0.02, 0.20 + anchor_locations[0, 0] + 0.02],
                    anchor_locations[0, 1] + 0.01, anchor_locations[0, 1] - 0.01, lw=0.5, ec="k", fc="k", zorder=0)
pyplot.fill_between([0.20 + anchor_locations[1, 0] - 0.02, 0.20 + anchor_locations[1, 0] + 0.02],
                    anchor_locations[0, 1] + 0.01, anchor_locations[0, 1] - 0.01, lw=0.5, ec="k", fc="none", zorder=1)
pyplot.vlines(0.20 + anchor_locations[1, 0], anchor_locations[0, 1] + 0.01, anchor_locations[0, 1] - 0.01,
              color="k", lw=0.5, zorder=1)

for location, color in zip(anchor_locations[2:], colors):
    pyplot.fill_between([0.20 + location[0] - 0.05, 0.20 + location[0] + 0.05],
                        location[1] + 0.01, location[1] - 0.01, lw=0.5, ec="k", fc="none", zorder=1)
    pyplot.fill_between([0.20 + location[0] - 0.02, 0.20 + location[0] + 0.02],
                        location[1] + 0.01, location[1] - 0.01, lw=0.5, ec="k", fc=color, zorder=0)

x_points = linspace(0.00, 0.03, 31) - 0.05
y_points_1, y_points_2 = cos(linspace(pi, 3 * pi, 31) - 1.00) * 0.01, cos(linspace(pi, 3 * pi, 31)) * 0.01
pyplot.plot(1.20 + anchor_locations[0, 0] + x_points, anchor_locations[0, 1] + y_points_1,
            color="#AAAAAA", lw=0.50, zorder=2)
pyplot.plot(1.20 + anchor_locations[0, 0] + x_points, anchor_locations[0, 1] - y_points_2,
            color="#AAAAAA", lw=0.50, zorder=2)
x_points = linspace(0.03, 0.07, 31) - 0.05
y_points_1, y_points_2 = cos(linspace(pi, 4 * pi, 31) - 1.00) * 0.01, cos(linspace(pi, 4 * pi, 31)) * 0.01
pyplot.plot(1.20 + anchor_locations[0, 0] + x_points, anchor_locations[0, 1] + y_points_1,
            color="k", lw=0.50, zorder=2)
pyplot.plot(1.20 + anchor_locations[0, 0] + x_points, anchor_locations[0, 1] - y_points_2,
            color="k", lw=0.50, zorder=2)
x_points = linspace(0.07, 0.10, 31) - 0.05
y_points_1, y_points_2 = cos(linspace(2 * pi, 4 * pi, 31) - 1.00) * 0.01, cos(linspace(2 * pi, 4 * pi, 31)) * 0.01
pyplot.plot(1.20 + anchor_locations[0, 0] + x_points, anchor_locations[0, 1] + y_points_1,
            color="#AAAAAA", lw=0.50, zorder=2)
pyplot.plot(1.20 + anchor_locations[0, 0] + x_points, anchor_locations[0, 1] - y_points_2,
            color="#AAAAAA", lw=0.50, zorder=2)

x_points = linspace(0.02, 0.05, 31) - 0.05
y_points_1, y_points_2 = cos(linspace(pi, 3 * pi, 31) - 1.00) * 0.01, cos(linspace(pi, 3 * pi, 31)) * 0.01
pyplot.plot(1.20 + anchor_locations[1, 0] + x_points, anchor_locations[1, 1] + y_points_1,
            color="#AAAAAA", lw=0.50, zorder=2)
pyplot.plot(1.20 + anchor_locations[1, 0] + x_points, anchor_locations[1, 1] - y_points_2,
            color="#AAAAAA", lw=0.50, zorder=2)
x_points = linspace(0.05, 0.08, 31) - 0.05
y_points_1, y_points_2 = cos(linspace(pi, 3 * pi, 31) - 1.00) * 0.01, cos(linspace(pi, 3 * pi, 31)) * 0.01
pyplot.plot(1.20 + anchor_locations[1, 0] + x_points, anchor_locations[1, 1] + y_points_1,
            color="#AAAAAA", lw=0.50, zorder=2)
pyplot.plot(1.20 + anchor_locations[1, 0] + x_points, anchor_locations[1, 1] - y_points_2,
            color="#AAAAAA", lw=0.50, zorder=2)

for location, color in zip(anchor_locations[2:], colors):
    x_points = linspace(0.00, 0.03, 31) - 0.05
    y_points_1, y_points_2 = cos(linspace(pi, 3 * pi, 31) - 1.00) * 0.01, cos(linspace(pi, 3 * pi, 31)) * 0.01
    pyplot.plot(1.20 + location[0] + x_points, location[1] + y_points_1,
                color="#AAAAAA", lw=0.50, zorder=2)
    pyplot.plot(1.20 + location[0] + x_points, location[1] - y_points_2,
                color="#AAAAAA", lw=0.50, zorder=2)
    x_points = linspace(0.03, 0.07, 31) - 0.05
    y_points_1, y_points_2 = cos(linspace(pi, 4 * pi, 31) - 1.00) * 0.01, cos(linspace(pi, 4 * pi, 31)) * 0.01
    pyplot.plot(1.20 + location[0] + x_points, location[1] + y_points_1,
                color=color, lw=0.50, zorder=2)
    pyplot.plot(1.20 + location[0] + x_points, location[1] - y_points_2,
                color=color, lw=0.50, zorder=2)
    x_points = linspace(0.07, 0.10, 31) - 0.05
    y_points_1, y_points_2 = cos(linspace(2 * pi, 4 * pi, 31) - 1.00) * 0.01, cos(linspace(2 * pi, 4 * pi, 31)) * 0.01
    pyplot.plot(1.20 + location[0] + x_points, location[1] + y_points_1,
                color="#AAAAAA", lw=0.50, zorder=2)
    pyplot.plot(1.20 + location[0] + x_points, location[1] - y_points_2,
                color="#AAAAAA", lw=0.50, zorder=2)
for location in anchor_locations:
    pyplot.fill_between([1.20 + location[0] - 0.06, 1.20 + location[0] + 0.06],
                        location[1] + 0.035, location[1] - 0.035, lw=0, ec="none", fc="#EEEEEE", zorder=0)

curve_1, curve_2 = cell_data["c-01"], cell_data["c-02"]
curve_1[:, 0] *= 0.10
curve_1[:, 1] *= 0.06
curve_2[:, 0] *= 0.10
curve_2[:, 1] *= 0.06
plot_shape(ax, curve_1 + array([2.20 + anchor_locations[0, 0] - 0.05, anchor_locations[0, 1] - 0.035]),
           lw=0.50, ec="k", fc="#FFFFFF", zorder=0)
plot_shape(ax, curve_2 + array([2.20 + anchor_locations[0, 0] - 0.05, anchor_locations[0, 1] - 0.035]),
           lw=0.50, ec="k", fc="#000000", zorder=0)
plot_shape(ax, curve_1 + array([2.20 + anchor_locations[1, 0] - 0.05, anchor_locations[1, 1] - 0.035]),
           lw=0.50, ec="k", fc="#FFFFFF", zorder=0)
plot_shape(ax, curve_2 + array([2.20 + anchor_locations[1, 0] - 0.05, anchor_locations[1, 1] - 0.035]),
           lw=0.50, ec="k", fc="#FFFFFF", zorder=0)
for location, color in zip(anchor_locations[2:], colors):
    plot_shape(ax, curve_1 + array([2.20 + location[0] - 0.05, location[1] - 0.035]),
               lw=0.50, ec="k", fc="#FFFFFF", zorder=0)
    plot_shape(ax, curve_2 + array([2.20 + location[0] - 0.05, location[1] - 0.035]),
               lw=0.50, ec="k", fc=color, zorder=0)
random.seed(2025)
indices = arange(27)
random.shuffle(indices)
plot_shape(ax, curve_1 + array([3.20 + anchor_locations[0, 0] - 0.05, anchor_locations[0, 1] - 0.035]),
           lw=0.50, ec="k", fc="#7FFF00", zorder=0)
plot_shape(ax, curve_2 + array([3.20 + anchor_locations[0, 0] - 0.05, anchor_locations[0, 1] - 0.035]),
           lw=0.50, ec="k", fc="#000000", zorder=0)

plot_shape(ax, curve_1 + array([3.20 + anchor_locations[1, 0] - 0.05, anchor_locations[1, 1] - 0.035]),
           lw=0.50, ec="k", fc="#FFFFFF", zorder=0)
plot_shape(ax, curve_2 + array([3.20 + anchor_locations[1, 0] - 0.05, anchor_locations[1, 1] - 0.035]),
           lw=0.50, ec="k", fc="#FFFFFF", zorder=0)

for index, (location, color) in enumerate(zip(anchor_locations[2:], colors)):
    if index in indices[:12]:
        plot_shape(ax, curve_1 + array([3.20 + location[0] - 0.05, location[1] - 0.035]),
                   lw=0.50, ec="k", fc="#7FFF00", zorder=0)
        plot_shape(ax, curve_2 + array([3.20 + location[0] - 0.05, location[1] - 0.035]),
                   lw=0.50, ec="k", fc=color, zorder=0)
    else:
        plot_shape(ax, curve_1 + array([3.20 + location[0] - 0.05, location[1] - 0.035]),
                   lw=0.50, ec="k", fc="#FFFFFF", zorder=0)
        plot_shape(ax, curve_2 + array([3.20 + location[0] - 0.05, location[1] - 0.035]),
                   lw=0.50, ec="k", fc=color, zorder=0)

pyplot.xlim(0.20, 3.80)
pyplot.ylim(0.00, 1.00)

pyplot.axis("off")

pyplot.savefig("./plot/4.pdf", format="pdf", pad_inches=0.02, bbox_inches="tight", dpi=300)
pyplot.close()
