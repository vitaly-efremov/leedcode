class CheatSolution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        str_x = str(x)
        if is_negative:
            str_x = str_x[1:]

        reversed_x = int(str_x[::-1])
        if is_negative:
            reversed_x *= -1
        if reversed_x <= -2 ** 31 and reversed_x > 2 ** 31:
            return 0
        return reversed_x


class Solution:
    MAX = 2 ** 31

    def reverse(self, x: int) -> int:
        result = 0
        num = abs(x)

        while num != 0:
            part = num % 10
            if (self.MAX - part) / 10 <= result:
                return 0

            result = result*10 + part
            num //= 10

        return -result if x < 0 else result


if __name__ == '__main__':
    solution = Solution()
    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(1563847412) == 0

    print('All good!')
