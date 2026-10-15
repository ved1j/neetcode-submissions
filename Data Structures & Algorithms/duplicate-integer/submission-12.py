class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        aura = []

        for num in nums:
            if num in aura:
                return True
            aura.append(num)
        return False

            



        