def fun():
      for i in range(n):
         print(i)
      yield 1
 
n=int(input("enter number :"))
g=fun()
next(g)
