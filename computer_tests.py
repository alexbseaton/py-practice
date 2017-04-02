import unittest
from distributed_median import Computer

class ComputerTestCase(unittest.TestCase):
    def setUp(self):
        self.computer = Computer([3, 2, 1, 4, 6], 1)

class SortNumsUponConstruction(ComputerTestCase):
    def runTest(self):
        self.assertEqual(self.computer.nums, [1, 2, 3, 4, 6])

    def test_report_smallest(self):
        self.assertEqual(self.computer.report_smallest(), (1, 1))

    def test_remove_smallest(self):
        computer = self.computer
        computer.remove_smallest()
        self.assertEqual(computer.nums[0], 2)
        self.assertEqual(len(computer.nums), 4)
        
if __name__ == '__main__':
    unittest.main()