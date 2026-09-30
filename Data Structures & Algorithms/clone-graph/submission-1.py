class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldtonewgraph = {}

        def dfs(node):
            if node in oldtonewgraph:
                return oldtonewgraph[node]

            copy = Node(node.val)
            oldtonewgraph[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)