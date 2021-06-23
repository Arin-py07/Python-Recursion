Input:
n = 99999
Output: 45
  
Solution:
class Solution:
    def sumOfDigits(self, n):
        '''
        :param n: given number
        :return: sum of digits of n.
        '''
        if n < 10:
            return n
        return (self.sumOfDigits(n//10) + n%10)
