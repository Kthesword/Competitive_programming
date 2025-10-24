class MagicDictionary:

    def __init__(self):
        self.di = []


    def buildDict(self, dictionary: List[str]) -> None:
        self.di = dictionary


    def search(self, searchWord: str) -> bool:
        for word in self.di:
            if len(word) == len(searchWord) and word != searchWord:
                print(word, searchWord)
                mismatches = 0
                for c1, c2 in zip(word, searchWord):
                    word, 
                    if c1 != c2:
                        print(c1, c2)
                        mismatches += 1
                        if mismatches > 1:
                            break

                if mismatches == 1:    
                    return True

        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)