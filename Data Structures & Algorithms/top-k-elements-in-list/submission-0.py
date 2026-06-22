from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count frequencies
        count = Counter(nums)
        
        # Step 2: Create buckets where index = frequency
        # Max frequency possible is len(nums), so we need len(nums) + 1 buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # Step 3: Populate the result from right to left (highest to lowest freq)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res