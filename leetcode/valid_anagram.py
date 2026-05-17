import unittest

def valid_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return  False

    store1 = {}
    store2 = {}
    for char in s1:
        store1[char] = store1.get(char, 0) + 1

    for char in s2:
        store2[char] = store2.get(char, 0) + 1

    return store1 == store2


class MyTestCase(unittest.TestCase):
    def test_one(self):
        s = "anagram"
        t = "nagaram"
        self.assertEqual(True, valid_anagram(s, t))  # add assertion here

    def test_two(self):
            s = "rat"
            t = "car"
            self.assertEqual(False, valid_anagram(s, t))  # add assertion here

    def test_three(self):
            s = "listen"
            t = "silent"
            self.assertEqual(True, valid_anagram(s, t))  # add assertion here


if __name__ == '__main__':
    unittest.main()
