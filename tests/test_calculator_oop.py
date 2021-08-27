import unittest
from calculator_oop import Calculator


class calculatorOopTest(unittest.TestCase):

    def test_add_result(self):
        self.assertEqual(Calculator.add(2, 3), 5)

    def test_add_result(self):
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-2, -3), -5)
        self.assertEqual(Calculator.add(-2, 3), 1)
        self.assertEqual(Calculator.add(2777777, 5000000), 2777777 + 5000000)

    def test_add_result_type(self):
        self.assertIsInstance(Calculator.add(2, 3), int)
        self.assertIsInstance(Calculator.add(-2, -3), int)
        self.assertIsInstance(Calculator.add(-2, 3), int)
        self.assertIsInstance(Calculator.add(2777777, 5000000), int)

    def test_add_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.add(2, "d")

    def test_sub_result(self):
        self.assertEqual(Calculator.sub(2, 3), -1)
        self.assertEqual(Calculator.sub(5, 3), 2)
        self.assertEqual(Calculator.sub(-2, 3), -5)
        self.assertEqual(Calculator.sub(500000, 300000), 500000 - 300000)

    def test_sub_result_type(self):
        self.assertIsInstance(Calculator.sub(2, 3), int)
        self.assertIsInstance(Calculator.sub(5, 3), int)
        self.assertIsInstance(Calculator.sub(-2, 3), int)
        self.assertIsInstance(Calculator.sub(500000, 300000), int)

    def test_sub_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.sub(2, "d")

    def test_mul_result(self):
        self.assertEqual(Calculator.mul(3, 3), 9)
        self.assertEqual(Calculator.mul(5, 3), 15)
        self.assertEqual(Calculator.mul(-2, 3), -6)
        self.assertEqual(Calculator.mul(500000, 300000), 500000 * 300000)

    def test_mul_result_type(self):
        self.assertIsInstance(Calculator.mul(2, 3), int)
        self.assertIsInstance(Calculator.mul(5, 3), int)
        self.assertIsInstance(Calculator.mul(-2, 3), int)
        self.assertIsInstance(Calculator.mul(500000, 300000), int)

    def test_mul_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.mul(2, "d")

    def test_div_int_result(self):
        self.assertEqual(Calculator.div(3, 3), 1)
        self.assertEqual(Calculator.div(9, 3), 3)
        self.assertEqual(Calculator.div(-12, 3), -4)
        self.assertEqual(Calculator.div(300000, 300000), 300000 / 300000)

    def test_div_result_int_type(self):
        self.assertIsInstance(Calculator.div(3, 3), int)
        self.assertIsInstance(Calculator.div(5, 3), int)
        self.assertIsInstance(Calculator.div(-2, 3), int)
        self.assertIsInstance(Calculator.div(300000, 300000), int)

    def test_div_float_result(self):
        self.assertEqual(Calculator.div(3, 3), 1.0)
        self.assertEqual(Calculator.div(9, 3), 3.0)
        self.assertEqual(Calculator.div(-12, 3), -4.0)
        self.assertEqual(Calculator.div(300000, 300000), 300000 / 300000)

    def test_div_float_type(self):
        self.assertIsInstance(Calculator.div(3.8, 2), float)
        self.assertIsInstance(Calculator.div(5.4, 3), float)
        self.assertIsInstance(Calculator.div(-2.056, 3), float)
        self.assertIsInstance(Calculator.div(300000.90, 300000), float)

    def test_div_str_type(self):
        with self.assertRaises(TypeError):
            Calculator.div(2, "d")




if __name__ == '__main__':
    unittest.main()
