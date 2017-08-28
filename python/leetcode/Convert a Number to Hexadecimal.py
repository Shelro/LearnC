class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return '0'
        res = ""
        if num<0:
            num = 16**8 - abs(num)
        while num>0:
            temp = num%16
            if temp<10:
                res = str(num%16)+res
            else:
                res = chr(ord('a')-10+temp)+res
            num = num/16
        return res
        
        """
        Faster Solution:

        hexlist="0123456789abcdef"
        result=""
        if num == 0:return "0"
        i = 0 
        while(num!=0 and i < 8):
            result=hexlist[num & 15]+result
            num = num >> 4
            i+=1
        return result
        """