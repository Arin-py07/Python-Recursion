Input:
n = 5
Output: 120
Example 2:

Input:
n = 0
Output: 1
  
#Solutions
class Solution:
    def factorial(self,n):
        #code here
        if n == 0:
            return 1
        else:
            return (n*self.factorial(n-1))
