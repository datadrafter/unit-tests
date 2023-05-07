import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), "FOO")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = "test word"
        self.assertEqual(s.split(), ['test', 'word'])
        with self.assertRaises(TypeError):
            s.split(2)

    
if __name__ == '__main__':
    unittest.main()

"""
A test case is created by subclassing unittest.TestCase and three
individual test cases are then within.
Test cases funtion name should start with "test"

CLI interface for unittest module
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
"python -m unittest tests/test_something.py"
python -m unittest -v test_module
python -m unittest
-b, --buffer : Output is echoed
-c, --catch : control C during test run waits and outputs results so far
-f, --failfast : stop the test to run on the first error or failure
-k : only run test that matches a pattern
-v, --verbose : verbose output
-s, --start-directory : Directory to start discovery (.default)
-p, --pattern : Pattern that matches test files
-t, --top-level-directory : Top level directory to default start
"""
# SetUp - TearDown - Test functions 

"""
if setUp() succeded, tearDown() will run weather the test methods succeded or not
this working environment is called the test fixture
"""

# Most common test cases in unittest
"""
assertEqual(a,b) : a == b
assertNotEqual(a,b) : a != b
assertTrue(x) : bool(x) is True
assertFalse(x) : bool(x) is False
assertIs(a,b) : a is b
assertIsNot(a,b) : a is not b
assertIsNone(x) : x is None
assertIn(a,b) : a in b
assertNotIn(a,b) : a not in b
assertIsInstance : isinstance(a,b)
assertNotIsInstance(a,b) : not isinstance(a,b)

refer to documentation below for more details:
https://docs.python.org/3/library/unittest.html
"""

#Unit test for basic_unit_test_case.py
import calc
from basic_unittest_case import *

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        expected_output = calc.add(10,5)
        actual_output = add(10,5)
        
        self.assertEqual(expected_output,actual_output)
    
    def test_substract(self):
        expected_subs = calc.substract(10,5)
        actual_substract = substract(10,5)
        
        self.assertEqual(expected_subs, actual_substract)

    def test_divide(self):
        expected_divide = calc.divide(10,5)
        actual_divide = divide(10, 5)

        self.assertEqual(expected_divide, actual_divide)

    def test_multiply(self):
        expected_multiply = calc.multiply(10,5)
        actual_multiply = multiply(10,5)

        self.assertEqual(expected_multiply,actual_multiply)
    
if __name__ == '__main__':
    unittest.main()

#rather than doing the above way we can do this way too

class TestCalc2(unittest.TestCase):

    def test_calc(self):
        expected_addition = calc.add(10,5)
        expected_substraction = calc.substract(10,5)
        expected_division = calc.divide(10,5)
        expected_multiplication = calc.multiply(10,5)

        actual_addition = add(10,5)
        actual_substraction = substract(10,5)
        actual_division = divide(10,5)
        actual_multiplication = multiply(10,5)

        self.assertEquals(expected_addition, actual_addition)
        self.assertEquals(expected_substraction, actual_substraction)
        self.assertEquals(expected_division, actual_division)
        self.assertEquals(expected_multiplication, actual_multiplication)

        with self.assertRaises(ValueError): 
            calc.divide(10,0)
    
if __name__ == '__main__':
    unittest.main()


