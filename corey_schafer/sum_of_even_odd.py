nums=[1,3,4,5,6,7,8,9]
n = len(nums)
even = 0
odd = 0

for i in range(n):
    if nums[i]%2==0:
        even += nums[i]
    else:
        odd += nums[i]

print(even, odd)