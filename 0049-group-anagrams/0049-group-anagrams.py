class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)

        for word in strs:
            sorted_word_tuple = tuple(sorted(word))
            anagram_group[sorted_word_tuple].append(word)
        
        return list(anagram_group.values())