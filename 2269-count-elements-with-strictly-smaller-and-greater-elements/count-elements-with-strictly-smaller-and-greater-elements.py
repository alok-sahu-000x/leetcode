class Solution:
    def countElements(self, nums: list[int]) -> int:
        if not nums:
            return 0

        mi = min(nums)
        mx = max(nums)

        return sum(1 for x in nums if mi < x < mx)
        