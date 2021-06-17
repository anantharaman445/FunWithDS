
from collections import defaultdict
from typing import List
def get_indices(num_list):
    res_dict = {}
    for i,item in enumerate(num_list): 
        if not res_dict.get(item):
            res_dict[item] = []
        res_dict[item].append(i)
    return res_dict
            
    
def twoSum(nums: List[int], target: int) -> List[int]:
    res_dict = get_indices(nums)
    for index, number in enumerate(nums):
        k = target - number
        if k in nums[index + 1:]:
            
            num_set = set()
            num_set.add(index)
            num_set.union(set(res_dict[k]))
            
            return list(num_set.union(set(res_dict[k])))
        
    return []

if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9,))