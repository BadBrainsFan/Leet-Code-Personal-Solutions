class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in nums]
        count = Counter(nums)
        for num, freq in count.items():
            bucket[-freq].append(num)
        return list(itertools.chain(*bucket))[:k]