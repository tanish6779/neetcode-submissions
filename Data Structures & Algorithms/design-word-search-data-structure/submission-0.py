class Trienode():
    def __init__(self):
        self.children = {}
        self.endofword = False


class WordDictionary:

    def __init__(self):
        self.root = Trienode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Trienode()
            curr = curr.children[c]
        curr.endofword = True
        

    def search(self, word: str) -> bool:
        
        def dfs(curr, i):
            if i == len(word):
                return curr.endofword
            
            if word[i] == ".":
                for child in curr.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if word[i] not in curr.children:
                    return False

                curr = curr.children[word[i]]
                return dfs(curr, i + 1)
        return dfs(self.root, 0)
        




        
