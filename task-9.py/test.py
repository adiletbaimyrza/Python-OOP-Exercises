import unittest
from main import Solution


class testTask_9(unittest.TestCase):
    def test_stick_one(self):
        self.assertEqual('sport#summer', Solution.stick('sport', 'summer'))
    
    def test_stick_two(self):
        self.assertEqual('', Solution.stick(3, 5, 7))
    
    def test_stick_three(self):
        self.assertEqual('time#workout#gym', Solution.stick(False, 'time', True, 'workout', [], 'gym'))


if __name__ == "__main__":
    unittest.main()