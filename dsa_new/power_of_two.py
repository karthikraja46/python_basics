# Input: n = 1
# Output: true
# Explanation: 2^0 = 1


def isPowerOfTwo(n):
        if n>0 and n&(n-1)==0:
            return True
        else:
            return False
        
n = 3
print('the power of two', isPowerOfTwo(n))

isPowerOfTwo = lambda n: n > 0 and n & (n - 1) == 0
print('the power of two', isPowerOfTwo(8))
