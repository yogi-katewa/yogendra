import re
str=input("enter [] brackets: ")
if re.match("^[[] ]*$", str):
   ct=0
   for i in str:
       if i=='[':
          ct=ct+1
       else:
          ct=ct-1
   if ct<0:
      print("wrong input")   
   else:
      print("right closing:")    
else:
   print("only square brackets")
