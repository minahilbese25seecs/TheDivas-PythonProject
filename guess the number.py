import random
while True:
 target=random.randint(1,49)
 print("you have 5 tries to guess the magic number\n")
 win=False
 for attempt in range(1,6):
  guess =int(input("Guess the magic number:"))
  if guess<target:
   print("Your guess is lower.Try again")
  elif guess>target:
   print("Your guess is higher.Try again.")
  else:
   number=int(attempt)
   print("Your guess is correct congratulations")
   print("it took you",number,"attempts")
   win=True
   break
 win==False
 print("You have lost.")
 print("the magic number was",target)
 play_again=input("Do you want to play again?:\n").lower()
 if play_again!="yes":
    print("thank you for playing")
    break





  
  
