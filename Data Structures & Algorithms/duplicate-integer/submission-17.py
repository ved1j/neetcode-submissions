class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        aura = set()

        for num in nums:
            if num in aura:
                return True
            aura.add(num)
        return False

            



        