class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = nums[0]
        calc = nums[0]
        for i in nums[1:]:
            calc = max(i, calc+i)
            max_val = max(max_val, calc)
            print(f'Max: {max_val} - Calc: {calc}')
        return max_val

sol = Solution()
arr = [5,4,-1,7,8]
res = sol.maxSubArray(arr)
print(res)