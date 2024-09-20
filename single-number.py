class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        seen = []
        for i in range(len(nums)):
            if nums[i] in seen:
                sum -= nums[i]
            else:
                sum += nums[i]
                seen.append(nums[i])
        
        return sum

sol = Solution()
print(sol.singleNumber([2,2,1]))