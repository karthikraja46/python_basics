
nums1=[1,2,3]
nums2=[4,5,6]

n= len(nums1)
m=len(nums2)
mx=0


for i in range(n):
    for j in range(m):
        sum=nums1[i]+nums2[j]
        mx=max(mx,sum)
        
print(mx)