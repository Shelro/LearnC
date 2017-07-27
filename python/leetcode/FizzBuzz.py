class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        num = 1
        result = []
        while num<=n:
            if num%15==0:
                result.append("FizzBuzz")
            elif num%3==0:
                result.append("Fizz")
            elif num%5==0:
                result.append("Buzz")
            else:
                result.append(str(num))
            num += 1
        
        return result
