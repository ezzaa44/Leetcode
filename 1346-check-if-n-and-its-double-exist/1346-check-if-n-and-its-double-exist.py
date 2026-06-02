class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        h = set()
        for i in arr:
            if (i *2 in h) or (i/2 in h):  
                    return True
            h.add(i)        
            
        return False
        
        