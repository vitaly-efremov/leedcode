import math


class Solution:
    roman_letters_extended = (
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    )

    def intToRoman(self, num: int) -> str:
        roman_value = ''
        current_num = num
        for int_num, letter in self.roman_letters_extended:
            letters_count = current_num // int_num
            roman_value += letters_count * letter
            current_num = current_num % int_num

        return roman_value


if __name__ == '__main__':
    solution = Solution()
    assert solution.intToRoman(1) == 'I'
    assert solution.intToRoman(3) == 'III'
    assert solution.intToRoman(58) == 'LVIII'
    assert solution.intToRoman(1994) == 'MCMXCIV'
    print('All good!')
