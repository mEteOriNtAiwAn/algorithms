def twoSum(nums: list[int], target: int) -> list[int]:
        dict_ = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if dict_.get(temp) is not None:
                return list((i, dict_[temp]))

            dict_[nums[i]] = dict_.get(nums[i], i)
        return []