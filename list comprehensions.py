#list comprehensions

#to find square
# lst=[1,2,3,4,]
# newlst=[x*x for x in lst]
# print(newlst)

#to add 10
# lst=[1,2,3,4,]
# newlst=[x+10 for x in lst]
# print(newlst)

#to find square of first 10 numbers
# newlst=[x*x for x in range(1,11)]
# print(newlst)

#to find square off odd num up to 10

# newlst=[x*x for x in range(1,11,2)]
# print(newlst)

# to find length
# lst=['rose','lilly','lotus','daisy']
# newlst=[len(x) for x in lst]
# print(newlst)

#to print those who have len5
# lst=['rose','lilly','lotus','daisy']
# newlst=[x for x in lst if len(x)==5]    #[exp for iter_var in seq if cond]
# print(newlst)

#not printing lilly
# lst=['rose','lilly','lotus','daisy']
# newlst=[x for x in lst if x!='lilly']
# print(newlst)

#to print those with 'o'
# lst=['rose','lilly','lotus','daisy']
# newlst=[x for x in lst if 'o' in x]
# print(newlst)

#when if else comes sthere will be a small syntax change
# lst=[2,4,6,7]
# newlst=['even' if x%2==0 else 'odd' for x in lst] #true_stnt-if cond-else-false stnt-for iter_var in seq]
# print(newlst)

#print those have 'o' & others with flowers
# lst=['rose','lilly','lotus','daisy']
# newlst=[x if 'o' in x else 'flower' for x in lst]
# print(newlst)