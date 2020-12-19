# TWO SUM

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Save list of index-value pairs
        nums_mod = []
        for i in range(len(nums)):
            nums_mod.append((i, nums[i]))

        # Sort list by value
        nums_mod = sorted(nums_mod, key = lambda x: x[1])

        # Find sum
        i = 0
        j = len(nums)-1
        x = y = None
        while i < j:
            sum = nums_mod[i][1] + nums_mod[j][1]
            if sum == target:
                x = nums_mod[i][0]
                y = nums_mod[j][0]
                break
            elif sum < target:
                i += 1
            else:
                j -= 1

        # Return result, if it exists
        if x is None or y is None:
            return None
        elif x < y:
            return x, y
        else:
            return y, x
