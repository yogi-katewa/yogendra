import re
lst1,lst2=[],[]
str=input("enter string")
str1=str.lower()
if re.match("^[a-zA-Z ]*$", str):
  for i in str1:
    if i !=" ":
       lst1.append(i)
       lst2.append(i)
  ct,j,count=0,0,0
  for n in lst1:
    count=0  
    while n in lst2:
          count=1
          lst2.remove(n)  
    ct=ct+count
  if ct==26:
    print("pangram")
  else:
    print("not")
else:
    print("!Error---wrong input")
