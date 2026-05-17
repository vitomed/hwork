import unittest

def contains_duplicate(nums: list[int]) -> bool:
    storage = set()
    for num in nums:
        if num in storage:
            return True
        storage.add(num)
    return False

class MyTestCase(unittest.TestCase):
    def test_one(self):
        nums = [1, 2, 3, 1]
        self.assertEqual(True, contains_duplicate(nums))  # add assertion here

    def test_two(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(False, contains_duplicate(nums))  # add assertion here

    def test_three(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertEqual(True, contains_duplicate(nums))  # add assertion here


if __name__ == '__main__':
    unittest.main()
