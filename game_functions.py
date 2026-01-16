import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = poss_values[len(poss_values)//2]   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    higher = False
    if next_val > current_val:
        higher = True
    if user_input == 'h' and higher == True:
        return True
    elif user_input == 'l' and higher == False:
        return True
    else:
        return False
        


# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    letter_pos = []
    
    for i in range(len(board)):
        if letter == word[i]:
            letter_pos.append(i)
    
    if len(letter_pos) == 0:
        print(f"Sorry, {letter} is not in the word")
        return False
    else:
        for i in letter_pos:
            board[i] = letter
           
        print(f"Well done! {letter} is in the word")
        return True


