import unittest
from Roman_to_Integer import Solution

class TestRomeTointeger(unittest.TestCase):
    
    def setUp(self):
        self.rometoint = Solution()
    
    def test_romanToInt(self):
        self.assertAlmostEqual(self.rometoint.romanToInt("X"), 10)
        self.assertAlmostEqual(self.rometoint.romanToInt("XX"), 20)
        self.assertAlmostEqual(self.rometoint.romanToInt("III"), 3)
        self.assertAlmostEqual(self.rometoint.romanToInt("LVIII"), 58)
        self.assertAlmostEqual(self.rometoint.romanToInt("MCMXCIV"), 1994)
        self.assertAlmostEqual(self.rometoint.romanToInt("XCVI"), 96)
        
if __name__ == '__main__':
    unittest.main()
    
  