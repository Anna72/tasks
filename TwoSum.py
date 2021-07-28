class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = dict()
        for i,v in enumerate(nums):
            if (target - v in x):
                return(x[target - v],i)
            else: 
                x[v] = i
                
