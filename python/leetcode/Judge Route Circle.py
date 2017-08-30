class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        position = [0,0]
        mlist = list(moves)
        for m in mlist:
            if m=="U":
                position[0]+=1
            elif m=="D":
                position[0]-=1
            elif m=="L":
                position[1]-=1
            else:
                position[1]+=1
        if position[0]==0 and position[1]==0:
            return True
        return False
        """
        Faster Solution:

        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
        """