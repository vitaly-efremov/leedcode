class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)
        max_len = max(a_len, b_len)
        a_shift = (max_len - a_len)
        b_shift = (max_len - b_len)
        sum_value = ''
        extra = 0
        for index in range(max_len-1, -1, -1):
            a_index = index - a_shift
            b_index = index - b_shift
            a_value = a[a_index] if a_index >= 0 else 0
            b_value = b[b_index] if b_index >= 0 else 0
            current_sum = int(a_value) + int(b_value) + extra
            if current_sum == 2:
                extra = 1
                current_sum = 0
            elif current_sum == 3:
                current_sum = 1
            else:
                extra = 0
            sum_value = str(current_sum) + sum_value

        if extra > 0:
            sum_value = str(extra) + sum_value
        return sum_value


class AlternativeSolution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.rjust(max_len, '0')
        b = b.rjust(max_len, '0')
        sum_value = ''
        extra = 0
        for index in range(max_len-1, -1, -1):
            current_sum = int(a[index]) + int(b[index]) + extra
            if current_sum == 2:
                extra = 1
                current_sum = 0
            elif current_sum == 3:
                current_sum = 1
            else:
                extra = 0
            sum_value = str(current_sum) + sum_value

        if extra > 0:
            sum_value = str(extra) + sum_value
        return sum_value


if __name__ == '__main__':
    solution = AlternativeSolution()
    assert solution.addBinary('11', '1') == '100'
    assert solution.addBinary('1010', '1011') == '10101'
    assert solution.addBinary('1111', '1111') == '11110'

    print('All good!')
