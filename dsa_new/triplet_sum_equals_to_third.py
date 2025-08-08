
def search(sum, start, end, nums):
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == sum:
            return True
        elif nums[mid] > sum:
            end = mid-1
        else:
            start = mid +1
    return False

def findTriplet(nums):
    nums.sort()
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if search(nums[i] + nums[j], j+1,n-1, nums):
                return True
        return False

nums = [5, 32, 1, 7, 10, 50, 19, 21, 2]
print("true" if findTriplet(nums) else "false")
