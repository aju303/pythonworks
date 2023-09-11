#binary search
# def binary_function(lst,key):
#     low=0
#     high=len(lst)-1
#     mid=0
#     while low<=high:
#         mid=(low+high)//2
#         if lst[mid]<key:
#             low=mid+1
#         elif lst[mid]>key:
#             high=mid-1
#         else:
#             return mid  #0,1,2,3,4,56....
#     return -1
# list1=[4,7,8,9]
# key=5
# r=binary_function(list1,key)
# if (r==-1):
#     print("item not found")
# else:
#     print("item found")

#by reading user values
#
# def binary_function(lst,key):
#     low=0
#     high=len(lst)-1
#     mid=0
#     while low<=high:
#         mid=(low+high)//2
#         if lst[mid]<key:
#             low=mid+1
#         elif lst[mid]>key:
#             high=mid-1
#         else:
#             return mid  #0,1,2,3,4,56....
#     return -1
# list1=input("Enter the elements").split()
# print(list1)
# newlst=[]
# for i in list1:
#     newlst.append(int(i))
# print(newlst)
# newlst.sort()
# print("sorted list",newlst)
# key=int(input("Enter the number"))
# r=binary_function(newlst,key)
# if (r==-1):
#     print("item not found")
# else:
#     print("item found")