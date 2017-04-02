""" Find the median of some numbers """

nums_per_pc = 3

class Computer:
    def __init__(self, nums):
        assert len(nums) == nums_per_pc
        self.nums = sorted(nums)

    def report_smallest(self):
        return self.nums[0]

    def remove_smallest(self):
        self.nums.pop(0)

def find_smallest(pcs):
    """ Takes a list of Computers and returns a tuple (int smallest, Computer pc) s.th smallest is
    the least number held in pcs and pc is the Computer that holds smallest. """
    pc_with_least_num = pcs[0]
    smallest = pcs[0].report_smallest()
    for pc in pcs:
        if pc.report_smallest() < smallest:
            smallest = pc.report_smallest()
            pc_with_least_num = pc
    return smallest, pc_with_least_num

def run(pcs):
    """ Work out the median of the numbers assuming that there's an even amount of numbers altogether. """

    # The locations of the smaller of the two numbers used to calculate the median
    lower_target = int(nums_per_pc * len(pcs) / 2)

    # Record of the smallest number left in the pcs
    # Defaults to the smallest in the first pc to start with
    smallest = pcs[0].report_smallest()
    # How many numbers have we heard about so far?
    for _ in range(lower_target):
        smallest, pc_with_least_num = find_smallest(pcs)
        # Remove the small number from the PC holding it
        pc_with_least_num.remove_smallest()
        # if that pc is empty, remove it from the list
        if not pc_with_least_num.nums:
            pcs.remove(pc_with_least_num)

    # print("Number reported: {}".format(num_reported))
    # print("Number currently on: {}".format(smallest))

    second_smallest, _  = find_smallest(pcs)

    median = (smallest + second_smallest) / 2
    print("The median is: {}".format(median))
    return median

if __name__ == '__main__':
    assert run([Computer([5, 3, 2]), Computer([1, 6, 7])]) == 4.0
    assert run([Computer([1, 1, 1]), Computer([2, 2, 2])]) == 1.5
    assert run([Computer([-1, -2, -5]), Computer([-6, -4, -3])]) == -3.5 # wow wasn't expecting this one to work
