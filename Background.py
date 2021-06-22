#Statements
def fun1():
    print("fun1 called")


def fun2():
    print("Before fun1()")
    fun1()
    print("After fun1()")


print("Before fun2()")
fun2()
print("After fun2()")


Result:
 
Before fun2()
Before fun1()
fun1 called
After fun1()
After fun2()
