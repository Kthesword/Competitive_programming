class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = set()
        def dfs(s,idx):
            if idx == len(s):
                return

            if s[idx].isalpha():
                if s[idx].isupper():
                    tmp = s[:idx] + s[idx].lower() + s[idx + 1:]
                else:
                    tmp = s[:idx] + s[idx].upper() + s[idx + 1:]

                res.add(tmp)
                dfs(tmp, idx + 1)
                dfs(s, idx + 1)
                    
            else:
                dfs(s, idx + 1)
        res.add(S)
        dfs(S, 0)
        return list(res)
