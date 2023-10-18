import pytest
import my_math

@pytest.mark.parametrize("num1, num2, result", [
    (5,5,10),
    ('Hello', 'World', 'HelloWorld')
])
@pytest.mark.add
def test_add(num1, num2, result):
    assert my_math.add(num1, num2) == result
    assert my_math.add() == 5
    assert my_math.add(3) == 7

def test_add():
    assert my_math.mult(4,5) == 20

@pytest.mark.add
def test_add_strings():
    result = my_math.add('Hello', 'World')
    assert result == 'HelloWorld'
    assert type(result) is str
    assert "Hello" in result

# import unittest
# import my_math
#
# class TestMath(unittest.TestCase):
#
#     def test_add(self):
#         self.assertEqual(my_math.add(5,7), 12)
#         self.assertEqual(my_math.add(5),9)
#         self.assertEqual(my_math.add(), 5)
#
# if __name__ == '__main__':
#     unittest.main()