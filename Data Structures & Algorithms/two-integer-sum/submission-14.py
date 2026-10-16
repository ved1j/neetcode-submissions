class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}
        
        for i, n in enumerate(nums):
            thing = target - n
            if thing in map:
                return [map[thing], i]
            map[n] = i
        return

        
        

 
        

        