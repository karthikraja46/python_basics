# Input: n=5, arr = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]

def reverse_array(nums, n):
    left = 0
    right = n-1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums

nums = [5,4,3,2,1]
n = 5
print('The reverse of an array is:',reverse_array(nums,n))
