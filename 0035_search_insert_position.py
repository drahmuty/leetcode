class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid
            else:
                low = mid + 1
        if target < nums[mid]:
            return mid
        else:
            return mid + 1
