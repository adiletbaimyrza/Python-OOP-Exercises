import unittest
from main import Solution


class TestTask_5(unittest.TestCase):
    def test_display_info(self):
        res = Solution.display_info(10)
        
        self.assertEqual(res, (110, '..........'))

if __name__ == "__main__":
    unittest.main()