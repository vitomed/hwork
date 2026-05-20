import collections
import unittest

# Requirements:
# Time complexity O(n)

def algorithm(nums, k: int):
    result = []
    buckets = [[] for _ in range(len(nums) + 1)]
    freq = collections.defaultdict(int)

    for n in nums:
        freq[n] += 1

    for num, fr_count in freq.items():
        buckets[fr_count].append(num)

    for i in range(len(buckets)-1, 0, -1):
        if not buckets[i]:
            continue

        result.extend(buckets[i])
        if len(result) == k:
            return result

    return None


# Time: O(n+n+f+n) = O(3n) -> O(n)
# Memory: O(n+n+r) = O(2n) -> O(n)



class MyTestCase(unittest.TestCase):
    def test_one(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        output = [1, 2]
        self.assertEqual(output, algorithm(nums, k))  # add assertion here

        nums = [1, 1, 1]
        k = 1
        output = [1]
        self.assertEqual(output, algorithm(nums, k))  # add assertion here


if __name__ == '__main__':
    unittest.main()
