# check if there are any two equal numbers in an array at a distance less than or equal to k

def contains_nearby(nums, k):
    num_indices = {}
    #iterating with each element in the map
    for i, num in enumerate(nums):
        if num in num_indices and i - num_indices[num] <= k:
            return True
        num_indices[num] = i
    return False

def main():
    nums = [1, 1, 3, 1, 2, 3]
    k = 2
    if contains_nearby(nums, k):
        print('There are numbers with distance <=', k)
    else:
        print('No two equal numbers within distance', k)

if __name__ == "__main__":
    main()
