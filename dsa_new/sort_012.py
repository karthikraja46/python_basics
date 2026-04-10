def sort_012_brute_force(nums):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for num in nums:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        else:
            count_2 += 1
    
    for i in range(count_0):
        nums[i] = 0
    
    for j in range(count_0, count_0 + count_1):
        nums[j] = 1
    
    for k in range(count_0 + count_1, len(nums)):
        nums[k] = 2
    
    return nums

nums = [0,1,2,0,1,2]
print(sort_012_brute_force(nums))


#optimized approach
def sort_012(nums):
    low, high, mid = 0, len(nums)-1, 0
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

nums = [0,1,2,0,1,2]
print(sort_012(nums))
