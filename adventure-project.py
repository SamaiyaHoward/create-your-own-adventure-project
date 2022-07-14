import sys
def main():
    play = input('Do you want to play my game? yes or no: ')
    if play == 'yes' or play == 'Yes':
     print('ok lets go!')
    else:
        print('Ok have a gret day')
    while play == 'yes':
        charname = input('What is your character name? ')
        print('Hello ', charname, '!')
        readytoplay = input('are you ready to play? Yes or No: ')
        if readytoplay == 'Yes' or readytoplay == 'yes':
            print('QUEST 1: ')
            print('This quest consist of multiple choices, some are good and some are bad.')
        elif readytoplay == 'No' or 'no':
            print('Ok have a great day!')
            backtochar = input('Do you want to change your character? ')
            if backtochar == 'yes' or readytoplay == 'Yes':
                return main()
            else:
                exit = input('Do you want to exit the game? ')
                if exit == 'yes' or exit == 'Yes':
                    sys.exit
                else:
                    return main()
        def quests():
                print('You were traveling at night. You came to a crossroads. One leads to food another leads to a village.')
                Quest1 = input('Left or right | Which road do you choose? ')
                if Quest1 == 'Left' or Quest1 == 'left':
                    print('You found an abandoned village and there was food only sustainable for 2 days!')
                else:
                    print('You have found food and water that would last you for a week')
                print('The Next day has gone by and you decided to go on a hiking trip.')
                print('You have to choose which mountain to take the risky but short or safe but long.')
                Quest2 = input('Which mountain do you choose... Risky or safe? ')
                if Quest2 == 'risky' or Quest2 == 'Risky':
                    print('You have taken the risky path.... You got over the mountain with barely no harm to yourself.')
                else:
                    print('You have taken the safe path which took 20 hours to hike, but you made it safely.')
                print('You looked at your map and saw that you were a couple of miles away from the treasure.')
                print('But there is two structures in front of you. one leads to the treasure and one leads to a trap which you can not get out from.')
                Quest3 = input('Which structure do you go in? The left one or the right one? Choose left or right: ')
                if Quest3 == 'right' or Quest3 == 'Right':
                    print('Congrats you have found the lost treasure of Kahoona!')
                    sys.exit
                else:
                    print('You lose and now you are trapped in this structure for eternity')
                    sys.exit



        quests()
main()
