class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for word in strs:
            sorted_tuple_word = tuple(sorted(word))
            answer[sorted_tuple_word].append(word)
        return list(answer.values())