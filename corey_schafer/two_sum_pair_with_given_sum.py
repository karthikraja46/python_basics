nums = [0, -1, 2, -3, 1]
target = -2

def two_sum(nums, target):
    nums.sort()
    left,right = 0, len(nums)-1
    while left<right:
        sum = nums[left]+nums[right]
        if sum == target:
            return True
        elif sum < target:
            left += 1
        else:
            right -= 1
    return False

print(two_sum(nums, target))
