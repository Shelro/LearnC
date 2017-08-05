def findRadius(houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        """
        My Answer: can't solve problem
        houses.sort()
        heaters.sort()
        
        dis = []
        
        outLeft = -1
        outRight = -1
        for i in range(len(heaters)):
            if heaters[i]<houses[0]:
                outLeft = i
            if heaters[len(heaters)-1-i]>houses[-1]:
                outRight = len(heaters)-1-i
        first = 0
        last = len(heaters)-1
        if outLeft!=-1:
            first = outLeft
        if outRight!=-1:
            last = outRight
        for i in range(first,last):
            dis.append(heaters[i+1]-heaters[i])
        print dis
        if outLeft==-1:
            dis.insert(0, 2*(heaters[0]-houses[0]))
        print dis
        if outRight==-1:
            dis.append(2*(houses[-1]-heaters[-1]))
        print dis
        return max(dis)/2
        """
        #Find the max one in the closest distances between these houses and heaters
        heaters = sorted(heaters) + [float('inf')]
        i = r = 0
        for x in sorted(houses):
            while x >= sum(heaters[i:i+2]) / 2.:  #Find out whether next heater is closer to the house
                i += 1
            r = max(r, abs(heaters[i] - x))
        return r

h1 = [1,2,3,5,15]
h2 = [2,30]
print findRadius(h1,h2)
