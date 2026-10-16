import os
import HangmanStructure as HS
user_word=''
def FriendWithPlay():
    user_word=input('Enter user the Word :').lower()
    os.system('cls')
    hidden_word=[]
    for i in user_word:
        hidden_word+='_'
    print(hidden_word)
    chances=0
    life=True
    while life:
        friend_letter=input('Enter the Friend letter:').lower()
        if friend_letter in user_word:
            for i in range(len(user_word)):
                if (friend_letter==user_word[i]):
                    hidden_word[i]=friend_letter
        else :
            chances+=1
        if chances<=5:
            a='_'
            if a in hidden_word:
                life=True
            else:
                life=False
                print(user_word)
                print('Friend won the Match')
                print('User loss the Match')
            print(HS.hangman[chances])
        else:
            print('User enter word is '+user_word)
            print('Friend loss the Match')
            print('User won the Match')
            life=False  
        print(hidden_word)




