class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]:
                nums[index] = nums[i+1]
                index += 1

        return index


if __name__ == '__main__':
    sol = Solution()

    nums = [1, 1, 2]

    ret = sol.removeDuplicates(nums)

    print(ret)