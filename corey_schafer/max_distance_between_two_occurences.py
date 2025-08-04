# Input: arr = [1, 1, 2, 2, 2, 1]
# Output: 5
# Explanation: distance for 1 is: 5-0 = 5, distance for 2 is: 4-2 = 2, So max distance is 5.

# Input : arr[] = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
# Output: 10
# Explanation : Max distance for 2 is 11-1 = 10, max distance for 1 is 4-2 = 2 and max distance for 4 is 10-5 = 5  

def maxDistance(nums):
    mp = {}
    res = 0

    for i in range(len(nums)):
        if nums[i] not in mp:
            mp[nums[i]] = i
        else:
            res = max(res, i-mp[nums[i]])

    return res

nums = [1,1,2,2,2,1]
print(maxDistance(nums))
