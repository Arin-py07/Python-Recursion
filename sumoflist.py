
#using recursiin

def sum_list(l):
    if len(l)==0:
        return 0
    return (l[0] + sum_list(l[1:])) #1st digit of the list and rest of the digit


#empty list
numbers = []
n = int(input("Enter the numbers you want to be add in a list:"))

for x in range(n):
    num = int(input("Enter a number :"))
    numbers.append(num)
    
#printiong the list
print("The list is:", numbers)
#calling the sum_list functions
print("The sum of the list are:", sum_list(numbers))
    

Output:
  
Enter the numbers you want to be add in a list:3
Enter a number :6
Enter a number :7
Enter a number :1
The list is: [6, 7, 1]
The sum of the list are: 14
