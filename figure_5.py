"""
@Author      : Haoling Zhang
@Description : Figure 5
"""
from logging import getLogger, CRITICAL
from matplotlib import pyplot, rcParams
from numpy import linspace
from warnings import filterwarnings

filterwarnings("ignore")

getLogger("matplotlib").setLevel(CRITICAL)

rcParams["font.family"] = "Arial"
rcParams["mathtext.fontset"] = "custom"
rcParams["mathtext.rm"] = "Linux Libertine"
rcParams["mathtext.cal"] = "Lucida Calligraphy"
rcParams["mathtext.it"] = "Linux Libertine:italic"
rcParams["mathtext.bf"] = "Linux Libertine:bold"

alignments = ["CCSM.CGRAYTSETYLMKHMSK..H",
              "CEE..CGKAFSRSSSLTRHKRI..H",
              "CEE..CGKSYRLISLLNLHKKR..H",
              "CKE..CGKVISSSSSFAKHKRI..H",
              "CKM..CSSILKDILHLAEHDGT..H",
              "CKV..CGKPFHSLSPFRIHERT..H",
              "CLT..CGVAWADARSLKRHVRT..H",
              "CMVQGCLSVVKLESSIVRHYKRT.H",
              "CQE..CQEWVPDRESYVSHMKKS.H",
              "CAE..CGKGMKTKHALRHHMKL..H",
              "CFT..CCPPCLCPVDPRGHCPK..H",
              "CLR..CRFRCTDSTKVTAHRKH..H",
              "CLT..CGVAWADARSLKRHVRT..H",
              "CNWSYCGKRFTRSDELQRHKRT..H",
              "CPVPGCKKRYKNVNGIKYHAKNG.H",
              "CLL..CNRRIPENETLREHMKNK.H",
              "CYY..CGKTLSDRLEYQQHMLKV.H",
              "CLYNGCNKRIARKYNVESHIQT..H",
              "CTF..CKTEWDTVLITKDHEIDI.H",
              "CPNCGCIQELMGTIFDETHFYN..H",
              "CSL..CNYSCNQSMNLKRHMLR..H",
              "CTV..CRTQMPDPKTFKQHFESK.H",
              "CIH..CAKYMETAIALKTHLKGKVH",
              "CGT..CGKKVGSAARLQAHEAA..H"]

collection = ["C", "x", "x", "x", "x", "C", "x", "x", "x", "LIVMFYWC",
              "x", "x", "x", "x", "x", "x", "x", "x", "H", "x", "x", "x", "x", "x", "H"]

pattern = ["C", "x(2,4)", "C", "x(3)", "[LIVMFYWC]", "x(8)", "H", "x(3,5)", "H"]


if __name__ == "__main__":
    figure = pyplot.figure(figsize=(7.2, 3.0), tight_layout=True)

    x_locations = linspace(0.15, 0.95, 25)
    y_locations = linspace(0.10, 0.80, 24)[::-1]

    for x_index, x_location in enumerate(x_locations):
        for y_index, y_location in enumerate(y_locations):
            info = alignments[y_index][x_index]
            if info != ".":
                # noinspection PyTypeChecker
                pyplot.text(x_location, y_location, info, va="center", ha="center", fontsize=4.5)
            else:
                # noinspection PyTypeChecker
                pyplot.scatter([x_location], [y_location], s=0.5, color="k")

    for x_location in x_locations:
        pyplot.hlines([0.07, 0.84], x_location - 0.009, x_location + 0.009, color="k", lw=0.5, zorder=1)
        pyplot.fill_between([x_location - 0.009, x_location + 0.009], 0.07, 0.84,
                            ec="none", fc="#dfe0df", zorder=0)

    pyplot.text(0.55, 0.03, "multiple sequence alignment", va="center", ha="center", fontsize=5)

    labels = {"HUMAN": 9,
              "MOUSE": 5,
              "PONAB": 1,
              "CAEEL": 2,
              "SCHPO": 2,
              "ASFK5": 1,
              "RAT": 1,
              "CHICK": 1,
              "YEAST": 1,
              "BOVIN": 1}
    start, positions = 0, linspace(0.09, 0.03, 5)
    for label, count in labels.items():
        if count > 1:
            upper, lower = y_locations[start], y_locations[start + count - 1]
            pyplot.plot([0.13, 0.12, 0.12, 0.13], [upper, upper, lower, lower], color="k", lw=0.5)
            pyplot.hlines((upper + lower) / 2.0, 0.11, 0.12, color="k", lw=0.5)
            for info, location in zip(label[::-1], positions):
                # noinspection PyTypeChecker
                pyplot.text(location, (upper + lower) / 2.0, info, va="center", ha="center", fontsize=5)
        else:
            pyplot.hlines(y_locations[start], 0.11, 0.13, color="k", lw=0.5)
            for info, location in zip(label[::-1], positions):
                # noinspection PyTypeChecker
                pyplot.text(location, y_locations[start], info, va="center", ha="center", fontsize=5)
        start += count

    pyplot.plot([0.55, 0.55, 1.45], [0.86, 0.90, 0.90], lw=0.5, color="k")
    pyplot.annotate("", xy=(1.45, 0.90), xytext=(1.45, 0.86),
                    arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.5, mutation_scale=5))
    pyplot.text(1.00, 0.93, "expert annotation", va="center", ha="center", fontsize=5)

    for x_location in x_locations + 0.9:
        pyplot.hlines(0.84, x_location - 0.009, x_location + 0.009, color="k", lw=0.5, zorder=1)
        pyplot.hlines(y_locations[7] - 0.03, x_location - 0.009, x_location + 0.009, color="k", lw=0.5, zorder=1)
    for label, x_location in zip(collection, x_locations + 0.9):
        if len(label) == 1:
            y_location = (y_locations[0] + y_locations[7]) / 2.0
            if label == "x":
                # noinspection PyTypeChecker
                pyplot.text(x_location, y_location, label, va="center", ha="center", fontsize=4.5, zorder=1)
                pyplot.fill_between([x_location - 0.009, x_location + 0.009], y_locations[7] - 0.03, 0.84,
                                    ec="none", fc="#fff8f0", zorder=0)
            else:
                # noinspection PyTypeChecker
                pyplot.text(x_location, y_location, label, va="center", ha="center", color="w", fontsize=4.5, zorder=1)
                pyplot.fill_between([x_location - 0.009, x_location + 0.009], y_locations[7] - 0.03, 0.84,
                                    ec="none", fc="#ae8a68", zorder=0)
        else:
            for info, y_location in zip(label, y_locations):
                pyplot.text(x_location, y_location, info, va="center", ha="center", fontsize=4.5)
            pyplot.fill_between([x_location - 0.0085, x_location + 0.0085], y_locations[7] - 0.03, 0.84,
                                ec="none", fc="#F9A345", zorder=0)

    x_locations += 0.9
    for index, info in zip([0, 5, 9, 18, 24], ["C", "C", "[LIVMFYWC]", "H", "H"]):
        pyplot.annotate("", xy=(x_locations[index], 0.52), xytext=(x_locations[index], 0.46),
                        arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.5, mutation_scale=5))
        pyplot.text(x_locations[index], 0.44, info, va="center", ha="center", fontsize=4.5)

    for (former, latter), info in zip([[1, 4], [6, 8], [10, 17], [19, 23]], ["x(2,4)", "x(3)", "x(8)", "x(3,5)"]):
        pyplot.plot([x_locations[former], x_locations[former], x_locations[latter], x_locations[latter]],
                    [0.52, 0.49, 0.49, 0.52], color="k", lw=0.5, zorder=1)
        pyplot.fill_between([x_locations[former], x_locations[latter]], 0.49, 0.52, ec="none", fc="#EEEEEE",
                            zorder=0)
        value = (x_locations[former] + x_locations[latter]) / 2.0
        pyplot.annotate("", xy=(value, 0.49), xytext=(value, 0.39),
                        arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.5, mutation_scale=5))
        pyplot.text(value, 0.37, info, va="center", ha="center", fontsize=4.5)
    pyplot.plot([x_locations[0], x_locations[0], x_locations[24], x_locations[24]],
                [0.32, 0.28, 0.28, 0.32], color="k", lw=0.5, zorder=1)
    value = (x_locations[1] + x_locations[24]) / 2.0
    # noinspection PyTypeChecker
    pyplot.annotate("", xy=(value, 0.28), xytext=(value, 0.22),
                    arrowprops=dict(arrowstyle="<|-", color="k", shrinkA=0, shrinkB=0, lw=0.5, mutation_scale=5))
    # noinspection PyTypeChecker
    pyplot.text(value, 0.16, "-".join(pattern), va="center", ha="center",
                bbox=dict(fc="w", ec="k", lw=0.50, boxstyle="round,pad=0.5"), fontsize=6)

    # noinspection PyTypeChecker
    pyplot.text(value, 0.03, "regular expression at the motif level", va="center", ha="center", fontsize=5)
    pyplot.xlim(0.00, 1.90)
    pyplot.ylim(0.00, 0.96)
    pyplot.axis("off")

    pyplot.savefig("./plot/5.pdf", format="pdf", pad_inches=0.02, bbox_inches="tight", dpi=300)
    pyplot.close()
