class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count = 0
        # n = len(nums)
        # for i in range(n):
        #     total = 0
        #     for j in range (i, n):
        #         total += nums[j]
        #         if total == k:
        #             count += 1
        # return count
        count = 0
        prefix = 0
        seen = {0: 1}  # prefix_sum: frequency

        for num in nums:
            prefix += num
            count += seen.get(prefix - k, 0)
            seen[prefix] = seen.get(prefix, 0) + 1

        return count

        