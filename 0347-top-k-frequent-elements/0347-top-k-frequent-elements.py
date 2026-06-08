from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted_nums = Counter(nums)
        most_frequent_k_key = [key for key, counted_nums in counted_nums.most_common(k)]
        return most_frequent_k_key
        