class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            temp = target - nums[i]
            try:
                found = nums[i+1:].index(temp)
                found += i + 1
                return [i, found]
            except:
                continue
    

"""
    O(n) Time Complexity
"""