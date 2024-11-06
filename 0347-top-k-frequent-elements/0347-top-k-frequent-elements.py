class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in nums]

        # O(N)
        c = collections.Counter(nums)

        # O(d) where d is the number of distinct numbers. d <= N
        for num, freq in c.items():
            bucket[-freq].append(num)
            
        # O(?)
        return list(itertools.chain(*bucket))[:k]