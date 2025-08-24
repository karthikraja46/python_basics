# nums = [1,2,5,6,7,8,9,10]
# output = 10


def largest_element(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num

    return largest

nums = [1,2,5,6,7,8,9,10]
print('largest element in an array',largest_element(nums))
