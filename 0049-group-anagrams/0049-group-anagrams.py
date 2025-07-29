class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for word in strs:
            sorted_word_tuple = tuple(sorted(word))
            answer[sorted_word_tuple].append(word)
        return list(answer.values())
