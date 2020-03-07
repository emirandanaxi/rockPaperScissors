'''
Created on Feb 1, 2020

@author: ITAUser

'''

keepPlaying = True
while (keepPlaying):
        print("Welcome to R, P, & S! The rules are best out of 3. Press 'q' to quit! And 1 for Rock, 2 for Paper and 3 for Scissor")
        import random
        userpoints = 0
        computerpoints = 0
        while (userpoints < 3 and computerpoints < 3):
            r = random.randint(1, 2+1)        
            userinput = input("Rock, Paper, or Scissor: ")
            if ("q" == userinput):
                keepPlaying = False
                
            #draw
            elif ("rock" == userinput and 1 == r) or ("scissors" == userinput and 3 == r) or ("paper" == userinput and 2 == r):
                    print("Draw!")
                    print ("Computer's Score: " , + computerpoints)
                    print("Your Score: ", + userpoints)
                    
            #computer wins
            elif ("rock" == userinput and 2 == r) or ("scissors" == userinput and 1 == r) or ("paper" == userinput and 3 == r):
                    print("Computer wins!")
                    computerpoints = computerpoints + 1
                    print("Computer's Score: ", + computerpoints)
                    print("Your Score: ", + userpoints)
            #human wins
            elif ("rock" == userinput and 3 == r) or ("scissors" == userinput and 2 == r) or ("paper" == userinput and 1 == r):
                    print("You win!")
                    userpoints = userpoints + 1
                    print("Computer's Score: ", + computerpoints)
                    print("Your Score: ", + userpoints)
                
            else:
                    print("You got this!")
            if (userpoints == 3): 
                    print("Yay!! You did it!")
            if (computerpoints == 3):
                    print(" Sorry, you lost :(")
                    
            print("Computer's score: ", + computerpoints, "Your score: ", + userpoints)
               
            
#r = 1
#p = 2
#s = 3
