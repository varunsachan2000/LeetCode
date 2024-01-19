class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=0
        lis=list()
        for i in range(n, len(nums)):
            for j in range(n+1,len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    return [i,j]
        
        