#Default argument

# def student(roll,n,dept='MCA'):
#     print("rollnumber:",roll)
#     print("Name:",n)
#     print("department:",dept)
# student(1,'jack')
# student(5,'adam','Msc')

#keyword arguments

# def student(roll,n):
#     print("rollnumber:",roll)
#     print("Name:",n)
# student(n='jack',roll=10)

#Recursion-a function calling itself
#factorial of a number
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(4))

#find the sum of first n natural numbers using recursion

# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return n+sum(n-1)
# print(sum(5))