class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        """
        Only Consider 3 elements condition
        dis = []
        same = []
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                dis.append(math.sqrt(pow(points[i][0]-points[j][0], 2) + pow(points[i][1]-points[j][1], 2)))
        dsize = len(points) * (len(points)-1) / 2
        for i in range(dsize-1):
            for j in range(i+1,dsize):
                if dis[i] == dis[j]:
                    same.append([i,j])
        return 2*len(same)
        """
        res = 0
        for p in points:
            cmap = {}
            for q in points:
                f = p[0]-q[0]
                s = p[1]-q[1]
                cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0)
            for k in cmap:
                res += cmap[k] * (cmap[k] -1)
        return res


"""
Another solution ------one line

return sum(
        n * (n - 1)
        for x1, y1 in points
        for n in collections.Counter(
            (x1 - x2) ** 2 + (y1 - y2) ** 2
            for x2, y2 in points).values())
"""