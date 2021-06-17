from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for index, number in enumerate(nums):
        k = target - number
        if k in nums:
            return [index, nums.index(k)]
    
if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9,))
