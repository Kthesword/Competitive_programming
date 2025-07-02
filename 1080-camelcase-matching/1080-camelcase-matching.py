class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(query, pattern):
            j = 0
            for i in range(len(query)):
                if j < len(pattern) and query[i] == pattern[j]:
                    j += 1  
                elif query[i].isupper():
                    return False
            return j == len(pattern)  
            
        return [match(query, pattern) for query in queries]