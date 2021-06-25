You are given two numbers n and r. You need to find nCr.
nCr = (n!) / ((n-r)!*(r!))
In recursive way, we can write nCr as nCr = (n-1)C(r-1) + (n-1)Cr

#Solution : loop

def nCr(n,r):
    #code here
    def fact(n):
        res = 1
        
        for i in range (2, n+1):
            res = res*i
        return res
        
    return fact(n)//(fact(n-r)*fact(r))
  
  
  #Solution : math
  
  import math

  def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)
