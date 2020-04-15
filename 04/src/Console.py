import math

from typing import Tuple, Union


def solve(a: float, b: float, c: float) -> Union[Tuple[float, float], float]:
    d = b ** 2 - 4 * a * c

    return ((-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a),) \
        if (d > 0) else -b / (2 * a) if (d == 0) else None


if __name__ == '__main__':
    a = float(input('Enter a: '))
    b = float(input('Enter b: '))
    c = float(input('Enter c: '))

    print(f'{solve(a, b, c)}')
