# Input: n = 5, arr = [1,2,3,4,5]
# Output: True
# Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.

class Solution:
    def arraySortedOrNot(self,nums, n):
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    return True
        return False

sol = Solution()
nums = [1,2,3,4,5]
n = 5
print('checking the sorting of array:',sol.arraySortedOrNot(nums,n))

# nums = [1,2,3,4,5]
# n = 5
# print('Checking the sorting of the array:', arraySortedOrNot(nums,5))
