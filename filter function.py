#filter
#filter(function,seq)
# lst=[3,4,5,6,7,8,9]
# elst=list(filter(lambda x:x%2==0,lst))
# print(elst)

# lst1=['a','abc','apple','grapes']
# newlst=list(filter(lambda x:len(x)>3,lst1))
# print(newlst)

#seperate even&odd list by reading value from user

# lst1=input("enter the elements").split()
# newlst=list(map(int,lst1))
# print(newlst)
# elst=list(filter(lambda x:x%2==0,newlst))
# print("even values are",elst)
# olst=list(filter(lambda x:x%2!=0,newlst))
# print("odd values are",olst)