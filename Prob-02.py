#Statements

def fun(n):
    if n == 0:
        return
    fun(n - 1)
    print(n)
    fun(n - 1)


fun(3)

#Results
1
2
1
3
1
2
1
