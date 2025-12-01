import unittest
from long_gest import Solution


class TestLongGest(unittest.TestCase):
     
    def setUp(self):
        self.longfn = Solution()

    def test_case_word(self):
        self.assertEqual(self.longfn.longestCommonPrefix(["grow"]), "grow")
        
    def test_case_prefix_fl(self):
        self.assertEqual(self.longfn.longestCommonPrefix(["flower","flow","flight"]), "fl")
        
    def test_case_single(self):
        self.assertEqual(self.longfn.longestCommonPrefix(["a"]), "a")

    def test_case_prefix_c(self):
        self.assertEqual(self.longfn.longestCommonPrefix(["cat", "cow", "car"]), "c")

    
    def test_case_non_prefix(self):
        self.assertEqual(self.longfn.longestCommonPrefix(["sit", "game", "fast"]), "")



if __name__ == "__main__":
   unittest.main() 