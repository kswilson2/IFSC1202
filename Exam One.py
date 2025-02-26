from random import randint
username = input("What is your name: ")
userscore = 0
compscore = 0 
while userscore <=30 and compscore <= 30:
    enter = input("Press enter to roll the die " + username)
    userroll = randint(1,6)
    print(f"{username} rolled a {userroll}")
    comproll = randint(1,6)
    print (f"Computer rolled a {comproll}")
    if userroll == 1:
       userscore = 0
       print (f"Oops {username} has to start over")
    else: 
       userscore += userroll
    if comproll == 1:
       compscore = 0
       print (f"Oops Computer has to start over")
    else: 
       compscore += comproll
    print (f"{username}'s Score: {userscore}")
    print (f"Computer's Score: {compscore}")
    print ("#"*20)   
if userscore > compscore:
   print (f"{username} Wins")
else:
   print ("Computer Wins")   