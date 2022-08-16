from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters_count = Counter(s)
        return next((index for index, letter in enumerate(s) if letters_count[letter] == 1), -1)


if __name__ == '__main__':
    solution = Solution()
    assert solution.firstUniqChar('leetcode') == 0
    assert solution.firstUniqChar('loveleetcode') == 2
    assert solution.firstUniqChar('aabb') == -1

    print('All good!')
