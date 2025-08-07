# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7

def subarraysDivByK(nums, k):
    prefix_sum = 0
    count = 0
    remainder_count = {0:1}
    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k
        if remainder <0:
            remainder += k
            
        if remainder in remainder_count:
            count += remainder_count[remainder]
            remainder_count[remainder] += 1
        else:
            remainder_count[remainder] = 1

    return count

nums = [4,5,0,-2,-3,1]
k = 5
print('the subarrays divisible by k',subarraysDivByK(nums,k))