from random import shuffle
from random import randint




######## Open menu



def game():
    choose = True

    while choose:
        
        print("_________________________________\n")
        print(" 1  Start card game")
        print(" 2  Champions score")
        print(" 3  Exit")
        print("___________________________________")


        choose  = input("Choose a number from menu: ")


        if choose  == "1":
            Start_game()
            break
        elif choose  == "2":
            top5 = open_Championsboard()
            Champions_score(top5)
        elif choose  == "3":
            print('See you.')
            break
        else:
            print("You put Out of range integer")
            return game()
            choose = False


##########  build deck


RED="red"
BLACK="black"
YELLOW="yellow"

def cards(colour):
        return (colour,randint(1, 10))

def build_deck():

    deck=[]

    for c in range(10):
            deck.append(cards(RED))
            deck.append(cards(BLACK))
            deck.append(cards(YELLOW))
    return deck

GAMBLER1="1"
GAMBLER2="2"
DRAW="draw"


def Start_game():


########  Allows two players to enter their details, which are then authenticated, to ensure that they are authorised players.


    valid = False   
    while not valid:
          First_player = input("What is the name of the first player?")
          if "@" in First_player:
               print("This sign - @ is not allowed.")
          elif "!" in First_player:
               print("This sign - ! is not allowed.")
          elif "?" in First_player:
               print("This sign - ? is not allowed.")
          elif "$" in First_player:
               print("This sign - $ is not allowed.")    
          else:
               valid = True
               print("Authenticated player")
       

    valid = False

    while not valid:
        Second_player = input("What is the name of the second player?")
        if "@" in Second_player:
            print("This sign - @ is not allowed.")
        elif "!" in Second_player:
            print("This sign - ! is not allowed.")
        elif "?" in Second_player:
            print("This sign - ? is not allowed.")
        elif "$" in Second_player:
            print("This sign - $ is not allowed.")
        elif Second_player == First_player:
            print("First player and second player should not match")
        else:
            valid = True
            print("Authenticated player")


######## Shuffles the 30 cards in the deck.



    deck = build_deck()

    game = True

    while game:

        First_player_cards = []
        Second_player_cards = []

        shuffle(deck)

        round = 1
        
        
######### Allows each player to take a card from the top of the deck. Play continues until there are no cards left in the deck.


        while len(deck) > 0:

            First_total_cards = deck[-1]
            Second_total_cards = deck[-2]

            deck.pop()
            deck.pop()
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            print("ROUND",round)

            show_score(First_total_cards, Second_total_cards)

            champion  = calculate_total(First_total_cards, Second_total_cards)

            if champion == GAMBLER1:
                print("Who win:", First_player)
            elif champion  == GAMBLER2:
                print("Who win:", Second_player)
            else:
                print("Who win: DRAW ")

            if champion  == GAMBLER1:
                First_player_cards.append(First_total_cards)
                First_player_cards.append(Second_total_cards)

            elif champion  == GAMBLER2:
                Second_player_cards.append(First_total_cards)
                Second_player_cards.append(Second_total_cards)

            round += 1

        if len(First_player_cards) > len(Second_player_cards):
            champion  = First_player
            champion_cards = First_player_cards

        elif len(First_player_cards) < len(Second_player_cards):
            champion = Second_player
            champion_cards = Second_player_cards

        else:
            champion=DRAW

        if champion !=DRAW:
               put_champions_into_file(champion,champion_cards)
               
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        print("You win:", champion)
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

        valid = False
        break

    playagain=input("Do you wanna play again?(yes or no)")
    if "yes" in playagain:
        return Start_game() 
    elif "no" in playagain:
        print("See you")
        
        
######## Invariables
COLOUR = 0
NUMBER = 1
    

######## Сalculate total both of players



def calculate_total(card1, card2):

    if card1[COLOUR] == card2[COLOUR]:

        if card1[NUMBER] > card2[NUMBER]:
            return GAMBLER1
        elif card1[NUMBER] < card2[NUMBER]:
            return GAMBLER2
        else:
            return DRAW

    else:

        if card1[COLOUR] == RED:
            return GAMBLER1 if card2[COLOUR] == BLACK else GAMBLER2

        elif card1[COLOUR] == BLACK:
            return GAMBLER1 if card2[COLOUR] == YELLOW else GAMBLER2

        elif card1[COLOUR] == YELLOW:
            return GAMBLER2 if card2[COLOUR] == RED else GAMBLER2



######### Displays round which player wins

def show_score(card1, card2):


    print("_____________________________________\n")   
    print("FIRST PLAYER              SECOND PLAYER")
    print("_______________________________________")

    print("C0L0UR", card1[COLOUR], end = "")
    amount_round=17 - len(card1[COLOUR])
    print(amount_round * " ", end="")
    print("C0L0UR", card2[COLOUR])

    print("NUMBER", card1[NUMBER], end="")
    amount_round = 17 - len(str(card1[NUMBER]))
    print(amount_round * ' ', end="")
    print("NUMBER", card2[NUMBER])
  


##########   Displays the name and quantity of cards of the 5 players with the highest quantity of cards from the external file.



def Champions_score(gamblers):

    print("Champions score")

    for i in range(len(gamblers)):
        score = len(gamblers[i]) - 1
        print(str(i+1), ")", gamblers[i][0], "-", score)

        print(".......................................\n")



########## Lists all of the cards held by the winning player and writes his name and cards to win.txt
def put_champions_into_file (name, cards):

    with open("Championsboard.txt", "a") as Championsboard_file:

        Championsboard_file.write(name)

        for card in cards:

            Championsboard_file.write("\n")
            Championsboard_file.write(card[0])
            Championsboard_file.write(",")
            Championsboard_file.write(str(card[1]))

        Championsboard_file.write("_")

########### Stores the name and quantity of cards of the winning player in an external file.
def open_Championsboard():

    with open("Championsboard.txt", "r") as Championsboard_file:
        gamblers = Championsboard_file.read()

    gamblers = gamblers.split("_")

    for i in range(len(gamblers)):
        gamblers[i] = gamblers[i].split("\n")

    try:
        while gamblers[-1] == [""]:
            gamblers.pop()
    except IndexError:
        pass



############ The players variable now stores a 2d array

    Champions5 = []

    max = 5 if len(gamblers) >= 5 else len(gamblers)

    while len(Champions5) < max:

        index_of_highest = 0

        for i in range(len(gamblers)):

            if len(gamblers[i]) > len(gamblers[index_of_highest]):
                index_of_highest = i

        Champions5.append(gamblers[index_of_highest])
        gamblers.pop(index_of_highest)

    return Champions5

    
if __name__ == "__main__":
    game()
