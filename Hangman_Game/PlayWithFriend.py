import os
import HangmanStructure as HS
friend_word=''
def PlayWithFriend():
    friend_word=input('Enter the Friend Word :').lower()
    os.system('cls')
    hidden_word=[]
    for i in friend_word:
        hidden_word+='_'
    print(hidden_word)
    chances=0
    life=True
    while life:
        user_letter=input('Enter the  user letter:').lower()
        if user_letter in friend_word:
            for i in range(len(friend_word)):
                if (user_letter==friend_word[i]):
                    hidden_word[i]=user_letter
        else :
            chances+=1
        if chances<=5:
            a='_'
            if a in hidden_word:
                life=True
            else:
                print('User won the Match')
                print('Friend loss the match')
                life=False
                print('friend entered word is :'+friend_word)
            print(HS.hangman[chances])
        else:
            print('User loss  the Match')
            print('Friend won the match')
            life=False
            print('Friend entered word is :'+friend_word)
        print(hidden_word)
