import unittest
from main import Solution


class TestTask_3(unittest.TestCase):
    def test_update_counter(self):
        updated_counter = Solution.update_counter()
        
        from main import counter
        self.assertEqual(counter, updated_counter)
        
if __name__ == "__main__":
    unittest.main()