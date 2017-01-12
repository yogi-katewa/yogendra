str=input("enter string:")
i=str[0:1]
b=i
for a in str[1:]:
     if a!=i:       
        b=b+a
     else:
        b=b+'$'
print(b)
