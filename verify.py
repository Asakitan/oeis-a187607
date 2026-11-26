"""Check the rectangle formula by enumerating ordered triples on the board."""
from itertools import product

MOVES = tuple(product((-1, 2), repeat=2))


def direct(w, h):
    def inside(p):
        return 0 <= p[0] < w and 0 <= p[1] < h

    count = 0
    for x, y in product(range(w), range(h)):
        for dx, dy in MOVES:
            q = x + dx, y + dy
            if not inside(q):
                continue
            for ex, ey in MOVES:
                r = q[0] + ex, q[1] + ey
                if inside(r) and len({(x, y), q, r}) == 3:
                    count += 1
    return count


def axis(m):
    return 3 * max(0, m - 2) + max(0, m - 4)


if __name__ == "__main__":
    for w, h in product(range(1, 10), repeat=2):
        assert direct(w, h) == axis(w) * axis(h), (w, h)
    a = [0] + [direct(n, n) for n in range(1, 10)]
    numerator = [sum(c * a[n-i] for i, c in enumerate((1, -3, 3, -1))
                     if i <= n) for n in range(len(a))]
    assert numerator == [0, 0, 0, 9, 9, 19, -5, 0, 0, 0]
    print("81 rectangles checked; numerator = 9*x^3 + 9*x^4 + 19*x^5 - 5*x^6")
