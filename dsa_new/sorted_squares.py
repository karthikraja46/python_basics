# nums = [-4, -1, 0, 3, 10]
# Output: [0,1,9,16,100]

def squaresSorted(nums):

    result = []
    n = len(nums)
    for x in range(n):
        result.append(x*x)
    result.sort()
    return result
nums = [-4,-1,0,3,10]
print('the squares of arrays is',squaresSorted(nums))

