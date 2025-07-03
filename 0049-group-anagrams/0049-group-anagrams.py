class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for word in strs:
            word_set = tuple(sorted(word))
            anagram_groups[word_set].append(word)
        return list(anagram_groups.values())