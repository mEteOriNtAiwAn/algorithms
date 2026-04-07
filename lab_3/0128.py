class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        unique_nums = set(nums) 
        max_len = 0

        for num in unique_nums:
            temp_len = 1
            temp_num = num + 1

            if (num - 1) not in unique_nums:
                while(temp_num in unique_nums): 
                    temp_len += 1
                    temp_num += 1
                max_len = max(max_len, temp_len)

        return max_len