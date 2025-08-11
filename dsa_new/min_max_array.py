# Input: arr[] = [3, 2, 1, 56, 10000, 167]
# Output: 1 10000
# Explanation: minimum and maximum elements of array are 1 and 10000.

def min_max_array(nums):
    min_val = nums[0]
    max_val = nums[0]

    for num in nums:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return(min_val, max_val)

nums = [3,2,1,56,100000,167,886666666656556565]
print('the min and max values in an array',min_max_array(nums))
