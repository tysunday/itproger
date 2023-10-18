import unittest
import my_math

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(my_math.add(5,7), 12)
        self.assertEqual(my_math.add(5),9)
        self.assertEqual(my_math.add(), 5)

if __name__ == '__main__':
    unittest.main()