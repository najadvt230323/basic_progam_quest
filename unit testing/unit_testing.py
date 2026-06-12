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
from calculation import rev,revint,revnevint,div,get_data

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

    def test_difrend(self):
        self.assertEqual(div(-10,2),-5)

        with self.assertRaises(ZeroDivisionError):
            div(10,0)

        self.assertNotEqual(div(-10,2),-4)

        self.assertTrue("PYTHON".isupper())
        self.assertTrue([True,1])
        self.assertTrue(1)
        self.assertTrue(True)

        self.assertAlmostEqual(20/3,6.7,places=1)
        self.assertAlmostEqual(20/3,6.67,places=2)
        self.assertAlmostEqual(20/3,6.667,places=3)
        self.assertAlmostEqual(20/3,6.6667,places=4)
        self.assertAlmostEqual(20/3,6.66667,places=5)
        self.assertAlmostEqual(20/3,6.666667,places=6)
        self.assertAlmostEqual(10/3,3.3,places=1)
        self.assertAlmostEqual(10/3,3.33,places=2)
        self.assertAlmostEqual(10/3,3.333,places=3)
        self.assertAlmostEqual(10/3,3.3333,places=4)

        self.assertFalse("PYTHOnn".isupper())

        f=["mango","apple"]
        self.assertIn("mango",f)

        self.assertIsNone(get_data())

        a=[1,2]
        b=a
        self.assertIs(a,b)

        # a=[1,2]
        # b=[1,2]
        # self.assertIs(a,b)
#output
# ======================================================================
# FAIL: test_difrend (__main__.Test1.test_difrend)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "c:\Users\NAJAD V T\Desktop\python full stak\python\unit testing\unit_testing.py", line 60, in test_difrend
#     self.assertIs(a,b)
#     ~~~~~~~~~~~~~^^^^^
# AssertionError: [1, 2] is not [1, 2]


    def test_isintatace(self):
        self.assertIsInstance("najad",str)
        self.assertIsInstance(123,int)
        self.assertIsInstance(True,bool)
        self.assertIsInstance(False,bool)
        self.assertIsInstance(1.255,float)





unittest.main()


# unittest.TestCase.assert
# unittest.