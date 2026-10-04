class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        prevmap = {i: [] for i in range(n)}

        for parent, child in edges:
            prevmap[parent].append(child)
            prevmap[child].append(parent)
        
        visited = set()
        
        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            for j in prevmap[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False
            return True
        return dfs(0,-1) and n == len(visited)
            

            

        