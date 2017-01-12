n1=int(input("enter range:"))	
for n in range(2,n1):
        flag=1
        for x in range(2,n):
            if n % x == 0:
                flag=0
                print(n, 'equals', x, '*', n//x)
                break
            elif n>3:
                 if n%3>0: 
                      print(n,"prime number")
                      break
            else:
                 print(x,"prime number")
