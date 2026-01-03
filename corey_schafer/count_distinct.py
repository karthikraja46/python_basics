nums = [1,2,2,3,3,4,4,5,5,6,7,8,8,9]
visited = {}
count = 0

for num in nums:
    if not visited.get(num, False):
        count += 1
        visited[num] = True

print(count)

## Different method

def countDistinct(nums):
    freq={}
    for num in nums:
        freq[num] = 1
        
    return len(freq)
