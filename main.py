#Game's Cards
cards={
   1: """
┌───────┐
| A     |
|       |
|   ♠   |
|       |
|     A |
└───────┘""",
 2:"""
┌───────┐
| 2     |
|       |
|   ♥   |
|       |
|     2 |
└───────┘""",
3:"""
┌───────┐
| 3     |
|       |
|   ♥   |
|       |
|     3 |
└───────┘""",
4:"""
┌───────┐
| 4     |
|       |
|   ♥   |
|       |
|     4 |
└───────┘
""",
5:"""
┌───────┐
| 5     |
|       |
|   ♥   |
|       |
|     5 |
└───────┘
""",
6:"""
┌───────┐
| 6     |
|       |
|   ♥   |
|       |
|     6 |
└───────┘
""",
7:"""
┌───────┐
| 7     |
|       |
|   ♥   |
|       |
|     7 |
└───────┘
""",
8:"""
┌───────┐
| 8     |
|       |
|   ♥   |
|       |
|     8 |
└───────┘
""",
9:"""
┌───────┐
| 9     |
|       |
|   ♥   |
|       |
|     9 |
└───────┘
""",
10:"""
┌───────┐
| 10    |
|       |
|   ♥   |
|       |
|    10 |
└───────┘
""",
11:"""
┌───────┐
| K     |
|  _T_  |
| |o|o| |
| ` - ' |
| /~~~\ |
| |___| |
|     K |
└───────┘
""",
12:"""
┌───────┐
| Q     |
|  _∧_  |
| (o o) |
|  \\v/  |
|  /|\\  |
| (_|_) |
|     Q |
└───────┘

""",
13:"""
┌───────┐
| J     |
|  /v\\  |
| ( - ) |
|  \\=/  |
|  /|\\  |
| [_|_] |
|     J |
└───────┘
"""}
#Starting Game
#Game's loop
while True:
 import time 
 input("Press enter to start the game......")
 print("Starting game.....")
 time.sleep(3)

 print("""
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗          
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝          
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗            
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝            
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗          
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝          
                                                                        
████████╗ ██████╗                                                       
╚══██╔══╝██╔═══██╗                                                      
   ██║   ██║   ██║                                                      
   ██║   ██║   ██║                                                      
   ██║   ╚██████╔╝                                                      
   ╚═╝    ╚═════╝                                                       
                                                                        
██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                                        
 ██████╗  █████╗ ███╗   ███╗███████╗                                    
██╔════╝ ██╔══██╗████╗ ████║██╔════╝                                    
██║  ███╗███████║██╔████╔██║█████╗                                      
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝                                      
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗                                    
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝                    
        _..-''--'----_.
      ,''.-''| .---/ _`-._
    ,' \\ \\  ;| | ,/ / `-._`-.
  ,' ,',\\ \\( | |// /,-._  / /
  ;.`. `,\\ \\`| |/ / |   )/ /
 / /`_`.\\\\ \\| /_.-.'-''/ /
/ /_|_:.`. \\ |;'`..')  / /
`-._`-._`.`.;`     ,' / /
    `-._`.`/    ,'-._/ /
      : `-/     \\`-.._/
      |  :      ;._ (
      :  |      \\  `\\
       \\        \\    |
        :        :   ;
        |           /
        ;         ,'
       /         /
      /         /
               / 
------------------------------------------------
""")
#Value Fanction
 def get_card_value(card):
  if card>10:
   return 10
  elif card==1:
    return 11
  else:
   return card
#Choose Random Cards
 import random 
 number=[1,2,3,4,5,6,7,8,9,10,11,12,13]
 user_cards=random.choices(number,k=2)
 print("Your cards are loading.....")
 time.sleep(3)
 print(f"Your cards are : {cards[user_cards[0]]} {cards[user_cards[1]]} ")
 computer_cards=random.choices(number,k=2)
 print("Computer's first card is loading......")
 time.sleep(3)

 print(f"Computer's first card is: {cards[computer_cards[0]]} ")

 
 while True:
  confirm=input("Get another card? y/n: ")
  if confirm=="y":
   another_user_card=random.choice(number)
   print("Your another card is loading......")
   time.sleep(3)
   print(f"Your another card is: {cards[another_user_card]}")
   user_cards.append(another_user_card)
  else:
   break
#The Total
 total_user_cards=0
 for card in user_cards:
   total_user_cards+=get_card_value(card)
 if 1 in user_cards:
  ace_value=int(input("choose the value of ace? (1/11): "))
  if ace_value==11:
    total_user_cards+=0
  else:
    total_user_cards-=10
 print("Computer's second card is loading...")
 time.sleep(3)
 print(f"Computer's second card is : {cards[computer_cards[1]]}")
 total_computer_cards=get_card_value(computer_cards[0])+get_card_value(computer_cards[1])
 while total_computer_cards<17:
    another_computer_card=random.choice(number)
    print("Computer's another card is loading.... ")
    time.sleep(3)
    print(f"Computer's another card is: {cards[another_computer_card]}") 
    computer_cards.append(another_computer_card)
    total_computer_cards = 0
    for card in computer_cards:
      total_computer_cards += get_card_value(card)
 if total_computer_cards>21 and 1 in computer_cards:
    total_computer_cards-=10
 else:
   total_computer_cards+=0
 print(f"Your final score is {total_user_cards}")
#The Results  
 print(f"Computer final score is {total_computer_cards}")
 if total_user_cards>21:
   print ("You lose!")
 elif total_computer_cards>21:
   print("You win!")
 elif abs(total_user_cards-21)>abs(total_computer_cards-21):
   print("You lose!")
 elif total_user_cards==total_computer_cards:
     print("Draw!")
 else:
   print("You win!")
 another_turn=input("Do you want to play again? y/n: ")
 if another_turn=="y":
  continue
 else:
   break
 
  
 



   



       
   
  
