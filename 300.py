class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = defaultdict(lambda : float('inf'))
        res = 1
        dp[0] = min(nums) - 1
        for i, n in enumerate(nums):
            keys = list(dp.keys())
            for k in keys:
                if dp[k] < n:
                    dp[k + 1] = min(dp[k + 1], n)
        return max(dp.keys())
