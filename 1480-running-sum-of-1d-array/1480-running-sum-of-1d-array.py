class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = []
        var = 0
        for i in range(len(nums)):
            nums[i] += var
            var = nums[i]
            temp.append(var)
        return (temp)    
        