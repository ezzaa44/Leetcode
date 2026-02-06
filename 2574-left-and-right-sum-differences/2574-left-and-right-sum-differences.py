class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        leftsum = 0
        for i in range (n):
            res [i] = leftsum
            leftsum += nums[i]
        rightsum = 0
        for i in range(n-1,-1,-1):
            res[i] = abs(res[i] - rightsum)
            rightsum +=  nums[i] 
        return (res)       
        