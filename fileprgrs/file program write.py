#write
# f=open('file 1','w')
# f.write("holmes")

#append
# f=open('file 1','a')
# f.write("holmes")

#writelines
# f=open('file 1','w')
# f.writelines(['first line\n','second line\n','third line'])

#copy content of a file to another file
# f1=open('file 1','r')
# lst=f1.readlines()
# print(lst)
# f2=open('file 2','w')
# f2.writelines(lst)
# f1.close()
# f2.close()

#count no of words in a file
# f1=open('file 1','r')
# data=f1.read()
# print(data)
# words=data.split()
# print(words)
# print(len(words))

#print the count of each word in a file
f1=open('file 1','r')
data=f1.read()
words=data.split()
print(len(words))
dict={}
for i in words:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]=dict[i]+1
print(dict)