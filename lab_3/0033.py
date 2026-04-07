class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            center = start + (end - start)//2

            if nums[center] == target: return center 
            if nums[start] <= nums[center]:
                if nums[start] <= target < nums[center]:
                    end = center - 1
                else:
                    start = center + 1

            else:
                if nums[center] < target <= nums[end]:
                    start = center + 1
                else:
                    end = center - 1

        return -1
