from dataclasses import dataclass

import json
import math


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Line:
    begin: Point
    end: Point


@dataclass
class Size:
    width: float
    height: float


@dataclass
class Rect:
    top_left: Point
    size: Size


def quadrant(p: Point) -> int:
    if p.x >= 0 and p.y >= 0:
        return 1
    elif p.x < 0 and p.y < 0:
        return 3
    elif p.x < 0 and p.y > 0:
        return 2
    elif p.x > 0 and p.y < 0:
        return 4


def distance(p1: Point, p2: Point) -> float:
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def point_to_json(p: Point) -> str:
    return json.dumps({
        'x': p.x,
        'y': p.y,
    })


def rect_to_json(r: Rect) -> str:
    return json.dumps({
        'top_left': point_to_json(r.top_left),
        'size': "***"
    })


if __name__ == '__main__':
    point: Point = Point(-12.0, 34.89)
    q = quadrant(point)
    print(q)

    point_2 = Point(0.9, 11)
    print(distance(point, point_2))
    print(point_to_json(point_2))

    print(rect_to_json(Rect(point, Size(100, 10))))

