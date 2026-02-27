class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp = 0
        max_val = 0
        for i in range(len(nums)):
            if nums[i]==1:
                temp+=1
                max_val = max(max_val,temp)
            else:
                nums[i] == 0
                temp = 0
        return(max_val)                      
        