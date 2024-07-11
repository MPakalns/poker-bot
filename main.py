import random

class Suit:
    def __init__(self, symbol):
        self.symbol = symbol

    def return_symbol(self):
        return self.symbol

class Rank:
    def __init__(self, symbol, strength_index):
        self.symbol = symbol
        self.strength_index = strength_index

    def return_symbol(self):
        return self.symbol
    
suits = []
suits.append(Suit("♠"))
suits.append(Suit("♥"))
suits.append(Suit("♦"))
suits.append(Suit("♣"))

ranks = []
ranks.append(Rank("2", 1))
ranks.append(Rank("3", 2))
ranks.append(Rank("4", 3))
ranks.append(Rank("5", 4))
ranks.append(Rank("6", 5))
ranks.append(Rank("7", 6))
ranks.append(Rank("8", 7))
ranks.append(Rank("9", 8))
ranks.append(Rank("10", 9))
ranks.append(Rank("J", 10))
ranks.append(Rank("Q", 11))
ranks.append(Rank("K", 12))
ranks.append(Rank("A", 13))
    
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def print_info(self):
        print("Card info: " + self.suit.return_symbol() + self.rank.return_symbol())

def generate_card_from_string(string):
    suits_symbols = [suit.return_symbol() for suit in suits]
    suits_index = suits_symbols.index(string[0])
    suit = suits[suits_index]

    ranks_symbols = [rank.return_symbol() for rank in ranks]
    ranks_index = ranks_symbols.index(string[1])
    rank = ranks[ranks_index]

    return Card(suit, rank)

class Deck:
    all_cards = []

    def __init__(self):
        self.generate_full_deck()
        self.shuffle_cards()

    def generate_full_deck(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.all_cards.append(new_card)

    def shuffle_cards(self):
        random.shuffle(self.all_cards)

    def deal_out_card(self):
        random_card = random.choice(self.all_cards)
        self.all_cards.remove(random_card)
        return random_card

class Hand:
    all_cards = []
    combinations = None

    def __init__(self, hole_card_1, hole_card_2):
        self.hole_card1 = hole_card_1
        self.hole_card2 = hole_card_2
        self.all_cards.append(hole_card_1)
        self.all_cards.append(hole_card_2)

    def add_community_card(self, community_card):
        self.all_cards.append(community_card)

    def print_info(self):
        for card in self.all_cards:
            card.print_info()

class CombinationFinder:


    high_card = None
    

    def __init__(self, hand):
        self.hand = hand

    def update(self):
        self.high_card()
        self.one_pair = self.one_pair()

    def high_card(self):
        current_highest_card = None
        for card in self.hand.all_cards:
            if (current_highest_card == None or card.rank.strength_index >= current_highest_card.rank.strength_index):
                current_highest_card = card

        self.high_card = current_highest_card

    def one_pair(self):
        all_cards = self.hand.all_cards
        for card in all_cards:
            all_cards.remove(card)
            for compare_against_card in all_cards:
                if (card.rank == compare_against_card.rank):
                    return [card, compare_against_card]
        
        return []

# --- MAIN LOOP ---


