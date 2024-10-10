from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for word in strs:
            sorted_str = ''.join(sorted(word))
            group[sorted_str].append(word)

        return [values for keys,values in group.items()]
