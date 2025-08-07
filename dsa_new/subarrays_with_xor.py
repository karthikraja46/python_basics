# Given an array of integers A and an integer B.

# Find the total number of subarrays having bitwise XOR of all elements equals to B.
# Problem Constraints
# 1 <= length of the array <= 105
# 1 <= A[i], B <= 109
# Input Format
# The first argument given is the integer array A.
# The second argument given is integer B.
# Output Format
# Return the total number of subarrays having bitwise XOR equals to B
# Example Input
# Input 1:
#  A = [4, 2, 2, 6, 4]
#  B = 6
# Input 2:
#  A = [5, 6, 7, 8, 9]
#  B = 5
# Output 1:

#  4
# Output 2:

#  2

def subarrays_with_xor(nums1, value):
    xor = 0
    count = 0
    freq = {}

    for num in nums1:
        xor ^= num

        if xor == value:
            count += 1
        
        required = xor ^ value
        if required in freq:
            count += freq[required]
        
        if xor in freq:
            freq[xor] += 1
        else:
            freq[xor] = 1

    return count

nums1 = [4,2,2,6,4]
value = 6

print('subarray with xor',subarrays_with_xor(nums1,value))