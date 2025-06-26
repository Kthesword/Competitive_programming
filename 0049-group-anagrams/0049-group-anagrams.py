class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dikt = defaultdict(list)
        for st in strs:
            dikt["".join(sorted(st))].append(st)
            
        return dikt.values()

        