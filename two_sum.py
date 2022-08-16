from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values_map = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in values_map:
                return [values_map[diff], index]
            values_map[value] = index


if __name__ == '__main__':
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
    assert solution.twoSum([3, 2, 3], 6) == [0, 2]
    assert solution.twoSum([2, 5, 5, 11], 10) == [1, 2]
    assert solution.twoSum([2, 7, 11, 15, 19, 23], 21) == [0, 4]
    assert solution.twoSum([1, 6142, 8192, 10239], 18431) == [2, 3]

    print('All good!')
