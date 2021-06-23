#Statements

def fun(n):
    if n == 0:
        return
    print(n)
    fun(n - 1)
    print(n)


fun(3)


#Results

3
2
1
1
2
3
