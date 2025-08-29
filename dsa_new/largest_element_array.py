# nums = [1,2,5,6,7,8,9,10]
# output = 10

import time

# Function method
def largest_element(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

# Test data
nums = [1, 2, 5, 6, 7, 8, 9, 10]

# Benchmark function method
start1 = time.perf_counter()
result1 = largest_element(nums)
end1 = time.perf_counter()
print("Largest element (function):", result1)
print("Time taken by code 1 (loop):", end1 - start1)

# Benchmark lambda + max()
largest_element_lambda = lambda nums: max(nums)

start2 = time.perf_counter()
result2 = largest_element_lambda(nums)
end2 = time.perf_counter()
print("\nLargest element (lambda+max):", result2)
print("Time taken by code 2 (lambda+max):", end2 - start2)
