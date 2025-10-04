from matplotlib import axes, path, patches
from numpy import ndarray, array, linspace, random, sqrt, sin, cos, pi
from shapely import geometry
from typing import Tuple, Union


def capsule(ax: axes.Axes,
            xy: Tuple[float, float],
            width: float,
            height: float,
            lw: float,
            ec: str,
            fc: str,
            zorder: int,
            horizontal: bool = True):
    if horizontal:
        radius = height / 2.0
        body_length = width - 2.0 * radius

        if body_length < 0:
            raise ValueError("For a horizontal capsule shape, the width must be at least the height.")

        # left semicircle
        left = [(xy[0] + radius + radius * cos(theta), xy[1] + radius + radius * sin(theta))
                for theta in linspace(1.5 * pi, 0.5 * pi)]

        # top edge
        top = [(xy[0] + radius + body_length, xy[1] + height)]

        # right semicircle
        right = [(xy[0] + radius + body_length + radius * cos(theta), xy[1] + radius + radius * sin(theta))
                 for theta in linspace(0.5 * pi, -0.5 * pi)]

        # bottom edge
        bottom = [(xy[0] + radius, xy[1])]

        verts = left + top + right + bottom + [left[0]]

    else:  # vertical
        radius = width / 2.0
        body_height = height - 2.0 * radius

        # top semicircle
        top = [(xy[0] + radius + radius * cos(theta), xy[1] + body_height + radius + radius * sin(theta))
               for theta in linspace(pi, 0)]

        # right edge
        right = [(xy[0] + width, xy[1] + radius)]

        # bottom semicircle
        bottom = [(xy[0] + radius + radius * cos(theta), xy[1] + radius + radius * sin(theta))
                  for theta in linspace(0, -pi)]
        # left edge
        left = [(xy[0], xy[1] + body_height + radius)]

        verts = top + right + bottom + left + [top[0]]

    plot_shape(ax, array(verts), lw, ec, fc, zorder)

    # codes = [path.Path.MOVETO] + [path.Path.LINETO] * (len(verts) - 2) + [path.Path.CLOSEPOLY]
    #
    # # noinspection PyTypeChecker
    # ax.add_patch(patches.PathPatch(path.Path(verts, codes), ec=ec, fc=fc, lw=lw))


def closed_curve(ax: axes.Axes,
                 curve: ndarray,
                 xy: Tuple[float, float],
                 width: float,
                 height: float,
                 lw: float,
                 ec: str,
                 fc: str,
                 zorder: int):
    adjusted_curve = curve.copy()
    adjusted_curve[:, 0] *= width
    adjusted_curve[:, 1] *= height
    adjusted_curve[:, 0] += xy[0]
    adjusted_curve[:, 1] += xy[1]

    plot_shape(ax, adjusted_curve, lw, ec, fc, zorder)

    # codes = [path.Path.MOVETO] + [path.Path.LINETO] * (curve.shape[0] - 2) + [path.Path.CLOSEPOLY]
    #
    # # noinspection PyTypeChecker
    # ax.add_patch(patches.PathPatch(path.Path(adjusted_curve, codes), ec=ec, fc=fc, lw=lw))


def plot_shape(ax: axes.Axes,
               curve: ndarray,
               lw: float,
               ec: str,
               fc: str,
               zorder: int):
    codes = [path.Path.MOVETO] + [path.Path.LINETO] * (curve.shape[0] - 2) + [path.Path.CLOSEPOLY]

    # noinspection PyTypeChecker
    ax.add_patch(patches.PathPatch(path.Path(curve, codes), ec=ec, fc=fc, lw=lw, zorder=zorder))


def random_scatters_g(curve: ndarray,
                      xy: Tuple[float, float],
                      width: float,
                      height: float,
                      point_number: int,
                      minimum_distance: float,
                      random_seed: Union[int, None] = None) \
        -> ndarray:
    adjusted_curve = curve.copy()
    adjusted_curve[:, 0] *= width
    adjusted_curve[:, 1] *= height
    adjusted_curve[:, 0] += xy[0]
    adjusted_curve[:, 1] += xy[1]

    if random_seed is not None:
        random.seed(random_seed)

    polygon = geometry.Polygon(adjusted_curve.tolist())
    min_x, min_y, max_x, max_y = polygon.bounds

    points = []
    while len(points) < point_number:
        x, y = random.uniform(min_x, max_x), random.uniform(min_y, max_y)
        if polygon.contains(geometry.Point(x, y)):
            flag = True
            for srx, sry in points:
                if sqrt((srx - x) ** 2 + (sry - y) ** 2) < minimum_distance:
                    flag = False
            if flag:
                points.append([x, y])

    if random_seed is not None:
        random.seed()

    return array(points)


def random_scatters_li(curve: ndarray,
                       point_number: int,
                       minimum_distance: float,
                       random_seed: Union[int, None] = None) \
        -> ndarray:
    if random_seed is not None:
        random.seed(random_seed)

    polygon = geometry.Polygon(curve.tolist())
    min_x, min_y, max_x, max_y = polygon.bounds

    points = []
    while len(points) < point_number:
        x, y = random.uniform(min_x, max_x), random.uniform(min_y, max_y)
        if polygon.contains(geometry.Point(x, y)):
            flag = True
            for srx, sry in points:
                if sqrt((srx - x) ** 2 + (sry - y) ** 2) < minimum_distance:
                    flag = False
            if flag:
                points.append([x, y])

    if random_seed is not None:
        random.seed()

    return array(points)


def random_scatters_lo(minimum_x: float,
                       maximum_x: float,
                       minimum_y: float,
                       maximum_y: float,
                       curve: ndarray,
                       point_number: int,
                       minimum_distance: float,
                       other_points: Union[ndarray, list, None] = None,
                       random_seed: Union[int, None] = None) \
        -> ndarray:
    if random_seed is not None:
        random.seed(random_seed)

    polygon = geometry.Polygon(curve.tolist())

    points = []
    while len(points) < point_number:
        x, y = random.uniform(minimum_x, maximum_x), random.uniform(minimum_y, maximum_y)
        if not polygon.contains(geometry.Point(x, y)):
            flag = True
            if other_points is not None:
                for srx, sry in other_points:
                    if sqrt((srx - x) ** 2 + (sry - y) ** 2) < minimum_distance:
                        flag = False
                        break
            if flag:
                for srx, sry in points:
                    if sqrt((srx - x) ** 2 + (sry - y) ** 2) < minimum_distance:
                        flag = False
                        break
            if flag:
                points.append([x, y])

    if random_seed is not None:
        random.seed()

    return array(points)


def random_scatters_b(minimum_x: float,
                      maximum_x: float,
                      minimum_y: float,
                      maximum_y: float,
                      point_number: int,
                      minimum_distance: float,
                      random_seed: Union[int, None] = None) \
        -> ndarray:
    points = []

    if random_seed is not None:
        random.seed(random_seed)

    while len(points) < point_number:
        x, y = random.uniform(minimum_x, maximum_x), random.uniform(minimum_y, maximum_y)
        flag = True
        for srx, sry in points:
            if sqrt((srx - x) ** 2 + (sry - y) ** 2) < minimum_distance:
                flag = False
        if flag:
            points.append([x, y])

    if random_seed is not None:
        random.seed()

    return array(points)
