import unittest
from main import attr

class testTask_1(unittest.TestCase):
    attr = attr
    
    def test_stock_info_attr(self):
        self.assertEqual(self.attr, ('company', 'country', 'price', 'currency'))
        
if __name__ == '__main__':
    unittest.main()