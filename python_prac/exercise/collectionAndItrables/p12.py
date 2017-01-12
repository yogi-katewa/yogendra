in_lst=input("enter list items: ")
str1=''
lst1=[]
for str in in_lst:
    if str!= ' ':
       str1=str1+str
    else:
       lst1.append(str1)
       str1=''

ot_lst=[]
print(lst1)
print("enter 1 for for loop 2 for list coperhensive:")
ch=int(input("enter choice: "))
if ch==1:
    for ele in lst1:
        n1=len(ele)
        print(ele,n1)
elif ch==2:
    print([(ele,len(ele)) for ele in lst1])
        #ot_lst.append(len(ele))
#print(ot_lst)    
         
