class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [ [] for i in nums]
        count = Counter(nums)
        for item, freq in count.items():
            bucket[-freq].append(item)
        return list(chain(*bucket))[:k]