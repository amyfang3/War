import random
class Card:

    # Initializes a card with a suit and rank
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    # Displays the card
    def __str__(self):
        
        return(self.rank + self.suit)

class Deck:

    suit = ["C", "D", "H", "S"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    # Creates a list of 52 Card objects
    def __init__(self):
        self.cardList = []

        for i in range(len(Deck.suit)):
            for j in range(len(Deck.rank)):
                card = Card(Deck.rank[j], Deck.suit[i])
                self.cardList.append(card)
            
    # Displays all the cards
    def __str__(self):
        string = ""
        
        for i in range(len(self.cardList)):
            if i % 13 == 0 and i != 0:
                string += "\n" + '{:>4}'.format(str(self.cardList[i]))
            else:
                string += '{:>4}'.format(str(self.cardList[i]))

        return string
                                      
    # Shuffles the deck
    def shuffle(self):
        return(random.shuffle(self.cardList))

    # Adds one card to a player's hand
    def dealOne(self, player):
        card = self.cardList[0]
        player.hand.append(card)
        player.handTotal += 1
        self.cardList = self.cardList[1:]

class Player:

    # Initialies player's hand with no cards
    def __init__(self):
        self.hand = []
        self.handTotal = 0

    # Displays the player's hand
    def __str__(self):
        string = ""
        for i in range(self.handTotal):
            if i % 13 == 0 and i != 0:
                string += "\n" + '{:>4}'.format(str(self.hand[i]))
            else:
                string += '{:>4}'.format(str(self.hand[i]))

        return string

    # Returns true if player still has cards
    def handNotEmpty(self):
        return (self.handTotal != 0)
            
# Play the game
def playGame(cardDeck, player1, player2):

    # Initialize round number
    roundNum = 1
    gameOver = False

    # While the game is playing
    while not gameOver:
        print("ROUND " + str(roundNum) + ":")
        print("Player 1 plays: " + str(player1.hand[0]))
        print("Player 2 plays: " + str(player2.hand[0]))
        print()

        # In case of war
        if player1.hand[0].rank == player2.hand[0].rank:
            print("War starts: " + str(player1.hand[0]) + " = " + str(player2.hand[0]))
            war = True
            stack1 = []
            stack2 = []

            while war: 
                # In case war occurs, but one of the players doesn't have enough cards
                if player1.handTotal < 5 or player2.handTotal < 5:
                    player1.hand = player1.hand[1:]
                    player2.hand = player2.hand[1:]
                    player1.handTotal = len(player1.hand)
                    player2.handTotal = len(player2.hand)
                    gameOver = True
                    break
                    
                # If war occurs and both players have enough cards
                # Display the next 3 face down cards
                for i in range(1, 4):
                    print("Player 1 puts " + str(player1.hand[i]) + " face down")
                    print("Player 2 puts " + str(player2.hand[i]) + " face down")

                # Adds each player's cards to stacks and removes them from their hand
                for i in range(4):
                    stack1.append(player1.hand[i])
                for i in range(4):
                    stack2.append(player2.hand[i])

                player1.hand = player1.hand[4:]
                player2.hand = player2.hand[4:]
                player1.handTotal = len(player1.hand)
                player2.handTotal = len(player2.hand)

                # Determining card
                print("Player 1 puts " + str(player1.hand[0]) + " face up")
                print("Player 2 puts " + str(player2.hand[0]) + " face up")
                print()

                # If war happens again
                if player1.hand[0].rank == player2.hand[0].rank:
                    print("War starts: " + str(player1.hand[0]) + " = " + str(player2.hand[0]))                    
                    continue
                    
                # If player 1 wins
                if didPlayer1Win(player1.hand[0], player2.hand[0]):
                    print("Player 1 wins round " + str(roundNum) + ": " + str(player1.hand[0]) + " > " + str(player2.hand[0]))

                    # Append the cards of both players to the winning player
                    player1.hand += stack1
                    player1.hand.append(player1.hand[0])
                    player1.hand += stack2
                    player1.hand.append(player2.hand[0])
                    
                    # Recalibrate each player's deck, hand total, and stacks
                    player1.hand = player1.hand[1:]
                    player1.handTotal = len(player1.hand)
                    player2.hand = player2.hand[1:]
                    player2.handTotal = len(player2.hand)
                    stack1 = []
                    stack2 = []
                    break

                # If player 2 wins
                else:
                    print("Player 2 wins round " + str(roundNum) + ": " + str(player2.hand[0]) + " > " + str(player1.hand[0]))

                    # Append the cards of both players
                    player2.hand += stack1
                    player2.hand.append(player1.hand[0])
                    player2.hand += stack2
                    player2.hand.append(player2.hand[0])

                    # Recalibrate each player's deck, hand total, and stacks
                    player2.hand = player2.hand[1:]
                    player2.handTotal = len(player2.hand)
                    player1.hand = player1.hand[1:]
                    player1.handTotal = len(player1.hand)
                    stack1 = []
                    stack2 = []
                    break
    
        # No war, if player 1 wins the round
        elif didPlayer1Win(player1.hand[0], player2.hand[0]):
            print("Player 1 wins round " + str(roundNum) + ": " + str(player1.hand[0]) + " > " + str(player2.hand[0]))
            player1.hand.append(player1.hand[0])
            player1.hand.append(player2.hand[0])
            player1.hand = player1.hand[1:]
            player1.handTotal = len(player1.hand)
            player2.hand = player2.hand[1:]
            player2.handTotal = len(player2.hand)

        # No war,if player 2 wins the round
        else: 
            print("Player 2 wins round " + str(roundNum) + ": " + str(player2.hand[0]) + " > " + str(player1.hand[0]))
            player2.hand.append(player1.hand[0])
            player2.hand.append(player2.hand[0])
            player2.hand = player2.hand[1:]
            player2.handTotal = len(player2.hand)
            player1.hand = player1.hand[1:]
            player1.handTotal = len(player1.hand)

        # Displays the hands of both players
        print()
        print("Player 1 now has", player1.handTotal, "card(s) in hand:")
        print(player1)
        print("Player 2 now has", player2.handTotal, "card(s) in hand:")
        print(player2)
        print()
        print()

        # Game over condition
        if player1.handTotal == 0 or player2.handTotal == 0:
            gameOver = True

        # Increment the round number
        roundNum += 1      
        
# Determines outcome of single battle
def didPlayer1Win(card1, card2):
    # If player 2 plays an Ace and player 1 does not
    if card2.rank == "A" and card1.rank != "A":
        return False

    # If the player 2's card is a 10 while player 1's card is 2-9 (player 2 wins)
    elif card2.rank == "10" and (card1.rank >= "2" and card1.rank <= "9"):
        return False

    # If the player 1's card is a 10 while player 2's card is 2-9 (player 1 wins)
    elif (card2.rank >= "2" and card2.rank <= "9") and card1.rank == "10":
        return True

    # If player 1 plays a higher card or plays an ace
    elif (card1.rank > card2.rank) or (card1.rank == "A" and card2.rank != "A"):
        return True

    # If player 2 plays a higher card
    else:
        return False
    
def main():

    # Creates a deck of 52 cards and displays it
    cardDeck = Deck()
    print("Initial deck:")
    print(cardDeck)
    print()

    # Shuffles the deck
    random.seed(15)
    cardDeck.shuffle()
    print("Shuffled deck:")
    print(cardDeck)
    print()

    # Creates the two players
    player1 = Player()
    player2 = Player()

    # Deals 26 cards to each player, one at a time, alternating between players
    for i in range(26):
        cardDeck.dealOne(player1)
        cardDeck.dealOne(player2)

    # Displays the players hands
    print("Initial hands:")
    print("Player 1:")
    print(player1)
    print()
    print("Player 2:")
    print(player2)
    print()

    # Play the game
    playGame(cardDeck, player1, player2)

    # Determines the winner
    if player1.handNotEmpty():
        print("Game over. Player 1 wins!")
    else:
        print("Game over. Player 2 wins!")

    # Prints the final hands
    print ("\n\nFinal hands:")    
    print ("Player 1:   ")
    print (player1)                 
    print ("\nPlayer 2:")
    print (player2)  

main()
