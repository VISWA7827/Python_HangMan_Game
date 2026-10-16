import os
import random
import HangmanStructure as HS
import Words as W

computer_word = ''
def PlayWithComputer():
    print('Enter the Computer Word')
    computer_word=random.choice(W.words)
    os.system('cls')
    hidden_word=[]
    for i in computer_word:
        hidden_word+='_'
    print(hidden_word)
    chances=0
    life=True
    while life:
        user_letter=input('Enter the  user letter:').lower()
        if user_letter in computer_word:
            for i in range(len(computer_word)):
                if (user_letter==computer_word[i]):
                    hidden_word[i]=user_letter
        else :
            chances+=1
        if chances<=5:
            a='_'
            if a in hidden_word:
                life=True
            else:
                print('user won the Match')
                print('computer loss the match')
                life=False
                print('computer entered word is :'+computer_word)
            print(HS.hangman[chances])
        else:
            print('User loss the Match')
            print('computer won the match')
            life=False
            print('computer entered word is :'+computer_word)
        print(hidden_word)







