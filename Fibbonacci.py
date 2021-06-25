You are given a number n. You need to find nth Fibonacci number.
F(n)=F(n-1)+F(n-2); where F(1)=1 and F(2)=1

#Solution:

class Solution:
    def fibonacci(self,n):
        
        if n == 1 or n == 2:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)
