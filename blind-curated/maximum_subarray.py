from typing import List
import sys
def maxSubArray(nums: List[int]) -> int:
    max_sum = nums[0]
    num_sum = 0
    n = len(nums)
    if n==1:
        return max_sum
    for i in range(0, n):
        num_sum = num_sum + nums[i]
        if num_sum < 0:
            max_sum=max(max_sum,num_sum)
            num_sum = 0
        elif max_sum < num_sum:
            max_sum = num_sum
    

    print(max_sum)
    return max_sum
    

if __name__ == "__main__":
  maxSubArray([-2,-1])
#   [-2,1,-3,4,-1,2,1,-5,4], [-2,-1]    [5,4,-1,7,8] [1]