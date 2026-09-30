class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        newgraph = {}

        def dfs(node):
            if node in newgraph:
                return newgraph[node]

            copy = Node(node.val)
            newgraph[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)