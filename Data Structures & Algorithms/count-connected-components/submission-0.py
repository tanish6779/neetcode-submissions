class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i: [] for i in range(n)} #creates a dictionary with empty list for each node
        
        for n1,n2 in edges: #appending the both n1 and n2 to eachother since its undirected
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set() #visit set to keep track
        count = 0

        def dfs(i):
            visit.add(i)
            
            for j in adj[i]:
                if j not in visit:
                    dfs(j)
            
        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i)
        return count


                


        


