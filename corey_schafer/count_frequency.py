arr = [1, 2, 3, 3, 4, 5, 5, 6]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for key in freq:
    print(f"{key} -> {freq[key]}")
