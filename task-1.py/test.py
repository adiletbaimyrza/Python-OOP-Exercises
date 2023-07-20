import unittest
from main import Solution

class testTask_1(unittest.TestCase):
    attr = Solution.arg_names()
    
    def test_arg_names(self):
        self.assertEqual(self.attr, ('company', 'country', 'price', 'currency'))
        
if __name__ == '__main__':
    unittest.main()