class Solution:
    roman_dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        string_iterator = iter(s)
        int_value = 0
        first_letter = next(string_iterator, None)
        second_letter = next(string_iterator, None)
        while first_letter:
            first_value = self.roman_dictionary[first_letter]
            second_value = second_letter and self.roman_dictionary[second_letter]
            if not second_value:
                int_value += first_value
                break

            if first_value < second_value:
                int_value += second_value - first_value
                first_letter = next(string_iterator, None)
            else:
                int_value += first_value
                first_letter = second_letter

            second_letter = next(string_iterator, None)

        return int_value


if __name__ == '__main__':
    solution = Solution()
    assert solution.romanToInt('') == 0
    assert solution.romanToInt('I') == 1
    assert solution.romanToInt('III') == 3
    assert solution.romanToInt('LVIII') == 58
    assert solution.romanToInt('MCMXCIV') == 1994
    print('All good!')
