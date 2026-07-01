class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        my_set = set()
        for i in range(n):
            if nums[i] in my_set:
                return True
            my_set.add(nums[i])
        return False    
