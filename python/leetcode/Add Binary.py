class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        tempA = a[::-1]
        tempB = b[::-1]
        length = min(len(a),len(b))
        carry = False
        for i in xrange(length):
            if tempA[i]=="1" and tempB[i]=="1":
                if carry:
                    res = "1"+res
                else:
                    res = "0"+res
                    carry = True
            elif tempA[i]=="0" and tempB[i]=="0":
                if carry:
                    res = "1"+res
                    carry = False
                else:
                    res = "0"+res
            else:
                if carry:
                    res = "0"+res
                else:
                    res = "1"+res
        if len(a)>length:
            for i in xrange(length,len(a)):
                if tempA[i]=="1":
                    if carry:
                        res = "0"+res
                    else:
                        res = "1"+res
                else:
                    if carry:
                        res = "1"+res
                        carry = False
                    else:
                        res = "0"+res
        if len(b)>length:
            for i in xrange(length,len(b)):
                if tempB[i]=="1":
                    if carry:
                        res = "0"+res
                    else:
                        res = "1"+res
                else:
                    if carry:
                        res = "1"+res
                        carry = False
                    else:
                        res = "0"+res
        if carry:
            res = "1"+res
        return res

        """
        Better Solution:

        addsum=int(a,2)+int(b,2)
        return bin(addsum)[2:]
        """