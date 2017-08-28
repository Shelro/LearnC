"""
class Solution(object):
    def imageSmoother(self, M):
        My Answer: Not right
        row = len(M)
        col = len(M[0])
        res = M
        if row==1:
            return M
        res[0][0] = int((M[0][0]+M[0][1]+M[1][1]+M[1][0])/4)
        res[0][col-1] = int((M[0][col-2]+M[0][col-1]+M[1][col-2]+M[1][col-1])/4)
        res[row-1][0] = int((M[row-2][0]+M[row-2][1]+M[row-1][0]+M[row-1][1])/4)
        res[row-1][col-1] = int((M[row-2][col-2]+M[row-2][col-1]+M[row-1][col-2]+M[row-1][col-1])/4)
        for i in xrange(1,col-1):
            res[0][i] = int((M[0][i]+M[0][i-1]+M[0][i+1]+M[1][i]+M[1][i-1]+M[1][i+1])/6)
            res[row-1][i] = int((M[row-1][i]+M[row-1][i-1]+M[row-1][i+1]+M[row-2][i]+M[row-2][i-1]+M[row-2][i+1])/6)
        for i in xrange(1,row-1):
            res[i][0] = int((M[i][0]+M[i-1][0]+M[i+1][0]+M[i][1]+M[i-1][1]+M[i+1][1])/6)
            res[i][col-1] = int((M[i][col-1]+M[i-1][col-1]+M[i+1][col-1]+M[i][col-2]+M[i-1][col-2]+M[i+1][col-2])/6)
        for i in xrange(1,row-1):
            for j in xrange(1,col-1):
                res[i][j] = int((M[i-1][j-1]+M[i-1][j]+M[i-1][j+1]+M[i][j-1]+M[i][j]+M[i][j+1]+M[i+1][j-1]+M[i+1][j]+M[i+1][j+1])/9)
        return res
"""
from copy import deepcopy as copy

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        x_len = len(M)
        y_len = len(M[0]) if x_len else 0
        res = copy(M)
        for x in range(x_len):
            for y in range(y_len):
                neighbors = [
                    M[_x][_y]
                    for _x in (x-1, x, x+1)
                    for _y in (y-1, y, y+1)
                    if 0 <= _x < x_len and 0 <= _y < y_len
                ]
                res[x][y] = sum(neighbors) // len(neighbors)
        return res