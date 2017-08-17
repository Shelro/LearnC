class Solution:

    # @param n, an integer

    # @return an integer

    def reverseBits(self, n):

        #Not Solve by myself
        return int(bin(n)[2:].zfill(32)[::-1], 2)
        """
        Faster Solution:

        s = bin(n)[2:]
        s = str((32-len(s))*'0' + s)
        s = s[::-1]
        return int(s, 2)
        """