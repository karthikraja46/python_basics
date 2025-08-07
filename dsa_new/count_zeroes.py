# nums = [1,0,0.0,9,8,3,2,1]
# count = 3

nums = [1,0,0,0,9,8,3,2,1]
n = len(nums)

count = 0 

for i in range(n):
    if nums[i] == 0:
        count += 1
    
print('no of zeroes in the array',count)