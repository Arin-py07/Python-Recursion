#Statements

def fun(n):
    if n == 0:
        return
    fun(n//2)
    print(n % 2)


fun(13)

#Output:
1
1
0
1
