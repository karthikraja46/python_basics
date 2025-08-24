# nums = [1,0,0.0,9,8,3,2,1]
# count = 3
def zeros_count(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        if nums[i] == 0:
            count += 1
    return count
nums = [1,0,0,0,9,9,7,0]
print('no of zeroes in the array',zeros_count(nums))