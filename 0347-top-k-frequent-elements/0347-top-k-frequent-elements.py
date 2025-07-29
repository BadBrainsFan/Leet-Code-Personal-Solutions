class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        answer = []
        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)
        sorted_count_dict = dict(sorted(count_dict.items(), key=lambda item:item[1], reverse=True))
        for key in sorted_count_dict.keys():
            answer.append(key)
        return answer[:k]