num1=input("enter elements for list1:")
num2=input("enter elements for list2:")
a,b,c=[],[],[] #created  empty lists	
for i in num1:
        a.append(i) 
for j in num2:
        b.append(j)    
#s=set(a)-set(b)
#print(s)
for i in a:
    if i in b:
        if i not in c:
           c.append(i)
        #break
print(c)
