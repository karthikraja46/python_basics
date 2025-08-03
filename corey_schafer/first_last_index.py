def find_first_last_index_linear(nums, target):
    first_index = -1
    last_index = -1
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            first_index = i
            break
    
    for j in range(n-1, -1,-1):
        if nums[j] == target:
            last_index = i
            break
    
    return (first_index, last_index)

nums = [1,2,3,4,5,5,6]
target = 5
print('linear search', find_first_last_index_linear(nums,target))

def find_first_last_binary(nums, target):
    def binary_search(left):
        l,r =0, len(nums)-1
        res = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                res = mid
                if left:
                    r = mid-1
                else:
                    l = mid+1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid-1
        return res
    
    first = binary_search(True)
    last = binary_search(False)
    return(first, last)

nums = [1,2,3,4,5,5,6]
target = 5
print('binary search', find_first_last_binary(nums,target))
