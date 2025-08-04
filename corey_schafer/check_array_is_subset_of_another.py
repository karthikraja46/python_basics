# Input: a[] = [11, 1, 13, 21, 3, 7], b[] = [11, 3, 7, 1] 
# Output: true
# Input: a[]= [1, 2, 3, 4, 5, 6], b = [1, 2, 4] 
# Output: true
# Input: a[] = [10, 5, 2, 23, 19], b = [19, 5, 3] 
# Output: false

def isSubset(a,b):
    a.sort()
    b.sort()

    i=0
    j=0

    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            i+=1
        elif a[i] == b[j]:
            i+=1
            j+=1
        else:
            return False
        
    return j == len(b)

a = [11,1,13,21,3,7]
b = [11,3,7,1]

print('two arrays subset',isSubset(a,b))
