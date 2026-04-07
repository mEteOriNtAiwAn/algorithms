class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            center = start + (end - start) // 2 
            if(nums[center] > target):
                end = center - 1
            elif(nums[center] < target):
                start = center + 1
            else:
                return center

        return -1