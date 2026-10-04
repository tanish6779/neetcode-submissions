class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        prevmap = {i: [] for i in range(n)} #creates a list for each node and neighbour

        for parent, child in edges:
            prevmap[parent].append(child)
            prevmap[child].append(parent)
        
        visited = set() #visited set to keep track
        
        def dfs(i, prev):
            if i in visited: 
                return False
            
            visited.add(i)
            for j in prevmap[i]: #j is neighbour of i
                if j == prev: #checking to see it the path is actually from the previous or not
                    continue
                if not dfs(j,i): #do dfs of neighbour and the present node and if the dfs finds a cycle then its gives false
                    return False
            return True
        return dfs(0,-1) and n == len(visited)

        
            

            

        