# Count all the (i,j) Pairs such that b[i] + b[j] == k (count of such pairs.) [i<j] 
# brute force
# def count_pairs_brute_force(b,k):
#     count = 0
#     n = len(b)

#     for i in range(n):
#         for j in range(i+1, n):
#             if b[i] + b[j] == k:
#                 count += 1
#     return count

# b = [1,5,7,-1,5]
# k = 6
# print('brute force count',count_pairs_brute_force(b,k))

#optimal solution
def count_pairs_with_sum(b,k):
    freq = {}
    count = 0

    for num in b:
        complement = k - num

        if complement in freq:
            count += freq[complement]

        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return count

b = [1,5,7,-1,5]
k = 6
print('efficient count',count_pairs_with_sum(b,k))