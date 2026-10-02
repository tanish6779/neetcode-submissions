class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows = len(heights)
        cols = len(heights[0])
        pacific = set()

        def dfspacific(r,c,pacific):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in pacific:
                return 
            
            pacific.add((r,c))

            if r + 1 < rows and heights[r + 1][c] >= heights[r][c]:
                dfspacific(r+1, c, pacific)
            
            if r - 1 >= 0 and heights[r - 1][c] >= heights[r][c]:
                dfspacific(r-1, c, pacific)
            
            if c + 1 < cols and heights[r][c + 1] >= heights[r][c]:
                dfspacific(r, c+1, pacific)

            if c - 1 >= 0 and heights[r][c - 1] >= heights[r][c]:
                dfspacific(r, c-1, pacific)
            
        for c in range(cols):
            dfspacific(0, c, pacific) # r = 0 means the first row, since pacific is first row and first column
        for r in range(rows):
            dfspacific(r, 0, pacific)

        atlantic = set()

        def dfsatlantic(r,c,atlantic):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in atlantic:
                return #boundary function
            
            atlantic.add((r,c))

            #direction checking, right, left, up, down
            if r + 1 < rows and heights[r + 1][c] >= heights[r][c]:
                dfsatlantic(r+1,c,atlantic)
            if r - 1 >= 0 and heights[r - 1][c] >= heights[r][c]:
                dfsatlantic(r-1,c,atlantic)
            if c + 1 < cols and heights[r][c+1] >= heights[r][c]:
                dfsatlantic(r,c+1,atlantic)
            if c - 1 >= 0 and heights[r][c-1] >= heights[r][c]:
                dfsatlantic(r,c-1,atlantic)
        for c in range(cols):
            dfsatlantic(rows-1,c,atlantic)
        for r in range(rows):
            dfsatlantic(r,cols-1,atlantic)

        result = []

        for r,c in pacific & atlantic:
            result.append([r,c])
        return result

            
            

    
