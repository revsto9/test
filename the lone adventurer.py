import os


#OPENING GAME INFO
print('\nWelcome to...\n\n\n\n"THE LONE ADVENTURER"\n\n\n\na game by Anthony Schmidt\n\nC. 2015\n\n\n\n')
os.system('pause')

#ESTABLISH THE PLAYER'S GENDER
UserGender = " "
Counter1 = 0
while Counter1 == 0:
    Counter2 = 0
    os.system('cls')
    UserGender = input("\nWill this adventurer be a man or woman? (M/W)  ").upper()
    while UserGender not in ['M','W']:
        UserGender = input("I did not understand. (M/W)  ").upper()
    if UserGender == 'M':
        UserGender = 'Man'
    else:
        UserGender = 'Woman'
    print("\n\nYou entered: ",UserGender)
    while Counter2 == 0:
        Counter3 = 0
        Continue = input("\nDo you wish to continue with this gender? (Y/N)  ").upper()
        if Continue == 'N':
            Counter2 = 1
        elif Continue == 'Y':
            Counter2 = 1
            Counter1 = 1
        else:
            while Counter3 == 0:
                Continue = input("I did not understand. (Y/N)  ").upper()
                if Continue == 'N':
                    Counter3 = 1
                    Counter2 = 1
                elif Continue == 'Y':
                    Counter3 = 1
                    Counter2 = 1
                    Counter1 = 1
                else:
                    Counter3 = 0
if UserGender == 'Man':
    UserGender = 'his'
else:
    UserGender = 'her'
print("\n\n\n\nConfirmed!\n\n\n\n")
os.system('pause')

#ESTABLISH THE PLAYER'S NAME
UserName = " "
Counter1 = 0
while Counter1 == 0:
    Counter2 = 0
    os.system('cls')
    UserName = input("\nPlease enter the name of your adventurer:  ")
    print("\n\nYou entered: ",UserName)
    while Counter2 == 0:
        Counter3 = 0
        Continue = input("\nDo you wish to continue with this name? (Y/N)  ").upper()
        if Continue == 'N':
            Counter2 = 1
        elif Continue == 'Y':
            Counter2 = 1
            Counter1 = 1
        else:
            while Counter3 == 0:
                Continue = input("I did not understand. (Y/N)  ").upper()
                if Continue == 'N':
                    Counter3 = 1
                    Counter2 = 1
                elif Continue == 'Y':
                    Counter3 = 1
                    Counter2 = 1
                    Counter1 = 1
                else:
                    Counter3 = 0
print("\n\n\n\nGreat! Let's get started\n\n\n\n")
os.system('pause')

#GETTING STARTING WITH THE ADVENTURE
os.system('cls')
print("\n%s is brave soul, but a loner.\n"%UserName)
print("Many years ago, %s decided it would be best to move to the great forest"%UserName)
print("with nothing but %s backpack, a flashlight, and a pocket knife."%UserGender)
print("\nEverything was going well until one very cold evening...\n\n\n\n")
os.system('pause')


#INVENTORY CREATION
ItemFlashlight = 1
ItemKnife = 1
ItemJug = 0
ItemWater = 0
ItemRocks = 0
ItemScienceEquip = 0
EventScientist1 = 0
EventScientist2 = 0
EventScientist3 = 0
GameOver = 0
NewArea = 0

#THIS LOOP EXECUTES UNTIL THE GAME IS COMPLETED
while GameOver == 0:
    #CAMP
    if NewArea == 0:
        #SELECT WHICH DIRECTION TO TRAVEL
        Direction = " "
        Counter1 = 0
        while Counter1 == 0:
            os.system('cls')
            print("\nThere is a mysterious sound coming from the north and an aweful smell")
            print("coming from the east.  To the west a town in the distance, and the lake")
            print("to the south was still as it's ever been.")
            print("\n\nYou're currently at your camp, but this is no time to just sit around!")
            Direction = input("\nIn which direction will you travel? (N,S,E,W)  ").upper()
            while Direction not in ['N','S','E','W']:
                Direction = input("I did not understand. (N,S,E,W)  ").upper()
            #NORTH IS SELETED (MYSTERIOUS SOUND)
            if Direction == 'N':
                NewArea = 1
                Counter1 = 1
            #SOUTH IS SELETED (THE LAKE)
            elif Direction == 'S':
                NewArea = 2
                Counter1 = 1
            #EAST IS SELETED (AWEFUL SMELL)
            elif Direction == 'E':
                NewArea = 3
                Counter1 = 1
            #WEST IS SELETED (TOWN)
            else:
                NewArea = 4
                Counter1 = 1

####################################################################################################

    #ALIENS  (ENTIRE SECTION NEEDS TO BE RE-DONE)
    elif NewArea == 1:
        UserChoice = " "
        Counter1 = 0
        while Counter1 == 0:
            #GENERIC MESSAGE
            os.system('cls')
            print("\nYou come upon an alien spaceship!  Some strange slug-like creatures are")
            print('crawling all around.  One of them warns you to stay away "OR ELSE!!"')
            print("\nThere isn't much to be done here.")
            print("Maybe I should go somewhere else first...")
            #OPTIONS
            UserChoice = input("\n(R)  Return to Camp?").upper()
            while UserChoice not in ['R']:
                UserChoice = input("I did not understand. (R)  ").upper()
            #RETURN TO CAMP
            if UserChoice == 'R':
                Counter1 = 1
                NewArea = 0
            #placeholder for another action
            else:
                Counter1 = 1
                NewArea = 0

####################################################################################################

    #LAKE
    elif NewArea == 2:
        #INITIAL MESSAGE
        os.system('cls')
        print("\nWhat a beautiful lake.  You come here often to relax.")
        print("As usual, the water is so clear you can see to the bottom, but it seems")
        print("something has scared all the fish away.  There isn't a creature in sight.")

        #THIS MESSAGE APPEARS UNTIL YOU OBTAIN THE JUG FROM THE WOMAN IN TOWN
        if ItemJug == 0:
            NewArea = 0
            print("\nThere doesn't appear to be much to do except skip stones.")
            print("That'll pass the time, but won't be of any help.")
            print("Maybe you should go somewhere else first.\n\n\n\n")
            os.system('pause')

        #THIS MESSAGE APPEARS UNTIL YOU FILL THE JUG WITH WATER
        elif ItemWater == 0:
            Counter1 = 0
            print("\nMaybe the calmness of the lake has inspired you or maybe you're just.")
            print("using that brain of yours, but you come up with an idea.")
            print("What if you fill the jug you've acquired with some of the water?")
            while Counter1 == 0:
                Counter2 = 0
                FillJug = input("\nFill the jug? (Y/N)  ").upper()
                if FillJug == 'N':
                    Counter1 = 1
                    NewArea = 0
                    print("\nMaybe this isn't such a good idea after all.")
                    print("You decide it's better to just return to camp.\n\n\n\n")
                    os.system('pause')
                elif FillJug == 'Y':
                    ItemWater = 1
                    Counter1 = 1
                    NewArea = 0
                    print("\nYou wade out to the knee high water and dip in the jug.")
                    print("It quickly fills with crystal clear water and you're on your way!\n\n\n\n")
                    os.system('pause')
                else:
                    while Counter2 == 0:
                        FillJug = input("I did not understand. (Y/N)  ").upper()
                        if FillJug == 'N':
                            Counter2 = 1
                            Counter1 = 1
                            NewArea = 0
                            print("\nMaybe this isn't such a good idea after all.")
                            print("You decide it's better to just return to camp.\n\n\n\n")
                            os.system('pause')
                        elif FillJug == 'Y':
                            ItemWater = 1
                            Counter2 = 1
                            Counter1 = 1
                            NewArea = 0
                            print("\nYou wade out to the knee high water and dip in the jug.")
                            print("It quickly fills with crystal clear water and you're on your way!\n\n\n\n")
                            os.system('pause')
                        else:
                            Counter2 = 0

        #THIS MESSAGE APPEARS UNTIL THE END OF THE GAME
        else:
            NewArea = 0
            print("\nYour jug is still full of water and no more can be added.")
            print("You decide to go back to camp and figure out what to do next.\n\n\n\n")
            os.system('pause')


####################################################################################################

    #SWAMP
    elif NewArea == 3:
        #INITIAL MESSAGE
        os.system('cls')
        print("\nThe swamp.  It's always been by the camp but it's never smelled so bad!")
        print("It's likely the recent disturbance has caused a reaction with the muck.")

        #THIS MESSAGE APPEARS UNTIL YOU RETURN THE LAB EQUIPMENT TO THE SCIENTIST
        if EventScientist2 == 0:
            NewArea = 0
            print("\nIt's quite dark and there doesn't appear to be anything to do.")
            print("Maybe you should go somewhere else first.\n\n\n\n")
            os.system('pause')

        #THIS MESSAGE APPEARS UNTIL YOU FIND THE ROCKS
        elif ItemRocks == 0:
            Counter1 = 0
            print("\nThe scientist says there are special rocks in the area.")
            print("You spend a few minutes debating the scietist's sanity.")
            while Counter1 == 0:
                Counter2 = 0
                SearchRocks = input("\nDo you want to look for the rocks? (Y/N)  ").upper()
                if SearchRocks == 'N':
                    Counter1 = 1
                    NewArea = 0
                    print("\nChecking for rocks in a swamp doesn't sound like much fun.")
                    print("You decide it's better to just return to camp.\n\n\n\n")
                    os.system('pause')
                elif SearchRocks == 'Y':
                    ItemRocks = 1
                    Counter1 = 1
                    NewArea = 0
                    print('\nWith your flashlight in hand you search for "sky rocks" in the muck.')
                    print("After hours of looking and a bit of luck you manage to locate a few.\n\n\n\n")
                    os.system('pause')
                else:
                    while Counter2 == 0:
                        SearchRocks = input("I did not understand. (Y/N)  ").upper()
                        if SearchRocks == 'N':
                            Counter2 = 1
                            Counter1 = 1
                            NewArea = 0
                            print("\nChecking for rocks in a swamp doesn't sound like much fun.")
                            print("You decide it's better to just return to camp.\n\n\n\n")
                            os.system('pause')
                        elif SearchRocks == 'Y':
                            ItemRocks = 1
                            Counter2 = 1
                            Counter1 = 1
                            NewArea = 0
                            print('\nWith your flashlight in hand you search for "sky rocks" in the muck.')
                            print("After hours of looking and a bit of luck you manage to locate a few.\n\n\n\n")
                            os.system('pause')
                        else:
                            Counter2 = 0

        #THIS MESSAGE APPEARS UNTIL YOU TRADE THE FLASHLIGHT TO THE WOMAN
        elif ItemFlashlight == 1:
            NewArea = 0
            print("\nThere isn't much else to do here.  WIth the rocks in your possession")
            print("you decide to just head back to camp.\n\n\n\n")
            os.system('pause')

        #THIS MESSAGE APPEARS UNTIL THE END OF THE GAME
        else:
            NewArea = 0
            print("\nYou've already found the rocks.")
            print("Without your flashlight you're only asking for trouble.")
            print("\nBest to return to camp.\n\n\n\n")
            os.system('pause')

####################################################################################################

    #TOWN
    elif NewArea == 4:
        UserChoice = " "
        Counter1 = 0
        while Counter1 == 0:

            #INITIAL MESSAGE
            os.system('cls')
            print("\nA small town with only a few residents, all of which are strangers.")
            print("You get a lot of curious looks but nobody says a word.\n")
            print("To the left you notice some thugs leaning against an old school house.")
            print("To the right is a scientist that seems pretty upset.")
            print("On the far end of town is a woman selling some goods.")
            print("")

            #OPTIONS
            print("\n(C)  Return to Camp?\n(T)  Approach the thugs?")
            UserChoice = input("(W)  Barter with the woman?\n(S)  Speak with the scientist?  ").upper()
            while UserChoice not in ['C','T','W','S']:
                UserChoice = input("I did not understand. (C/T/W/S only)  ").upper()

#---------------------------------------------------------------------------------------------------

            #RETURN TO CAMP
            if UserChoice == 'C':
                Counter1 = 1
                NewArea = 0

#---------------------------------------------------------------------------------------------------

            #THUGS
            elif UserChoice == 'T':
                os.system('cls')

                #THIS MESSAGE APPEARS UNTIL YOU SPEAK WITH THE SCIENTIST
                if EventScientist1 == 0:
                    print("\nYou approach the thugs but they aren't in the mood to chat.")
                    print("You quickly realize it's not worth the trouble at this time.\n\n\n\n")
                    os.system('pause')

                #THIS MESSAGE APPEARS AFTER TALKING WITH THE SCIENTIST UNTIL THE TRADE IS ACCEPTED
                elif ItemKnife == 1:
                    Counter1 = 0
                    print("\nYou approach the thugs and they seem very angry.")
                    print("They warn that you better have a good reason for bothering them.")
                    print("\nYou ask about the scientists things and demand they be returned.")
                    print("It looks like they're ready for a fight, but once they see")
                    print("your knife they offer a trade.")
                    while Counter1 == 0:
                        Counter2 = 0
                        TradeKnife = input("\nDo you want to trade the knife for the lab equipment? (Y/N)  ").upper()
                        if TradeKnife == 'N':
                            Counter1 = 1
                            print("\nYou'll keep the knife for now.\n\n\n\n")
                            os.system('pause')
                        elif TradeKnife == 'Y':
                            ItemKnife = 0
                            ItemScienceEquip = 1
                            Counter1 = 1
                            print("\nTrade complete!\n\n\n\n")
                            os.system('pause')
                        else:
                            while Counter2 == 0:
                                TradeKnife = input("I did not understand. (Y/N)  ").upper()
                                if TradeKnife == 'N':
                                    Counter2 = 1
                                    Counter1 = 1
                                    print("\nYou'll keep the knife for now.\n\n\n\n")
                                    os.system('pause')
                                elif TradeKnife == 'Y':
                                    ItemKnife = 0
                                    ItemScienceEquip = 1
                                    Counter2 = 1
                                    Counter1 = 1
                                    print("\nTrade complete!\n\n\n\n")
                                    os.system('pause')
                                else:
                                    Counter2 = 0

                #THIS MESSAGE APPEARS UNTIL THE END OF THE GAME
                else:
                    print("\nAs you approach the thugs and they thank you for the knife")
                    print("but are quick to tell you they have no other business with you.\n\n\n\n")
                    os.system('pause')

#---------------------------------------------------------------------------------------------------

            #WOMAN
            elif UserChoice == 'W':
                os.system('cls')

                #THIS MESSAGE APPEARS UNTIL YOU HAVE THE JUG
                if ItemJug == 0:
                    print("\nYou approach the woman and engage her in conversation.  She tells you she")
                    print("only has a water jug for sale and you quickly inform her you have no money.")
                    print("She offers to trade you for your flashlight.")

                    #THIS MESSAGE APPEARS UNTIL YOU'VE FOUND THE ROCKS IN THE SWAMP
                    if ItemRocks == 0:
                        print("\nYou'd better hold onto it for now.  You just may need it for something.\n\n\n\n")
                        os.system('pause')

                    #THIS MESSAGE APPEARS AFTER YOU HAVE THE ROCKS
                    else:
                        Counter1 = 0
                        while Counter1 == 0:
                            Counter2 = 0
                            TradeJug = input("\nWill you trade? (Y/N)  ").upper()
                            if TradeJug == 'N':
                                Counter1 = 1
                                print("\nYou like your flashlight and you're not ready to part with it.\n\n\n\n")
                                os.system('pause')
                            elif TradeJug == 'Y':
                                ItemFlashlight = 0
                                ItemJug = 1
                                Counter1 = 1
                                print("\nTrade complete!\n\n\n\n")
                                os.system('pause')
                            else:
                                while Counter2 == 0:
                                    TradeJug = input("I did not understand. (Y/N)  ").upper()
                                    if TradeJug == 'N':
                                        Counter2 = 1
                                        Counter1 = 1
                                        print("\nYou like your flashlight and you're not ready to part with it.\n\n\n\n")
                                        os.system('pause')
                                    elif TradeJug == 'Y':
                                        ItemFlashlight = 0
                                        ItemJug = 1
                                        Counter2 = 1
                                        Counter1 = 1
                                        print("\nTrade complete!\n\n\n\n")
                                        os.system('pause')
                                    else:
                                        Counter2 = 0

                #THIS MESSAGE APPEARS UNTIL THE END OF THE GAME
                else:
                    print("\nThe woman reminds you she only had a jug to sell.")
                    print("With the jug in your possession you walk away.\n\n\n\n")
                    os.system('pause')

#---------------------------------------------------------------------------------------------------

            #SCIENTIST
            else:
                os.system('cls')

                #THIS MESSAGE APPEARS UNTIL THE TRADE WITH THE THUGS IS COMPLETE
                if ItemScienceEquip == 0:
                    EventScientist1 = 1
                    print("\nYou approach the scientist.  He's so upset he won't even talk with you.")
                    print("He mentions something about his lab equipment being taken by thugs.")
                    print("\nMaybe there's something you can do to help him.\n\n\n\n")
                    os.system('pause')

                #THIS MESSAGE APPEARS ONLY ONCE, AFTER THE TRADE IS COMPLETE
                elif EventScientist2 == 0:
                    EventScientist2 = 1
                    print("\nYou approach the scientist and tell him you have his equipment.")
                    print("He's overjoyed and begins talking your face off.")
                    print("It seems he needs you do something for him.")
                    print("\nHe explains that in the swamp are some rocks that recently fell from the skies.")
                    print("Bring him some samples and you'll get a reward.\n\n\n\n")
                    os.system('pause')

                #THIS MESSAGE APPEARS UNTIL THE ROCKS HAVE BEEN OBTAINED
                elif ItemRocks == 0:
                    print("\nYou appraoch the scientist and he quickly reminds you that")
                    print("he wants those rocks from the swamp.")
                    print("\nYou'd better do as he asks if you expect any more help from him.\n\n\n\n")
                    os.system('pause')

                #THIS MESSAGE APPEARS UNTIL THE TRADE IS COMPLETE
                elif EventScientist3 == 0:
                    Counter1 = 0
                    while Counter1 == 0:
                        Counter2 = 0
                        TradeRocks = input("\nThe scientist is eagerly waiting on the rocks.  Will you trade? (Y/N)  ").upper()
                        if TradeRocks == 'N':
                            Counter1 = 1
                            print("\nYou're not ready to trade just yet.\n\n\n\n")
                            os.system('pause')
                        elif TradeRocks == 'Y':
                            EventScientist3 = 1
                            ItemSalt = 1
                            Counter1 = 1
                            print("\nTrade complete!\n\n\n\n")
                            os.system('pause')
                        else:
                            while Counter2 == 0:
                                TradeRocks = input("I did not understand. (Y/N)  ").upper()
                                if TradeRocks == 'N':
                                    Counter2 = 1
                                    Counter1 = 1
                                    print("\nYou're not ready to trade just yet.\n\n\n\n")
                                    os.system('pause')
                                elif TradeRocks == 'Y':
                                    EventScientist3 = 1
                                    ItemSalt = 1
                                    Counter2 = 1
                                    Counter1 = 1
                                    print("\nTrade complete!\n\n\n\n")
                                    os.system('pause')
                                else:
                                    Counter2 = 0

                #THIS MESSAGE APPEARS UNTIL THE END OF THE GAME
                else:
                    print("\nThe scientist is very grateful for all of your help however")
                    print("has nothing further to discuss with you.\n\n\n\n")
                    os.system('pause')

####################################################################################################
