# nums = [1, 2, 1, 3, 4, 2, 3]

def count_distinct_elements(nums):

    distinct_elements = set()
    for num in nums:
        distinct_elements.add(num)
    return len(distinct_elements)

nums = [1, 2, 1, 3, 4, 2, 3]
count = count_distinct_elements(nums)
print('the count', count)


