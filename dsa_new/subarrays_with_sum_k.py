# nums = [1, 1, 1], k = 2
# subarrays with sum k

#Brute force
def countSubArrays(nums, k):
    count = 0
    n = len(nums)

    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += nums[end]
            if current_sum == k:
                count += 1
    
    return count

nums = [1,1,1]
k = 2
print('the subarray with sum k', countSubArrays(nums, k))


#Optimal solution 

def countSubArraysOptimize(nums, k):
    prefix_sum = 0
    count = 0
    prefix_map = {0:1}

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum-k]

        if prefix_sum in prefix_map:
            prefix_map[prefix_sum] += 1
        else:
            prefix_map[prefix_sum] = 1
    
    return count

nums = [1,1,1]
k = 2
print('the subarray with sum k', countSubArraysOptimize(nums, k))
