import unittest
from distributed_median import Computer

class ComputerTestCase(unittest.TestCase):
    def setUp(self):
        self.computer = Computer([3, 2, 1, 4, 6], 1)

class SortNumsUponConstruction(ComputerTestCase):
    def runTest(self):
        self.assertEqual(self.computer.nums, [1, 2, 3, 4, 6])

if __name__ == '__main__':
    unittest.main()