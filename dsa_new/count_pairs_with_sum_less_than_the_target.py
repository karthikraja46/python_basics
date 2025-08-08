# Input: nums[] = [7, 2, 5, 3], target = 8
# Output: 2 
# def binarySearch(nums, complement):
#     left, right = 0, len(nums)-1
#     result = len(nums)
#     while left <= right:
#         mid = (left + right)//2
#         if nums[mid] >= complement:
#             result = mid
#             right = mid-1
#         else:
#             left = mid+1
#     return result
    
# def countPairs(nums, target):
#     count = 0
#     nums.sort()

#     for i in range(len(nums)):
#         complement = target-nums[i]
#         ind = binarySearch(nums, complement)
#         count += ind

#         if ind > i:
#             count -= 1
    
#     return count // 2


# Python program to count pairs with sum less 
# than target using two pointers technique

def countPairs(nums, target):
  
    nums.sort()
    left, right = 0, len(nums) - 1
    count = 0

    while left < right:
        sum = nums[left] + nums[right]

        if sum < target:
            count += right - left
            left += 1
        else:
            right -= 1

    return count


nums = [2,1,8,3,4,7,6,5]
target = 7
print('the pairs in which sum less than target',countPairs(nums, target))