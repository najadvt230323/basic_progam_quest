# unit testing
# ================

import unittest

from calculation import add

class Test(unittest.TestCase):
    
    def test_positive(self):
        self.assertEqual(add(20,5),25)
    
    def test_nagatve(self):
        self.assertEqual(add(-10,-20),-30)
    
# unittest.main()

# ------------------------------------------------
from calculation import rev,revint,revnevint,div

class Test1(unittest.TestCase):
    
    def test_revarse(self):
        self.assertEqual(rev("najad"),"dajan")
    
    def test_revarseint(self):
        self.assertEqual(revint(12),21)
    def test_revarsenevint(self):
        self.assertEqual(revnevint(-123),-321)
        self.assertEqual(revnevint(123),321)
    def test_divi(self):
        self.assertEqual(div(10,5),2)
        self.assertEqual(div(-10,2),-5)
        with self.assertRaises(ZeroDivisionError):
            div(10,0)



unittest.main()