import random as r
from replit import clear
logo = '''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/              
'''
def give_card():
    '''gives a rendom card from card list'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return r.choice(cards)

def calculate_sum(cards):
    if(sum(cards) == 21 and len(cards) == 2):
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score,computer_score):
    if user_score == computer_score:
        return ("its a draw")
    elif computer_score == 0:
        return "Lose, opponent has a black jack"
    elif user_score == 0:
        return "Win with a black jack"
    elif user_score > 21:
        return "you went over. You Lost"
    elif computer_score > 21:
        return "Opponent went over, You Won"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You Lose"



def play_game():
    clear()
    print(logo)
    computer_cards = []
    user_cards = []
    for i in range(2):
        user_cards.append(give_card())
        computer_cards.append(give_card())
        is_game_over = False
    while not is_game_over:
        user_score = calculate_sum(user_cards)
        comp_score = calculate_sum(computer_cards)
        print(f"your cards:{user_cards}, current score {user_score}")
        print(f"computer's first card:{computer_cards[0]}")
        if user_score > 21 or comp_score == 0 or user_score == 0:
            is_game_over = True
        else:
            user_deal = input("enter y to deal a new card: ")
            if user_deal == 'y':
                user_cards.append(give_card())
            else:
                is_game_over = True
    while comp_score != 0 and comp_score < 17:
        computer_cards.append(give_card())
        comp_score = calculate_sum(computer_cards)
    print(f"your final hand {user_cards}\n computer final hand {computer_cards}")
    print(compare(user_score,comp_score))
    if input("wanna have another try, enter y : ") == 'y':
        play_game()
    

play_game()



    