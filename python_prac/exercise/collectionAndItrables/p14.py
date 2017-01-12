dict={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
in_lst=input("input message: ")
str1=''
lst1=[]
for str in in_lst:
    if str!= ' ':
       str1=str1+str
    else:
       lst1.append(str1)
       str1=''
lst1.append(str1)
print([dict[ele] for ele in lst1 if ele in dict])
