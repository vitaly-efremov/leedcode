import math


class SimpleSolution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = len(s)
        total_columns = math.ceil(n * numRows / (numRows + (numRows - 2))) - numRows
        matrix = [['' for c in range(total_columns)] for r in range(numRows)]
        row = 0
        col = 0
        col_direction = True
        for index in range(n):
            matrix[row][col] = s[index]
            if col_direction:
                row += 1
                col_direction = row + 1 < numRows
            else:
                col += 1
                row -= 1
                col_direction = row == 0

        for row in matrix:
            print(row)
        return ''.join(c for row in matrix for c in row)


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [''] * numRows
        row = 0
        col_direction = True
        for symbol in s:
            rows[row] += symbol
            if col_direction:
                row += 1
                col_direction = row + 1 < numRows
            else:
                row -= 1
                col_direction = row == 0

        return ''.join(rows)


if __name__ == '__main__':
    solution = Solution()
    assert solution.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert solution.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
    assert solution.convert('A', 1) == 'A'
    assert solution.convert('AB', 1) == 'AB'

    print('All good!')
