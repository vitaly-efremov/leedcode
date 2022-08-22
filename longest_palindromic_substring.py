class SimpleSolution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest_palindrome = ''
        for start_index in range(n):
            longest_palindrome_len = len(longest_palindrome)
            current_sub_string = ''
            if n - start_index <= longest_palindrome_len:
                break

            for end_index in range(start_index, n):
                current_sub_string += s[end_index]
                if self._is_palindrome(current_sub_string) and len(current_sub_string) > longest_palindrome_len:
                    longest_palindrome = current_sub_string
        return longest_palindrome

    def _is_palindrome(self, value: str) -> bool:
        start = 0
        end = len(value) - 1
        while start <= end:
            if value[start] != value[end]:
                return False
            start += 1
            end += -1
        return True


class TableSolution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        palindrome_table = self._init_palindrome_table(s)
        word_start = 0
        max_len = 1
        for substring_len in range(2, n + 1):
            for start_index in range(n - substring_len + 1):
                end_index = start_index + substring_len - 1
                current_len = end_index - start_index
                if s[start_index] == s[end_index] and (current_len == 1 or palindrome_table[start_index + 1][end_index - 1]):
                    palindrome_table[start_index][end_index] = True
                    if max_len - 1 < end_index - start_index:
                        word_start = start_index
                        max_len = end_index - start_index + 1
        longest_palindrome = s[word_start: word_start + max_len]
        return longest_palindrome

    def _init_palindrome_table(self, s: str) -> list:
        n = len(s)
        table = [[None] * n for _ in range(n)]
        for i in range(n):
            table[i][i] = True

        for i in range(n - 1):
            table[i][i + 1] = s[i] == s[i+1]

        return table


class MedianSolution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        best_palindrome = s[0]
        for middle in range(0, n - 1):
            if 2 * (n - middle) <= len(best_palindrome):
                break

            best_palindrome = self._get_biggest_word(
                self._get_biggest_palindrome(s, middle, middle),
                self._get_biggest_palindrome(s, middle, middle + 1),
                best_palindrome,
            )
        return best_palindrome

    def _get_biggest_palindrome(self, s, start, end) -> str:
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start+1:end]

    def _get_biggest_word(self, *words):
        return sorted(words, key=len)[-1]


if __name__ == '__main__':
    solution = MedianSolution()
    assert solution.longestPalindrome('aba') == 'aba'
    assert solution.longestPalindrome('bbbbb') == 'bbbbb'
    assert solution.longestPalindrome('babad') == 'bab'
    assert solution.longestPalindrome('cbbd') == 'bb'
    assert solution.longestPalindrome('c') == 'c'
    assert solution.longestPalindrome('bb') == 'bb'

    print('All good!')
