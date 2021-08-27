import unittest
from calculator_functions import add
from calculator_functions import sub
from calculator_functions import mul
from calculator_functions import div


class CalculateUnitTest(unittest.TestCase):
    def test_add_result(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(2777777, 5000000), 2777777 + 5000000)

    def test_add_result_type(self):
        self.assertIsInstance(add(2, 3), int)
        self.assertIsInstance(add(-2, -3), int)
        self.assertIsInstance(add(-2, 3), int)
        self.assertIsInstance(add(2777777, 5000000), int)

    def test_add_non_int_type(self):
        with self.assertRaises(TypeError):
            add(2, "d")

    def test_sub_result(self):
        self.assertEqual(sub(2, 3), -1)
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(-2, 3), -5)
        self.assertEqual(sub(500000, 300000), 500000 - 300000)

    def test_sub_result_type(self):
        self.assertIsInstance(sub(2, 3), int)
        self.assertIsInstance(sub(5, 3), int)
        self.assertIsInstance(sub(-2, 3), int)
        self.assertIsInstance(sub(500000, 300000), int)

    def test_sub_non_int_type(self):
        with self.assertRaises(TypeError):
            sub(2, "d")

    def test_mul_result(self):
        self.assertEqual(mul(3, 3), 9)
        self.assertEqual(mul(5, 3), 15)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(500000, 300000), 500000 * 300000)

    def test_mul_result_type(self):
        self.assertIsInstance(mul(2, 3), int)
        self.assertIsInstance(mul(5, 3), int)
        self.assertIsInstance(mul(-2, 3), int)
        self.assertIsInstance(mul(500000, 300000), int)

    def test_mul_non_int_type(self):
        with self.assertRaises(TypeError):
            mul(2, "d")

    def test_div_int_result(self):
        self.assertEqual(div(3, 3), 1)
        self.assertEqual(div(9, 3), 3)
        self.assertEqual(div(-12, 3), -4)
        self.assertEqual(div(300000, 300000), 300000 / 300000)

    def test_div_result_int_type(self):
        self.assertIsInstance(div(3, 3), int)
        self.assertIsInstance(div(5, 3), int)
        self.assertIsInstance(div(-2, 3), int)
        self.assertIsInstance(div(300000, 300000), int)

    def test_div_float_result(self):
        self.assertEqual(div(3, 3), 1.0)
        self.assertEqual(div(9, 3), 3.0)
        self.assertEqual(div(-12, 3), -4.0)
        self.assertEqual(div(300000, 300000), 300000 / 300000)

    def test_div_float_type(self):
        self.assertIsInstance(div(3.8, 2), float)
        self.assertIsInstance(div(5.4, 3), float)
        self.assertIsInstance(div(-2.056, 3), float)
        self.assertIsInstance(div(300000.90, 300000), float)

    def test_div_str_type(self):
        with self.assertRaises(TypeError):
            div(2, "d")

    def test_div_for_zero(self):
        with self.assertRaises(ArithmeticError):
            div(9, 0)


if __name__ == '__main__':
    unittest.main()
