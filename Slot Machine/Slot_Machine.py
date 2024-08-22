import time
import sys
import random

random_number1 = random.randint(1,7)
random_number2 = random.randint(1,7)
random_number3 = random.randint(1,7)
spin = random_number1, random_number2, random_number3
print('Welcome\nto\nAllans\nSlot\nMachine')
time.sleep(3)
deposit = int(input('Please enter your amount: $'))
balance = deposit
if deposit > 1:
    print(f'You have added ${deposit}')
    print(f'You currently have a balance of ${balance}')
else: 
    print('You have not added any money')
if balance > 1:
    player_input = input('Would you like to spin?\n1. Yes\n2. No\n')
    if player_input != 2:
        print(f'{random_number1},{random_number2},{random_number3}')
        if spin != random_number1 == random_number2 == random_number3:
            time.sleep(3)
            print('You have won $10')
            win_balance = balance + 10
            print(f'Your new balanace is ${win_balance}')
        else:
            print('You have last $10')
            lose_balance = balance - 10
            print(f'Your new balance is ${lose_balance}')
            if lose_balance > 0:
                play_again = input('Would you like to play again?\n1.Yes\n2.No\n')
                if play_again != 2:
                    print(spin)
                    


