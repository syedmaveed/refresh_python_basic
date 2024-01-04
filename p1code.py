import random
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:
    print("Enter the choice\n 1:Rock \n 2:Paper \n 3: Scissors \n")
    choice=int(input("Enter the choice : "))
    
    while choice>3 or choice<1:
        choice=int(input("Enter Valid Choice."))
        
    if choice==1:
        choice_name='Rock'
    elif choice==2:
        choice_name='Paper'
    else :
        choice_name='Scissors'
        
    print('Enter User Choice : ',choice_name)
    print("Computer Turn")
    
    comp_choice=random.randint(1,3)
    while comp_choice==choice:
        comp_choice=random.randint(1,3)
    
    if comp_choice==1:
        comp_choice_name='Rock'
    elif comp_choice==2:
        comp_choice_name='Paper'
    else :
        comp_choice_name='Scissors'
    
    print('Computer Choice is : ',comp_choice_name)
    print(choice_name, 'VS' ,comp_choice_name )
    
    
    #CHECK FOR DRAW
    if choice==comp_choice:
        print("Its a DRAW",end="")
        result="DRAW"
    
    if (choice==1 and comp_choice==2):
        print('paper wins =>',end="")
        result='papeR'
    elif (choice==2 and comp_choice==1):
        print('paper wins =>',end="")
        result='Paper'
    
    if (choice==1 and comp_choice==3):
        print('Rock wins =>\n',end= "")
        result='Rock'
    elif (choice==3 and comp_choice==1):
        print('Rock wins =>\n',end= "")
        result='rocK'
        
    if (choice==2 and comp_choice==3):
        print('Scissors wins =>',end="")
        result='scissoR'
    elif (choice==3 and comp_choice==2):
        print('Scissors wins =>',end="")
        result='Rock'
        
    #print results
    
    if result=='DRAW':
        print("ITS A TIE")
    if result==choice_name:
        print("USER WINS")
    else:
        print("COMPUTER WINS")
    
    print("Do you Want to play again? (Y/N)")
    ans=input().lower
    if ans=="n":
        break
print("THANKS FOR PLAYING")
        
        
        
    