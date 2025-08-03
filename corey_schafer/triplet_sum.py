nums = [2,3,4,5,6]
n = len(nums)

for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum = nums[i] + nums[j] + nums[k]
            print(sum, end =" ")