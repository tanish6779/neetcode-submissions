class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i: [] for i in range(n)} #creates a dictionary with empty list for each node
        
        for n1,n2 in edges: #appending the both n1 and n2 to eachother since its undirected
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set() #visit set to keep track
        count = 0

        def dfs(i): 
            visit.add(i) #adding i to the visited set
            
            for j in adj[i]: #for each neighbour of i (j) we check if its in visited, if not we do dfs(j)
                if j not in visit:
                    dfs(j)
            
        for i in range(n): #for a i which is not in visited means it is disconnected
            if i not in visit:#since it is disconnected we increment count and do same dfs(i)
                count += 1
                dfs(i)
        return count
        #take 0-1 2-3 i = 0 and dfs 0, increment count and keep 0 in visited, 1 is neighbour(j) so we add in visited. now we move to 2 since it is not already in 2 that means it is not connected to 1 and 0 hence it is disconnected so we increment count. We carry on the process


                


        


