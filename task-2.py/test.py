import unittest
from main import Solution


class testTask_2(unittest.TestCase):
    docstring = Solution.sum_func_docstring()
    sum_li = Solution.sum_list()
    
    def test_sum_func_docstring(self):
        self.assertEqual(self.docstring, sum.__doc__)
        
    def test_sum_list(self):
        self.assertEqual(self.sum_li, 1)
        
if __name__ == "__main__":
    unittest.main()