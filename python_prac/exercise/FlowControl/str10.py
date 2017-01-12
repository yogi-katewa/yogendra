str=input("enter string:")
str1=""
lst=[]
lst2=[]
count=0
j=0
for i in str:
     if i != " ":
          str1=str1+i
     else:
          print(str1)
          lst.append(str1)   
          str1=""
lst.append(str1)
lst.sort()
print(lst)
for i in sorted(lst):	
    print(i)
    lst2.append(i)
 #   stack.append(i)
print(lst2)

#for i in lst1:
 #   for j+i
 #     print(i,lst2.count(i))
 #     for i in lst2.count(i):
  #     count++     
    #lst2.remove(i)
for i in lst:
    
    count=0
    s1=i
    for j in lst:
      s2=j
      if s1==s2:
         if s1 in lst2:       
           #if len(lst2)>0:
            lst2.remove(s1)
           #print(s1,"deleted")
            count=count+1
    if count >0:
      print(i,":",count)
    



