def sumOfElements(nums, n):
    total = 0
    for i in nums:
        total += i
    return total

nums = [1,2,3,4,5]
n = 5
print('The sum of elements in the array:', sumOfElements(nums,n))