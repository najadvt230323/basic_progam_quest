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
from calculation import rev,revint,revnevint

class Test1(unittest.TestCase):
    
    def test_revarse(self):
        self.assertEqual(rev("najad"),"dajan")
    
    def test_revarseint(self):
        self.assertEqual(revint(12),21)
    def test_revarsenevint(self):
        self.assertEqual(revnevint(-123),-321)
        self.assertEqual(revnevint(123),321)

unittest.main()