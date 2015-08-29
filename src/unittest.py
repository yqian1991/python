# splitter.py
import unittest
 
def split(line, types=None, delimiter=None):
    """Splits a line of text and optionally performs type conversion.
    ...
    """
    fields = line.split(delimiter)
    if types:
        fields = [ ty(val) for ty,val in zip(types,fields) ]
    return fields
 
class TestSplitFunction(unittest.TestCase):
    def setUp(self):
        # Perform set up actions (if any)
        pass
    def tearDown(self):
        # Perform clean-up actions (if any)
        pass
    def testsimplestring(self):
        r = split('GOOG 100 490.50')
        self.assertEqual(r,['GOOG','100','490.50'])
    def testtypeconvert(self):
        r = split('GOOG 100 490.50',[str, int, float])
        self.assertEqual(r,['GOOG', 100, 490.5])
    def testdelimiter(self):
        r = split('GOOG,100,490.50',delimiter=',')
        self.assertEqual(r,['GOOG','100','490.50'])
 
# Run the unittests
if __name__ == '__main__':
    unittest.main()