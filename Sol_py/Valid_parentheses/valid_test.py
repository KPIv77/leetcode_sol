import unittest
from valid_Sol import Solution

class TestValid(unittest.TestCase):
    
    def setUp(self):
        self.valid = Solution()
       
    def test_case1(self):
        self.assertEqual(self.valid.isValid("()"), True)

    def test_case2(self):       
        self.assertEqual(self.valid.isValid("()[]{}"), True)

    def test_case3(self):
        self.assertEqual(self.valid.isValid("(]"), False)

    def test_case4(self):
        self.assertEqual(self.valid.isValid("([])"), True)

    def test_case5(self):
        self.assertEqual(self.valid.isValid("([)]"), False)

    def test_case6(self):  
        self.assertEqual(self.valid.isValid("([)]]]]]][[)"), False)

    def test_case7(self):
        self.assertEqual(self.valid.isValid("]]][[["), False)

    def test_case8(self):
        self.assertEqual(self.valid.isValid("(]]][[[)"), False)

if __name__ == "__main__":
    unittest.main() 