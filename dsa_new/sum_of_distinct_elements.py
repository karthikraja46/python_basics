def sum_of_distinct_elements(nums):
    map = {}
    count = 0
    for num in nums:
        if num not in map:
            count += num

    return count

nums = [1, 2, 3, 2, 4, 1]
print(sum_of_distinct_elements(nums))