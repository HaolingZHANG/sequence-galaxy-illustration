"""
@Author      : Haoling Zhang
@Description : Figure 2
"""
from logging import getLogger, CRITICAL
from matplotlib import pyplot, rcParams
from numpy import array, linspace, cos, pi
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

pyplot.subplot(1, 2, 1)
pyplot.text(0.40, 1.50, "function-presence\nanchor", ha="center", va="center", fontsize=5)
pyplot.text(0.40, 0.50, "function-absence\nanchor", ha="center", va="center", fontsize=5)

pyplot.fill_between([0.80, 2.00], 1.20, 1.80, color="#FFF7F3", zorder=0)
pyplot.plot(linspace(0.95, 1.25, 31),
            1.50 + cos(linspace(0, 3 * pi, 31) - 1.00) * 0.05,
            color="#AAAAAA", lw=0.75, zorder=2)
pyplot.plot(linspace(0.95, 1.25, 31),
            1.50 - cos(linspace(0, 3 * pi, 31)) * 0.05,
            color="#AAAAAA", lw=0.75, zorder=2)
for location, (x_point, y_point_1, y_point_2) in enumerate(zip(linspace(0.95, 1.25, 31),
                                                               cos(linspace(0, 3 * pi, 31) - 1.00) * 0.05,
                                                               cos(linspace(0, 3 * pi, 31)) * 0.05)):
    if location % 2 == 1:
        pyplot.vlines(x_point, 1.50 + y_point_1, 1.50 - y_point_2, lw=0.75, color="#AAAAAA", zorder=1)
pyplot.plot(linspace(1.25, 1.55, 31),
            1.50 + cos(linspace(pi, 4 * pi, 31) - 1.00) * 0.05,
            color="#000000", lw=0.75, zorder=3)
pyplot.plot(linspace(1.25, 1.55, 31),
            1.50 - cos(linspace(pi, 4 * pi, 31)) * 0.05,
            color="#000000", lw=0.75, zorder=3)
for location, (x_point, y_point_1, y_point_2) in enumerate(zip(linspace(1.25, 1.55, 31),
                                                               cos(linspace(pi, 4 * pi, 31) - 1.00) * 0.05,
                                                               cos(linspace(pi, 4 * pi, 31)) * 0.05)):
    if location % 2 == 1:
        pyplot.vlines(x_point, 1.50 + y_point_1, 1.50 - y_point_2, lw=0.75, color="#000000", zorder=3)
pyplot.plot(linspace(1.55, 1.85, 31),
            1.50 + cos(linspace(0, 3 * pi, 31) - 1.00) * 0.05,
            color="#AAAAAA", lw=0.75, zorder=2)
pyplot.plot(linspace(1.55, 1.85, 31),
            1.50 - cos(linspace(0, 3 * pi, 31)) * 0.05,
            color="#AAAAAA", lw=0.75, zorder=2)
for location, (x_point, y_point_1, y_point_2) in enumerate(zip(linspace(1.55, 1.85, 31),
                                                               cos(linspace(0, 3 * pi, 31) - 1.00) * 0.05,
                                                               cos(linspace(0, 3 * pi, 31)) * 0.05)):
    if location % 2 == 1:
        pyplot.vlines(x_point, 1.50 + y_point_1, 1.50 - y_point_2, lw=0.75, color="#AAAAAA", zorder=1)

pyplot.text(1.40, 1.61, "wild-type sequence", ha="center", va="center", fontsize=4)
pyplot.text(1.40, 1.85, "whole gene", ha="center", va="center", fontsize=4)
pyplot.plot([0.95, 0.95, 1.20], [1.68, 1.85, 1.85], lw=0.50, ls=":", color="#000000", zorder=4)
pyplot.plot([1.85, 1.85, 1.60], [1.68, 1.85, 1.85], lw=0.50, ls=":", color="#000000", zorder=4)
pyplot.vlines([0.95, 1.85], 1.60, 1.68, lw=0.50, color="k", zorder=4)

pyplot.vlines([0.95, 1.25, 1.55, 1.85], 1.40, 1.32, lw=0.50, color="k", zorder=4)
pyplot.plot([0.95, 1.10], [1.32, 0.68], lw=0.50, ls=":", color="#000000")
pyplot.plot([1.25, 1.40], [1.32, 0.68], lw=0.50, ls=":", color="#000000")
pyplot.plot([1.55, 1.40], [1.32, 0.68], lw=0.50, ls=":", color="#000000")
pyplot.plot([1.85, 1.70], [1.32, 0.68], lw=0.50, ls=":", color="#000000")
pyplot.vlines([1.10, 1.40, 1.70], 0.60, 0.68, lw=0.50, color="k", zorder=4)

pyplot.fill_between([0.80, 2.00], 0.20, 0.80, color="#FFF7F3")
pyplot.plot(linspace(1.10, 1.70, 61),
            0.50 + cos(linspace(0, 6 * pi, 61) - 1.00) * 0.05,
            color="#AAAAAA", lw=0.75, zorder=2)
pyplot.plot(linspace(1.10, 1.70, 61),
            0.50 - cos(linspace(0, 6 * pi, 61)) * 0.05,
            color="#AAAAAA", lw=0.75, zorder=2)
for location, (x_point, y_point_1, y_point_2) in enumerate(zip(linspace(1.10, 1.70, 61),
                                                               cos(linspace(0, 6 * pi, 61) - 1.00) * 0.05,
                                                               cos(linspace(0, 6 * pi, 61)) * 0.05)):
    if location % 2 == 1:
        pyplot.vlines(x_point, 0.50 + y_point_1, 0.50 - y_point_2, lw=0.75, color="#AAAAAA")

pyplot.vlines(1.40, 0.32, 0.40, lw=0.50, color="k", zorder=4)
pyplot.text(1.40, 0.25, "knocked out", ha="center", va="center", fontsize=4)

pyplot.annotate("", xy=(2.10, 1.50), xytext=(2.45, 1.50),
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.50))
pyplot.annotate("", xy=(2.10, 0.50), xytext=(2.45, 0.50),
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.50))
pyplot.vlines(2.70, 0.65, 1.35, color="k", lw=0.5, ls="--", zorder=0)
pyplot.text(2.70, 1.50, "phenotype 1", ha="center", va="center", fontsize=5)
pyplot.text(2.70, 0.50, "phenotype 2", ha="center", va="center", fontsize=5)
pyplot.text(2.70, 1.00, "difference(s) can be\nconsistently observed",
            bbox=dict(fc="w", ec="w", boxstyle="round,pad=0.4"), color="#C00000", ha="center", va="center", fontsize=5)

pyplot.xlim(0.00, 3.10)
pyplot.ylim(0.05, 1.95)
pyplot.axis("off")

pyplot.subplot(1, 2, 2)

pyplot.text(0.30, 1.00, "investigated\nvariant", ha="center", va="center", fontsize=5)

pyplot.fill_between([0.60, 1.80], 0.70, 1.30, color="#FFF7F3")

pyplot.plot(linspace(0.75, 1.05, 31),
            1.00 + cos(linspace(0, 3 * pi, 31) - 1.00) * 0.05,
            color="#AAAAAA", lw=0.75, zorder=2)
pyplot.plot(linspace(0.75, 1.05, 31),
            1.00 - cos(linspace(0, 3 * pi, 31)) * 0.05,
            color="#AAAAAA", lw=0.75, zorder=2)
for location, (x_point, y_point_1, y_point_2) in enumerate(zip(linspace(0.75, 1.05, 31),
                                                               cos(linspace(0, 3 * pi, 31) - 1.00) * 0.05,
                                                               cos(linspace(0, 3 * pi, 31)) * 0.05)):
    if location % 2 == 1:
        pyplot.vlines(x_point, 1.00 + y_point_1, 1.00 - y_point_2, lw=0.75, color="#AAAAAA", zorder=1)
pyplot.plot(linspace(1.05, 1.35, 31),
            1.00 + cos(linspace(pi, 4 * pi, 31) - 1.00) * 0.05,
            color="#000000", lw=0.75, zorder=3)
pyplot.plot(linspace(1.05, 1.35, 31),
            1.00 - cos(linspace(pi, 4 * pi, 31)) * 0.05,
            color="#000000", lw=0.75, zorder=3)
nucleotide_indices = []
for location, (x_point, y_point_1, y_point_2) in enumerate(zip(linspace(1.05, 1.35, 31),
                                                               cos(linspace(pi, 4 * pi, 31) - 1.00) * 0.05,
                                                               cos(linspace(pi, 4 * pi, 31)) * 0.05)):
    if location % 2 == 1:
        nucleotide_indices.append(location)
        pyplot.vlines(x_point, 1.00 + y_point_1, 1.00 - y_point_2, lw=0.75, color="#000000", zorder=3)
pyplot.plot(linspace(1.35, 1.65, 31),
            1.00 + cos(linspace(0, 3 * pi, 31) - 1.00) * 0.05,
            color="#AAAAAA", lw=0.75, zorder=2)
pyplot.plot(linspace(1.35, 1.65, 31),
            1.00 - cos(linspace(0, 3 * pi, 31)) * 0.05,
            color="#AAAAAA", lw=0.75, zorder=2)
for location, (x_point, y_point_1, y_point_2) in enumerate(zip(linspace(1.35, 1.65, 31),
                                                               cos(linspace(0, 3 * pi, 31) - 1.00) * 0.05,
                                                               cos(linspace(0, 3 * pi, 31)) * 0.05)):
    if location % 2 == 1:
        pyplot.vlines(x_point, 1.00 + y_point_1, 1.00 - y_point_2, lw=0.75, color="#AAAAAA", zorder=1)

x_points = linspace(1.05, 1.35, 31)
y_points_1 = cos(linspace(pi, 4 * pi, 31) - 1.00) * 0.05
y_points_2 = cos(linspace(pi, 4 * pi, 31)) * 0.05
for index in [1, 13, 25]:
    pyplot.vlines(x_points[index], 1.00 + y_points_1[index], 1.00 - y_points_2[index],
                  color="#C00000", lw=0.75, zorder=4)
    pyplot.plot(x_points[index - 1: index + 2], 1.00 + y_points_1[index - 1: index + 2],
                color="#C00000", lw=0.75, zorder=4)
    pyplot.plot(x_points[index - 1: index + 2], 1.00 - y_points_2[index - 1: index + 2],
                color="#C00000", lw=0.75, zorder=4)

pyplot.text(1.20, 1.15, "variant of the\nwild-type sequence", ha="center", va="center", fontsize=4)
for index, (location, label) in enumerate(zip(x_points[array([1, 13, 25])], ["1st", "2nd", "3rd"])):
    pyplot.vlines(location, 0.90, 0.82, lw=0.50, color="k", zorder=4)
    pyplot.text(location, 0.75, label, ha="center", va="center", fontsize=4)
pyplot.text(x_points[-1] + 0.02, 0.75, "variant site", ha="left", va="center", fontsize=4)

pyplot.annotate("", xy=(1.40, 1.40), xytext=(1.60, 1.70),
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.50))
pyplot.annotate("", xy=(1.40, 0.60), xytext=(1.60, 0.30),
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.50))
pyplot.text(1.90, 1.70, "phenotype 1", ha="center", va="center", fontsize=5)
pyplot.text(1.90, 0.30, "phenotype 2", ha="center", va="center", fontsize=5)
pyplot.annotate("", xy=(2.20, 1.70), xytext=(2.40, 1.70),
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.50))
pyplot.annotate("", xy=(2.20, 0.30), xytext=(2.40, 0.30),
                arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.50))
pyplot.text(2.70, 1.70, "function\npresence", ha="center", va="center", fontsize=5)
pyplot.text(2.70, 0.30, "function\nabsence", ha="center", va="center", fontsize=5)
pyplot.vlines(2.70, 0.50, 1.50, color="k", lw=0.5, ls="--", zorder=0)
pyplot.text(2.70, 1.00, "boundary of the sequence space\ncan be roughly determined",
            bbox=dict(fc="w", ec="w", boxstyle="round,pad=0.4"), color="#C00000", ha="center", va="center", fontsize=5)
pyplot.xlim(0.10, 3.25)
pyplot.ylim(0.05, 1.95)
pyplot.axis("off")

figure.text(0.02, 0.98, "a", va="center", ha="center", fontsize=8)
figure.text(0.50, 0.98, "b", va="center", ha="center", fontsize=8)

pyplot.savefig("./plot/2.pdf", format="pdf", pad_inches=0.01, bbox_inches="tight", dpi=300)
pyplot.close()
