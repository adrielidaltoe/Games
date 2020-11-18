#!/usr/bin/env python
# coding: utf-8

# ### BlackJack
# 
# The rules programmed in this code:
# 
# 1. When player has a black Jack is paid 3/2 of the bet.
# 2. Up to 2 splits are allowed.
# 3. When player double down, receive only one more card.
# 4. 4 decks of standard 52 cards deck are used.
# 5. After splitting a pair of As player gain only one more card each hand.
# 
# The player's hand is seing as a nested list. This approach was adopted to facilitate the splitting of pairs.
# 
# The game is composed of 4 classes named: Cards, Player, Dealer, Splitting.

# In[ ]:


import random
from IPython.display import clear_output


# In[ ]:


class Cards:
    
    '''Standard 52 card deck'''
    
    def frenchSuits(self):
        suit = ['♣','♦','♥','♠'] #clubs, diamonds, hearts and spades
        numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = 4*[j+i for i in suit for j in numbers]
    
    def shuffle(self): #shuffle the cards in self.cards (inplace change)
        self.frenchSuits()
        random.shuffle(self.cards)
    
    def deal(self): #after calling self.shuffle(), choose a card from self.cards
        if len(self.cards) == 0: #if the deck is over, cards are shuffled to fill the deck again
            self.shuffle()
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card


# In[ ]:


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = [[]]
        self.bet = []
    
    def getHand(self,cards, i): #i is the hand index
        for j,hand in enumerate(self.hand):
            if j == i:
                hand.append(cards.deal())
    
    def gameChip(self):
        while True:
            try:
                self.chips = int(input('{}, enter the number of chips you want: '.format(self.name)))
            except:
                print('You must enter an integer')
                continue
            else:
                break
    
    def toBet(self):
        while True:
            try:
                bet = int(input('{}, enter your bet: '.format(self.name)))
            except:
                print('You must enter an integer')
                continue
            else:
                break
        while True:
            if bet > self.chips:
                print('Bet greater than your chips')
                bet = int(input('{}, enter your bet: '.format(self.name)))
            else:
                self.bet.append(bet)
                break
    
    def decisions(self):
        while True:        
            try:
                self.decision = int(input('\n{}, choose one decision: \n\n 1. Hitting \n 2. Standing \n 3. Doubling down \n 4. Splitting: \n'.format(self.name) ))
            except:
                print('{}, choose a number between 1 and 4'.format(self.name))
                continue
            else:
                break
        while True:
            if self.decision > 4 or self.decision < 1:
                print('Choose a number between 1 and 4')
                self.decision = int(input('{}, choose: 1. Hitting, 2. Standing, 3. Doubling down or 4. Splitting: \n'.format(self.name)))
            else:
                break

    def doubleDown(self, hand, i):
        if len(hand) > 2:
            print('You can only double bet in the first hand')
            return False
        total_bet = sum(self.bet) + self.bet[i]
        if total_bet > self.chips:
            print('{}, your chips are not enough.'.format(self.name))
            return False
        else:
            self.bet[i] *= 2
            return True
    
    def sumCards(self,hand):   # hand argument is necessary when player split hand     
        
        def valueCards(card): #return the score of one card
            suit1 = ('J','Q','K')
            suit2 = ('2','3','4','5','6','7','8','9')
            if card[0] in suit1:
                return 10
            elif card[0] in suit2:
                return int(card[0])
            elif card[0:2] == '10':
                return 10
            else:
                return [1,11]
        
        def orderHand(hand): #sort ace to be the last card in hand
            for i, card in enumerate(hand):
                if card[0]=='A':
                    hand[i], hand[-1] = hand[-1], hand[i]
            return hand
        
        sumcard = 0 #sum the score of cards in hand, ace must be in the last position
        player_hand = orderHand(hand)
        for card in player_hand:
            if card[0] == 'A':
                sumcard += valueCards(card)[1]
                if sumcard > 21:
                    sumcard += valueCards(card)[0] - valueCards(card)[1]
            else:
                sumcard += valueCards(card)
        return sumcard
    
    def restartHand(self):
        self.hand.clear()
        self.hand.append([])
        self.bet.clear()


# In[ ]:


class Dealer(Player):
    
    def __init__(self):
        self.name = 'Dealer'
        self.hand = []
        self.chips = 0
    
    def getHand(self,cards):
        self.hand.append(cards.deal())
        if len(self.hand) == 2:
            return [self.hand[0], "?"]
    
    def gameChip(self):
        for player in self.players:
            player.gameChip()
    
    def toBet(self):
        for player in self.players: 
            if player.chips > 0:
                player.toBet()
    
    def award(self):
        for player in self.players:
            for i,hand in enumerate(player.hand):
                score = player.sumCards(hand)
                dealer_score = self.sumCards(self.hand)
                if score > 21: #player lose the bet
                    player.chips -= player.bet[i]
                    self.chips += player.bet[i]
                    print('{}, you lost with hand {}. Your chips: {}'.format(player.name,i+1,player.chips))
                elif score <= 21 and dealer_score <= 21 and dealer_score > score: #player lose the bet
                    player.chips -= player.bet[i]
                    self.chips += player.bet[i]
                    print('{}, you lost with hand {}. Your chips: {}'.format(player.name,i+1,player.chips))
                elif score <= 21 and dealer_score < 21 and score > dealer_score: #player wins
                    player.chips += player.bet[i]
                    self.chips -= player.bet[i]
                    print('Yes! {}, you won with hand {}. Your chips: {}'.format(player.name,i+1,player.chips))
                elif score == 21 and len(player.hand) == 2 and dealer_score < 21:
                    player.chips += 1.5*player.bet[i]
                    self.chips -= 1.5*player.bet[i]
                    print('Yes! {}, you won with hand {}. Your chips: {}'.format(player.name,i+1,player.chips))
                elif score <= 21 and dealer_score > 21:
                    player.chips += player.bet[i]
                    self.chips -= player.bet[i]
                    print('Yes! {}, you won with hand {}. Your chips: {}'.format(player.name,i+1,player.chips))
                elif score == dealer_score:
                    print('{}, the game tied with hand {}. Your chips: {}'.format(player.name,i+1,player.chips))
                
    def decisions(self,cards): #if player.sumCards <= 21, dealer get more cards if self.sumCards() < 17
        sum_card = 0
        for player in self.players:
            for hand in player.hand:
                if player.sumCards(hand) <= 21:
                    sum_card += 1
                    break
        if sum_card > 0:        
            while self.sumCards(self.hand) < 17:
                self.getHand(cards)
            print(self.hand)
        print('\n')
        self.award()
        print('Dealer earnings: {}'.format(self.chips))
    
    def showHands(self,dealer_cards):
        '''Show the players and the dealer hands'''
        for player in self.players:
            print('{}: {}. Chips:{}, Current bet:{}'.format(player.name,player.hand,player.chips, player.bet))
        print(self.name, ':', dealer_cards)
    
    def restartHand(self):
        self.hand.clear()
    
    def hand_decision(self, player, cards, dealer_cards):
        
        '''This method asks what players want to do with their hands'''
        
        for i, hand in enumerate(player.hand):
            if hand[i][0] == 'A' and len(player.hand)>=2:
                break
            while player.sumCards(hand) <= 21:
                print('\nHand: {}'.format(i+1))
                player.decisions()
                if player.decision == 1: #hitting
                    player.getHand(cards,i)
                elif player.decision == 3: #double down bet
                    if player.doubleDown(hand,i): #if player has enough chips.
                        player.getHand(cards,i)
                        break #player can have only one more card after double down
                elif player.decision == 4:
                    split = Splitting() #intanciating class Splitting()
                    if split.splitting(player,hand,i):
                        split.dealCards(i,player,cards)
                        hand = player.hand[i]
                        if hand[i][0] == 'A':
                            break
                elif player.decision == 2:
                    break
                self.showHands(dealer_cards)#called to show the cards hitted after a decision
            self.showHands(dealer_cards)
    
    def play(self,cards):
        '''Deal the cards, call self.hand_decision(player,cards,dealer_cards), show dealer hand after players
            have made their decisions'''
        for j in range(2): #deal cards first round
            for player in self.players:
                i = 0 #player.hand has only an empty list with index = 0 in the begging of the game.
                player_cards = player.getHand(cards,i)
            dealer_cards = self.getHand(cards)
        
        self.showHands(dealer_cards)
        
        for player in self.players:
            self.hand_decision(player,cards,dealer_cards)

        self.showHands(self.hand) #showing the dealer hand
        self.decisions(cards)
    
    def getPlayers(self):
        while True:
            try:
                number = int(input('Enter the number of players: '))
            except:
                print('You must enter an integer')
                continue
            else:
                break
        self.players = []
        for i in range(number):
            name = input('Enter the name of player {}: '.format(i+1))
            name = Player(name) #instantiating Player class
            self.players.append(name)
    
    def game(self):
        
        '''Call this method to play the game!'''
        
        self.getPlayers() #define the players
        self.gameChip() #get the amount of chips of each player
        self.toBet() #get players bets
        cards = Cards() #instantiating Cards class
        clear_output()
        cards.shuffle()
        
        def hasChips(): #the game will continue until a player has chips
            sum_chips = 0
            for player in self.players:
                if player.chips > 0:
                    sum_chips += 1
                else:
                    self.players.remove(player) #if player.chips == 0, it is removed from self.players list
            if sum_chips > 0:
                return True
            else:
                return False
        
        while hasChips():
            self.play(cards)
            for player in self.players:
                player.restartHand()
            self.restartHand()
            self.toBet()
            if hasChips():
                clear_output()


# In[ ]:


class Splitting:
    
    '''Class to split decision'''
    
    def splitting(self,player,Hand,i):
        if len(Hand) > 2:
            print("Splitting is allowed only in the hand's first decision")
            return False
        if len(player.hand) < 3:
            if Hand[0][0] == Hand[1][0]:
                if self.splitBet(player, i):
                    self.splitHand(player, Hand,i)
                    return True
            else:
                print('You must have pairs to split.')
                return False
        else:
            print('You reached the maximum split times allowed.')
            return False
    
    def splitBet(self,player, i): #list index in dealer.hand_decision()
        total_bet = sum(player.bet) + player.bet[i]
        if total_bet <= player.chips:
            player.bet.append(player.bet[i])
            return True
        else:
            print('You dont have enough chips.')
            return False
    
    def splitHand(self, player, Hand, i):
        
        '''Split hand with pairs.
        when player already has two hands and want to split the hand in position 0, the position of the new splitted hand
            must be 0 and 1 (the position is important for self.dealCards() works), so insert() method was used.'''
        
        hand1 = [Hand[0]]
        hand2 = [Hand[1]]
        player.hand.remove(Hand) #reconfigure the player.hand
        player.hand.insert(i,hand1)
        player.hand.insert(i+1,hand2)
        
    def dealCards(self,i,player,cards):
        for j in range(2):
            j += i
            player.getHand(cards,j)


# In[ ]:


dealer = Dealer()


# In[ ]:


dealer.game()

