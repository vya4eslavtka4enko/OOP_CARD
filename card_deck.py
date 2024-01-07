import random
class Card():
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    def present(self):
        return f'{self.value} of {self.suit}'
    

class Deck():
    def __init__(self,cards):
        self.cards = []
    def make_deck(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for suit in suits:
            for value in values:
                self.card = Card(value=value,suit=suit)
                self.cards.append(self.card)
        # for item in self.cards:
        #     print(item.present())
        
    def shuffle(self):
        random.shuffle(self.cards)
        
        
    def deal(self):
        save_last = self.cards[-1].present()
        self.cards.remove(self.cards[-1])
        return save_last
    
    def count_remaining(self):
        return len(self.cards)
    
    
    def get_remaining(self):
        remaining_list = []
        for item in self.cards:
            remaining_list.append(item.present())
        print(remaining_list)

# [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]



from random import shuffle
 
class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
 
	def present(self):
		return self.value + ' of ' + self.suit 
 
class Deck:
	def __init__(self):
	    suits = ['hearts', 'diamonds', 'clubs', 'spades']
	    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
	    self.cards = [Card(suit, value) for suit in suits for value in values]
 
	def shuffle(self):
		shuffle(self.cards)
 
	def deal(self):
	    if len(self.cards) == 0:
	        return None
	    return self.cards.pop()
 
	def count_remaining(self):
	    return len(self.cards)
	
	def get_remaining(self):
	    return [x.present() for x in self.cards]

