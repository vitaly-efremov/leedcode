class SimpleSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        s_len = len(s)
        for i in range(s_len):
            if s_len - i <= max_len:
                break

            visited_chars = set()
            for j in range(i, s_len):
                char = s[j]
                if char in visited_chars:
                    break
                visited_chars.add(char)
            max_len = max(max_len, len(visited_chars))
        return max_len


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        s_len = len(s)
        start = 0
        while start < s_len:
            if s_len - start <= max_len:
                break

            visited_chars = dict()
            for end in range(start, s_len):
                char = s[end]
                if char in visited_chars:
                    start = visited_chars[char]
                    break
                visited_chars[char] = end
            max_len = max(max_len, len(visited_chars))
            start += 1
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        s_len = len(s)
        start = end = 0
        visited_chars = dict()
        while end < s_len:
            if s_len - start <= max_len:
                break

            char = s[end]
            if char in visited_chars:
                new_start = visited_chars[char]
                max_len = max(max_len, len(visited_chars))
                for i in range(start, new_start):
                    del visited_chars[s[i]]
                start = new_start + 1

            visited_chars[char] = end
            end += 1

        max_len = max(max_len, len(visited_chars))
        return max_len


if __name__ == '__main__':
    solution = Solution()
    assert solution.lengthOfLongestSubstring('abcabcbb') == 3
    assert solution.lengthOfLongestSubstring('bbbbb') == 1
    assert solution.lengthOfLongestSubstring('pwwkew') == 3
    assert solution.lengthOfLongestSubstring(' ') == 1

    print('All good!')
