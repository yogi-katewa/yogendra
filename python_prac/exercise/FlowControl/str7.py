con="y"
while con=='y':
   print("you have on;y three choices--> 1.rock 2.paper 3.scissors")
   play1=input("Enter value value for player1: ")
   play2=input("Enter value value for player2: ")
   play1=play1.lower() 
   play1=play1.lower()
   if play1=="rock" and play2=="scissors":
          print("player1")
          con="n"
   elif play1=="scissors" and play2=="rock":
          print("player2")
          con="n"
   elif play1=="paper" and play2=="rock":
          print("player1")
          con="n"
   elif play1=="rock" and play2=="paper":
          print("player2")
          con="n"
   elif play1=="scissors" and play2=="paper":
          print("player1")
          con="n"
   elif play1=="paper" and play2=="scissors":
          print("player2")
          con="n"
   elif play1==play2:
          print("It's a tie")
          con="n"
   else:
          print("you have inputed wrong value")
            
   
   print("you want to continue:")
   con=input("enter y to continu:")

   
