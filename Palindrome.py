You are given a number n. You need to see if the number is a palindrome or not (recursively)

Solution:
class Solution:
    def isPalin(self,N):
        #code here
        str1 = str(N)
        rev = ''.join(reversed(str1))
        
        if str1 == rev:
            return 1
        else:
            return 0
