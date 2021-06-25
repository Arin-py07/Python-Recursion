Input:
n = 5
arr[] = {1,2,3,4,5}
Output: 1 2 3 4 5
  
#Soluton:
class Solution:
    def printArrayRecursively(self,arr,n):
        #code here
        i = 0
        for i in range(n):
            print(arr[i], end=" ")
            i+=1
