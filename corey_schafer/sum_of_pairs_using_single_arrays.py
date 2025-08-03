nums = [1,2,3,4,5,6]
n = len(nums)

for i in range(n):
    for j in range(i+1, n):
        sum = nums[i] + nums[j]
        print(sum, end=" ")