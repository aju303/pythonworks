#lambda function/anonymous function

#sum of 2 numbers

# sum=lambda a,b:a+b
# n1=int(input("enter number 1"))
# n2=int(input("enter number 2"))
# print(sum(n1,n2))

#find the square of a number using lambda function

# sq=lambda n:n*n
# print(sq(2))

#calculate simple interest

# simpleinterest=lambda p,n,r:p*n*r/100
# p1=int(input("enter principle amount"))
# n1=int(input("enter no of years"))
# r1=int(input("enter rate of interest"))
# print("simple interest is",simpleinterest(p1,n1,r1))

#largest among 2 numbers using lambda function

# lar=lambda a,b:a if a>b else b
# print(lar(5,7))

#largest among 3 numbers
# lar=lambda a,b,c:a if a>b and a>c else b if b>a and b>c else c
# print(lar(2,3,4))