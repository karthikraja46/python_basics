from typing import List
class TwoSum:
    def twoSum(self, nums:List[int], target: int):
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

if __name__ == "__main__":
    nums = list(map(int, input('Enter the numbers........:').split()))
    target = int(input("Enter the value.........:"))

    twosum = TwoSum()
    result = twosum.twoSum(nums, target)

    if result:
        print(f"Indices of numbers adding up to target: {result}")
    else:
        print("No two numbers add up to the target.")


