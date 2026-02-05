class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        var = 0
        for i in range(len(nums)):
            var = var + nums[i]
            nums[i] = var
        return nums    

           
        