import unittest
from main import Solution


class testTask_4(unittest.TestCase):
    def test_update_counters(self):
        for _ in range(40):
            Solution.update_counters()
        
        from main import counter, dot_counter
        self.assertEqual(40, counter)
        self.assertEqual('........................................', dot_counter)
        
if __name__ == "__main__":
    unittest.main()