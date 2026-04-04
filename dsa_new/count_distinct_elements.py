# nums = [1, 2, 1, 3, 4, 2, 3]

def count_distinct_elements(nums):

    distinct_elements = set()
    for num in nums:
        distinct_elements.add(num)
    return len(distinct_elements)

nums = [1, 2, 1, 3, 4, 2, 3]
count = count_distinct_elements(nums)
print('the count', count)

#using the hashmap to count the distinct elements in the array
def count_distinct_elements_optimal(nums):
    map = {}
    count = 0
    for num in nums:
        if num not in map:
            count += 1
            map[num] = True
    return count

nums = [1, 2, 1, 3, 4, 2, 3]
count = count_distinct_elements_optimal(nums)
print('the count', count)