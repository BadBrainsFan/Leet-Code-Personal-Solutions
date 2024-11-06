class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for i in nums]
        frequency = Counter(nums)
        for num, freq in frequency.items():
            bucket[-freq].append(num)
        return list(itertools.chain(*bucket))[:k]