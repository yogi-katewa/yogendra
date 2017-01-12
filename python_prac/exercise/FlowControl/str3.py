d={'sape': 4139, 'guido': 4127, 'jack': 4098}
k,v=input("enter new key:"),input("enter value:")
if k in d:
    print("already exist") 
else:
   #print("new key")
   d[k]=v 
   print(d.keys())
