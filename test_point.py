import unittest

from point import make_point_class


class TestMakePointClass(unittest.TestCase):
    def test_attributes(self):
        P = make_point_class(3)
        p = P(1, 2.5, -3)
        self.assertEqual(p.x0, 1)
        self.assertEqual(p.x1, 2.5)
        self.assertEqual(p.x2, -3)

    def test_to_tuple(self):
        P = make_point_class(4)
        self.assertEqual(P(1, 2, 3, 4).to_tuple(), (1, 2, 3, 4))

    def test_type_error(self):
        P = make_point_class(2)
        with self.assertRaises(TypeError):
            P(1, "not a number")
        p = P(0, 0)
        with self.assertRaises(TypeError):
            p.x0 = None

    def test_wrong_number_of_args(self):
        P = make_point_class(3)
        with self.assertRaises(TypeError):
            P(1, 2)
        with self.assertRaises(TypeError):
            P(1, 2, 3, 4)

    def test_cache(self):
        self.assertIs(make_point_class(5), make_point_class(5))

    def test_cache_normalizes_call_style(self):
        point_class = make_point_class(6)
        self.assertIs(point_class, make_point_class(n=6))
        self.assertIs(point_class, make_point_class(6, name=None))

    def test_invalid_dimension(self):
        for n in (0, -1):
            with self.subTest(n=n), self.assertRaises(ValueError):
                make_point_class(n)

        for n in (1.5, "3", True):
            with self.subTest(n=n), self.assertRaises(TypeError):
                make_point_class(n)


if __name__ == "__main__":
    unittest.main()
