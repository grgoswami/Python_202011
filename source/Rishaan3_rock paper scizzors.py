player1 = 0
player2 = 0

while player1 < 2 and player2 < 2:
    action1 = str(input("Player 1, What is youre choice? rock - paper - scizzors. : "))
    action2 = str(input("Player 2, What is youre choice? Rock - Paper - Scizzors. : "))

#p1 rock
    if action1 == "rock" and action2 == "rock":
        print("Tie!")
        print("Player 1 your score is ",player1)
        print("Player 2 your score is ",player2)
        
    elif action1 == "rock" and action2 == "paper":
        print("Player 2 Wins!")
        player2 += 1
        print("Player 1 your score is ",player1)
        print("Player 2 your score is your score is ",player2)
        
    elif action1 == "rock" and action2 == "scizzors":
        print("Player 1 Wins!")
        player1 += 1
        print("Player 1 your score is ",player1)
        print("Player 2 your score is your score is ",player2)
#p1 paper
    elif action1 == "paper" and action2 == "paper":
        print("Tie")
        print("Player 1 your score is ",player1)
        print("Player 2 your score is your score is ",player2)
       
    elif action1 == "paper" and action2 == "rock":
        print("Player 1 Wins!")
        player1 += 1
        print("Player 1 your score is ",player1)
        print("Player 2 your score is your score is ",player2)
     
    elif action1 == "paper" and action2 == "scizzors":
        print("Player 2 wins!")
        player2 += 1
        print("Player 1 your score is ",player1)
        print("Player 2 your score is your score is ",player2)
#p1 scizzors
    elif action1 == "scizzors" and action2 == "scizzors":
        print("Tie!")
        print("Player 1 your score is ",player1)
        print("Player 2 your score is your score is ",player2)
      
    elif action1 == "scizzors" and action2 == "rock":
        print("Player 2 wins!")
        player2 += 1
        print("Player 1 your score is ",player1)
        print("Player 2 your score is your score is ",player2)
    
    elif action1 == "scizzors" and action2 == "paper":
        print("Player 1 Wins!")
        player1 += 1
        print("Player 1 your score is ",player1)
        print("Player 2 your score is your score is ",player2)
    

  
if player1 > 1 and player1 < 3:
    print("And the winner is Player 1!!!")
if player2 > 1 and player2 < 3:
    print("And the winner is Player 2!!!")
