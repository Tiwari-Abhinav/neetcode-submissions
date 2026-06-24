class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0

        for num in my_set:
            # start a sequence only if num-1 doesn't exist
            if num - 1 not in my_set:
                x = num
                count = 1

                while x + 1 in my_set:
                    x += 1
                    count += 1

                longest = max(longest, count)

        return longest
