nums1 = [1,2,3,4]
nums2 = [5,6,7,8]

n = len(nums1)
m = len(nums2)

for i in range(n):
    for j in range(m):
        sum = nums1[i] + nums2[j]
        print(sum, end=" ")
