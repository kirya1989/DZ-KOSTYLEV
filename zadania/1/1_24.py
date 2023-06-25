import unittest
import math
import numpy as np

class MyTestCase(unittest.TestCase):
    
    def test_solver(self):
        x1, x2 = solve_quadratic(1, 2, 1)
        tx1, tx2 = np.roots([1, 2, 1])

        self.assertAlmostEqual(x1, tx1, delta=1e-8)
        self.assertAlmostEqual(x2, tx2, delta=1e-8)


def solve_quadratic(a, b, c):
    # решает квадратное уравнение
    # ax^2 + bx + c = 0

    d = (b**2) - 4 * a * c

    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)

    return x1, x2

if __name__ == '__main__':
    unittest.main()