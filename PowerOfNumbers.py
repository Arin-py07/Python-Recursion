Test case 1 : 
Input:
N = 2
Output: 4
Explanation: The reverse of 2 is 2
and after raising power of 2 by 2 
we get 4 which gives remainder as 
4 by dividing 1000000007.

Test case 2:
Input:
N = 12
Output: 864354781
Explanation: The reverse of 12 is 21
and 1221 , when divided by 1000000007 
gives remainder as 864354781.

Solution:

class Solution:
  
    #Complete this function
    def power(self,N,R):
        if R == 0:
            return 1
    
        t = self.power(N, R // 2)
        ans = t * t

        if R % 2 == 0:
            if ans > 1000000007:
                ans %= 1000000007
            return ans
        else:
            ans = N * ans
            if ans > 1000000007:
                ans %= 1000000007
            return ans
