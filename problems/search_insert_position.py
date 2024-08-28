class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        if len(nums) == 0:
            return 0
        high = len(nums) - 1
        low = 0
        while low <= high:
            mid = int((high + low) / 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low




if __name__ == '__main__':
    sol = Solution()

    
    res = sol.searchInsert([1, 3, 5, 6], 7)
    print(res)