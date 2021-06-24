Test Case 01 :
Input:
n = 1
Output: 1
Explanation: Number of digit in 1 is 1.
  
Test Case 02 :
n  = 99999
Output: 5
Explanation:Number of digit in 99999 is 5.
  
Solution:

class Solution:
    def countDigits(self, n):
        if n < 10:
            return 1
        return 1 + self.countDigits(n//10)
