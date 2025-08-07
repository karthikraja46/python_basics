# move zeroes to end
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

nums = [0,1,0,3,12]
n = len(nums)

left = 0
for right in range(n):
    if nums[right] != 0:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1

print('moved zeroes to the end',nums)