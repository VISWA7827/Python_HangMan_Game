#Hangman game
import PlayWithFriend as PF
import FriendWithPlay as FP
import ComputerWithPlay as CP
import PlayWithComputer as PC
print('!!!!!Welcome to the Hangman Game!!!!!')
choice='yes'
while choice=="yes":
    print('1.Play with Friend')
    print('2.Friend with Play')
    print('3.Play with Computer')
    print('4.Computer with play')
    user_choice=int(input('Enter the Your Choice :'))
    if (user_choice>4 or user_choice<0):
        print('Ohhhh!! Invalid Choice!!!!')
    elif user_choice==1:
        PF.PlayWithFriend()
    elif user_choice==2:
        FP.FriendWithPlay()
    elif user_choice==3:
        PC.PlayWithComputer()
    elif user_choice==4:
        CP.ComputerWithPlay()
    choice=input(' if you want play(yes/no) :')
print('successfully completed the Hangman Game')