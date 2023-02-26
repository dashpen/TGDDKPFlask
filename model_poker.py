import random, itertools
global players
players = []
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Player:
    def __init__(self, username, chips):
        self.hand = []
        self.username = username
        self.chips = chips
        self.commited = 0
        global players
        players.append(self)
        self.win = False

    
    def draw(self, deck, draws):
        for draw in (' ' * draws):
            (self.hand).append(deck.draw())
    
    def add_card(self, card):
        (self.hand).append(card)
    
    def show_hand(self):
        for card in self.hand:
            print(card.value, 'of', card.suit)
    def hand_value(self):
        self.handrank = handcalc5(self.hand)
        self.weight = weightcalc5(self.handrank, self.hand)
    def bet(self, _bet):
        pass
        
            


class River:
    def __init__(self):
        self.cards = []

    def draw(self, deck, draws):
        for draw in (' ' * draws):
            (self.cards).append(deck.draw())
            
    def show_cards(self):
        for card in self.cards:
            print(card.value, 'of', card.suit)



class Deck:
    def __init__(self, decks):
        self.cards = [Card(value, suit) for value in range(1,14) for suit in ['hearts', 'diamonds', 'spades', 'clubs'] for decc in (' ' * decks)]
    
    def shuffle(self):
        self.cards = random.sample(self.cards, len(self.cards))
    
    def draw(self):
        drawn_card = self.cards[0]
        (self.cards).remove(drawn_card)
        return drawn_card

def five_of_a_kind(hand):
    same = 0
    for a, b in itertools.combinations(hand, 2):
        if a.value == b.value:
            same += 1
    if same >= 9:
        return True
    return False

def Straight_Flush(hand):
    same = 0
    for a, b in itertools.combinations(hand, 2):
        if a.suit == b.suit:
            same += 1
    if same <= 9:
        return False
    card_numbers = []
    for card in hand:
        card_numbers.append(card.value)
    card_numbers = sorted(card_numbers)
    count = int(card_numbers[0])
    number = 0
    for card in card_numbers:
        if count - card_numbers[0] == 5:
            return True
        if card != count:
            count = int(card_numbers[1])
            for card in card_numbers:
                if card != count:
                    count = int(card_numbers[1])
                    for card in card_numbers:
                        if card != count:
                            return False
                        if card == count:
                            count += 1
                if card == count:
                    count += 1
        if card == count:
            count += 1
    return True

def four_of_a_kind(hand):
    same = 0
    for a, b in itertools.combinations(hand, 2):
        if a.value == b.value:
            same += 1
    if same == 6:
        return True
    return False

def full_house(hand):
    same = 0
    for a, b in itertools.combinations(hand, 2):
        if a.value == b.value:
            same += 1
    if same == 4:
        return True
    return False

def flush(hand):
    same = 0
    for a, b in itertools.combinations(hand, 2):
        if a.suit == b.suit:
            same += 1
    if same <= 9:
        return False
    return True

def straight(hand):
    card_numbers = []
    for card in hand:
        card_numbers.append(card.value)
    card_numbers = sorted(card_numbers)
    number = 0
    count = int(card_numbers[0])
    for card in card_numbers:
        if count - card_numbers[0] == 5:
            return True
        if card != count:
            count = int(card_numbers[1])
            for card in card_numbers:
                if card != count:
                    count = int(card_numbers[1])
                    for card in card_numbers:
                        if card != count:
                            return False
                        if card == count:
                            count += 1
                if card == count:
                    count += 1
        if card == count:
            count += 1
    return True

def there_of_a_kind(hand):
    same = 0
    for a, b in itertools.combinations(hand, 2):
        if a.value == b.value:
            same += 1
    if same == 3:
        return True
    return False

def two_duo(hand):
    duo = 0
    for a, b in itertools.combinations(hand, 2):
        if a.value == b.value:
            duo += 1
    if duo >= 2:
        return True
    return False

def duo(hand):
    for a, b in itertools.combinations(hand, 2):
        if a.value == b.value:
            return True
    return False

def handcalc5(hand):
    #5 of a kind
    if five_of_a_kind(hand) == True:
        return 0
    #Straight Flush
    if Straight_Flush(hand) == True:
        return 1
    if four_of_a_kind(hand) == True:
        return 2
    if full_house(hand) == True:
        return 3
    if flush(hand) == True:
        return 4
    if straight(hand) == True:
        return 5
    if there_of_a_kind(hand) == True:
        return 6
    if two_duo(hand) == True:
        return 7
    if duo(hand) == True:
        return 8
    return 9

    
def weightcalc5(rank, hand):
    weight = 0
    for card in hand:
        if int(card.value) == 1:
            setattr(card, 'value', 14)
    if rank in (0, 3, 4):
        for card in hand:
            weight += card.value
        return weight
    if rank in (1, 5):
        cards = []
        for card in hand:
            cards.append(card.value)
        cards = sorted(cards, reverse=True)
        return cards[0]
    if rank == 2:
        last = None
        for card in hand:
            if card == last:
                return card * 4
            last = card
    if rank == 6:
        for a, b in itertools.combinations(hand, 2):
            if a.value == b.value:
                weight = int(a.value)
                return weight * 3
    if rank == 7:
        for a, b in itertools.combinations(hand, 2):
            if a.value == b.value:
                weight += int(a.value)
        return weight * 2
    if rank == 8:
        for a, b in itertools.combinations(hand, 2):
            if a.value == b.value:
                weight += int(a.value)
                return weight * 2
    if rank == 9:
        cards = []
        for card in hand:
            cards.append(int(card.value))
        cards = sorted(cards, reverse=True)
        return cards[0]
    pass

def win(players):
    value = 10
    weight = 0
    winner = None
    index = 0
    for player in players:
        if player.handrank < value:
            value = player.handrank
            weight = player.weight
            winner = player
            player_index = index
        elif player.handrank == value:
            if player.weight > weight:
                value = player.handrank
                weight = player.weight
                winner = player
                player_index = index
        index += 1
    print('Winner: ', winner.username, 'index', player_index)
    winner.win = True
    return player_index


def set_up_game(decks):
    global deck, river
    deck = Deck(decks)
    deck.shuffle()
    river = River()
    river.draw(deck, 5)

global chips
chips = 10
def player_creat(player):
    Players_add = []
    Players_add.append(Player(player , chips))



def draw(starting_cards):
    global players, deck
    deck.shuffle()
    for player in players:
        player.draw(deck, starting_cards)

def bettingblinds(anti):
    if players[1].chips > anti / 2:
        players[1].commited = (anti/2)
        players[1].chips -= anti
    else:
        players[1].commited = players[1].chips
    
    if players[2].chips > anti / 2:
        players[2].commited = (anti/2)
        players[2].chips -= anti
    else:
        players[2].commited = players[2].chips
        players[2].chips = 0
   

def betting():
    pass

def print_results():
    global players
    for player in players:
        for Card in river.cards:
            player.hand.append(Card)
        
    print('-------------')
    for player in players:
        player.show_hand()
        player.hand_value()
        for card in player.hand:
            if int(card.value) == 14:
                setattr(card, 'value', 1)
        print('Handrank: ', player.handrank, 'Weight: ', player.weight)
        print('-------------')
        
        
        
def initpoker(gamers):
    for gamer in gamers:
        player_creat(gamer)
    set_up_game(1)
    draw(2)
    print_results()
        
    winner_index = win(players)
    rando = []
    for player in players:
        rando.append(player.hand)
    players_dict = []
    for player in players:
        players_dict.append(player.__dict__)
    for player_dict in players_dict:
        player_dict['hand'] = []
    river_dict = []
    for card in river.cards:
        river_dict.append(card.__dict__)
    for l in rando:
        for number in range(0,2):
            l[number] = l[number].__dict__
        for number in range(2,len(l)):
             l.pop()
    
    for o,j in zip(players_dict, rando):
        o['hand'] = j
