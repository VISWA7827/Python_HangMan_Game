import os
import random
import HangmanStructure as HS
import Words as W

user_word = ''
def ComputerWithPlay():
    user_word=input('Enter the user word :').lower()
    os.system('cls')
    hidden_word=[]
    for i in user_word:
        hidden_word+='_'
    print(hidden_word)
    chances=0
    life=True
    while life:
        print('Enter the computer letter:')
        computer_letter=random.choice(W.letters)
        print(computer_letter)
        if computer_letter in user_word:
            for i in range(len(user_word)):
                if (computer_letter==user_word[i]):
                    hidden_word[i]=computer_letter
        else :
            chances+=1
        if chances<=5:
            a='_'
            if a in hidden_word:
                life=True
            else:
                print('computer won the Match')
                print('user loss the match')
                life=False
                print('User entered word is :'+user_word)
            print(HS.hangman[chances])
        else:
            print('User won the Match')
            print('computer loss the match')
            life=False
            print('User entered word is :'+user_word)
        print(hidden_word)