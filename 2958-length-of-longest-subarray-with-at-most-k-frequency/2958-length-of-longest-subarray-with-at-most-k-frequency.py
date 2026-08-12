class Solution:
    def maxSubarrayLength(self, nums, k):
        # Intuition: only nums[right] itself can break the window, shrink from left until it fits again
        n = len(nums)
        r = 1
        left = 0
        freq = {}
        for right in range(n):
            c = nums[right]
            freq[c] = freq.get(c, 0) + 1
            # Decrease window length until k constraint is true again
            while freq[c] > k:
                d = nums[left]
                freq[d] -= 1
                left += 1
            r = max(r, right - left + 1)
        return r