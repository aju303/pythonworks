#map function

# lst=['3','4','5','6']
# newlst=list(map(int,lst))
# print(newlst)

#lst1=['apple','orange','banana','jackfruit']
#need to find length
#newlst=list(map(len,lst1))
# print(newlst)

#square of a list
#map(fun,sequence)
# def square(n):
#     return n*n
#
# lst=[3,4,5,6]
# nwlst=list(map(square,lst))
# print(nwlst)


# def sum(n):
#     return n+10
#
# lst=[3,4,5,6]
# nwlst=list(map(sum,lst))
# print(nwlst)

#map functon using lambda
# lst=[3,4,5,6]
# newlst=list(map(lambda n:n+10,lst))
# print(newlst)

#square of a number using map&lambda

# lst=[3,4,5,6]
# newlst=list(map(lambda n:n*n,lst))
# print(newlst)

#changing to caps
# lst=['apple','orange','mango']
# newlst=list(map(lambda i:i.upper(),lst))
# print(newlst)

#list by list
lst=['apple','orange','mango']
newlst=list(map(list,lst))
print(newlst)