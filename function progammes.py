#find the sum of two numbers using function

# def sum(a,b): #formal parameters/arguments
#     s=a+b
#     print(s)
# num1=int(input("enter number 1"))
# num2=int(input("enter number 2"))
# sum(num1,num2) #actual arguments/parameters


# def sum(a,b): #formal parameters/arguments
#     s=a+b
#     return s #return used to return value from a function
# num1=int(input("enter number 1"))
# num2=int(input("enter number 2"))
# result=sum(num1,num2) #actual arguments/parameters
# print(result)
# avg=result/2
# print(avg)

#four operations
# def calc(a,b):
#     s=a+b
#     d=a-b
#     m=a*b
#     di=a/b
#     return s,d,m,di
# sum,dif,mul,div=calc(3,4)
# print("sum is",sum)
# print("difference is",dif)
# print("product is",mul)
# print("quotient is",div)


#operation by users choice
# def sum(a,b):
#     s=a+b
#     print(s)
# def sub(a,b):
#     d=a-b
#     print(d)
# def mul(a,b):
#     m=a*b
#     print(m)
# def div(a,b):
#     di=a/b
#     print(di)
# num1=int(input("Enter the fist number"))
# num2=int(input("enter the second number"))
# print("1,Addition")
# print("2.Substraction")
# print("3.Multiplication")
# print("4.Division")
# choice=int(input("enter the choice"))
# if choice==1:
#     sum(num1,num2)
# elif choice==2:
#     sub(num1,num2)
# elif choice==3:
#     mul(num1,num2)
# elif choice==4:
#     div(num1,num2)
# else:
#     print("wrong choice")

#Factorial of a number using function
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
# factorial(6)

#check a given number is prime or not using function
def prime(n):
    count=0
    for i in range(1,n+1):
        if n % i == 0:
            count=count+1
        return count
prime(8)
if count==2:
    print("prime no")
else:
    print("not a prime num")
# prime(8)
# if count==2:
#     print("prime no")
# else:
#     print("not a prime num")


