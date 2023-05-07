import unittest
from unittests.src.fixtures import *

# This method is used for not rewriting code

class TestEmployee(unittest.TestCase):

    # this setup method will run its code before every test cases
    @classmethod(cls)
    def setUpClass(cls):
        print('setUpClass')

    @classmethod(cls)
    def tearDown(cls):
        print('tearDownClass')
        
    def setUp(self):
        self.emp1 = Employee('Corey', 'Smith', 500000)
        self.emp2 = Employee('Sue', 'Baker', 60000)
        
    # this tearDown method will run after every single test executes
    @classmethod(cls)
    def tearDown():
        print('teardown\n')
    
    #test number 1
    def test_email(self):
        emp_1 = Employee('Corey', 'Smith', 500000)
        emp2 = Employee('Sue', 'Baker', 60000)

        self.assertEqual(emp_1.email, 'corey.smith@email.com')
        self.assertEqual(emp_2.email, 'sue.baker@email.com')
    
    #test number 2
    def test_fullname(self):
        self.assertEqual(emp_1.fullname, 'Corey Smith')
        self.assertEqual(emp_2.fullname, 'Sue Baker')

    def test_apply_raise(self):
        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63200)

if __name__ == '__main__':
    unittest.main()        
    