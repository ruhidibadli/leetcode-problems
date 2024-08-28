class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = len(nums)
        
        if a < k:
            k = k % a
        if k == 0:
            return nums
        arr = nums[:-k]
        nums[:k] = nums[-k:]
        nums[k:] = arr

        return nums

sol = Solution()

array = [1, 2]

res = sol.rotate(array, 2)

print(res)