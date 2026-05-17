import unittest
from collections import defaultdict

def group_anagram(s: list[str]) -> list[list[str]]:
    store = defaultdict(list)
    for word in s: # O(n) - n is number of words
        key = tuple(sorted(word)) # O(k) - k is max length of word
        store[key].append(word)
    return list(store.values())


# Memory is O(n*k)
# Time is O(n*k*log(k)) - k*log(k) is Time of quick sort - bubble sort time complexity is k


class MyTestCase(unittest.TestCase):
    def test_one(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertEqual(output, group_anagram(strs))  # add assertion here

    def test_two(self):
        strs = [""]
        output = [[""]]
        self.assertEqual(output, group_anagram(strs))  # add assertion here

    def test_three(self):
        strs = ["a"]
        output = [["a"]]
        self.assertEqual(output, group_anagram(strs))  # add assertion here


if __name__ == '__main__':
    unittest.main()
