class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prevmap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prevmap[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False

            if prevmap[crs] == []:
                return True

            visited.add(crs)

            for pre in prevmap[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            prevmap[crs] = []
            return True

        for crs in prevmap:
            if not dfs(crs):
                return False

        return True