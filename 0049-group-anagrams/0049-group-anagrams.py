class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for word in strs:
            sorted_word_tuple = tuple(sorted(word))
            output[sorted_word_tuple].append(word)
        
        return list(output.values())