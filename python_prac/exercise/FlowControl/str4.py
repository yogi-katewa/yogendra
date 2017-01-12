str=input("element for lists:")
a=[]
b=""
for i in str:
      if i != " ":
          b=b+i
      else:
          a.append(b)
          b=""	
a.append(b)
print(a)
for ls in a:
       str1=ls
       ln=len(str1)
       print(ln)
       ft=str1[:1]
       print(ft)
       lt=str1[ln-1:]
       print(lt)
       print(str1.replace(ft,lt,1))
       print(str1.replace(lt,ft))
       print("----------")
       print("")            
a.reverse()
print(a)   

