# def sum_of_distinct_elements(nums):
#     map = {}
#     count = 0
#     for num in nums:
#         if num not in map:
#             count += num
#             map[num] = True

#     return count

# nums = [1, 2, 3, 2, 4, 1]
# print('sum of distinct elements',sum_of_distinct_elements(nums))


# solving without any extra space

def sum_of_distinct_elements(nums):
    nums.sort()
    total = nums[0]

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            total += nums[i]
    return total

nums = [1, 2, 3, 2, 4, 1]
print('sum of distinct elements',sum_of_distinct_elements(nums))