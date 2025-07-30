#Code to find the maximum and minimum frequency of elements in an array
arr = [3,2,5,3,3,2,1,4,5]

#calculating the frequency using map
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

frequencies = list(freq.values())
min_freq = frequencies[0]
max_freq = frequencies[0]
for count in frequencies:
    if count < min_freq:
        min_freq = count
    if count > max_freq:
        max_freq = count

print('minimum frequency',min_freq)
print('maximum frequency',max_freq)
