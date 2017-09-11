class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        counts = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]==1:
                    counts+=1
        counts*=4
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])-1):
                if grid[i][j]==1 and grid[i][j+1]:
                    counts-=2
        for i in xrange(len(grid)-1):
            for j in xrange(len(grid[0])):
                if grid[i][j]==1 and grid[i+1][j]:
                    counts-=2
        return counts

        """
        Faster Solution:

        rt = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0]) if grid else 0):
                if grid[i][j]:
                    rt+=4
                    if i>0 and grid[i-1][j]:
                        rt-=2
                    if j>0 and grid[i][j-1]:
                        rt-=2
                        
        return rt
        """