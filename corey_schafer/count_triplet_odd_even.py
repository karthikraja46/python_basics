nums = [1,2,3,4,5,6]
n = len(nums)
odd_count = 0
even_count = 0

for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1, n):
            sum = nums[i]+nums[j]+nums[k]
            if sum %2 == 0:
                even_count += 1
            else:
                odd_count += 1
print(even_count, " ",odd_count)