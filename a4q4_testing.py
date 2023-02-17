#Name: Nhu Nhu Ly
#NSID: cvd326
#instructor's name: Eric Neufeld
#student number: 11333935
#course number: 27177
#lab section: Monday 1:30 - 2:50 - 28623

import a4q4 as C

card = C.Card()
deck = card.create()

 #test create(self):
print('Testing if the create(self) operation print out')
print('to the console enough 52 cards')
   
expected1 = ['AH', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'JH', 'QH', 'KH', 'AD', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'JD', 'QD', 'KD', 'AS', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'JS', 'QS', 'KS', 'AC', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'JC', 'QC', 'KC', 'AH', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'JH', 'QH', 'KH', 'AD', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'JD', 'QD', 'KD', 'AS', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'JS', 'QS', 'KS', 'AC', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'JC', 'QC', 'KC']
result1 = card.create()
if expected1 == result1:
    print("The create() operation prints out enough 52 cards") 

else:
    print("Error in the create() operation. Please try again...")

print()
########

#test deal(self, num_cards, num_players, deck)
num_cards1 = 2
num_players1 = 3
reason1 = "Test when the operation distributes {} cards to {} players".format(num_cards1,num_players1)
result2 = card.deal(2,3,deck)

#because this is including the random.randint() built-in function so that
#it is impossible to have the expectation for the test case

print(reason1)
print(result2)
print()

num_cards2 = 10
num_players2 = 4
reason2 = "Test when the operation distributes {} cards to {} players".format(num_cards2,num_players2)
result2 = card.deal(10,4,deck)

print(reason2)
print(result2)
print()

#test when there is not enough cards
num_cards3 = 10
num_players3 = 7
reason3 = "Test when the operation distributes {} cards to {} players but this time is not enough cards".format(num_cards3,num_players3)
print(reason3)

result3 = card.deal(10,7,deck)

print(result3)
print()

#test if there is a duplicate in the random distribution
def test_dup(card_collection):
    a = 1
    player = 0  

    for player in range(len(card_collection)):
        for i in card_collection[player]:
            for v in (card_collection[player])[a:]:
                if i == v:
                    print('The value of {} in {} is duplicated'.format(v,card_collection[player]))
                    return v
                
                a += 1

        player += 1

#I myself create a list in list where there are duplicated elements
test_case1 = [['C8', 'S6', 'C3', 'C8', 'H8'], ['C4', 'QH', 'C6', 'S5', 'D9'], ['S2', 'H4', 'C6', 'D3', 'D6'], ['AS', 'C9', 'KH', 'AH', 'QC']]
reason4 = "Test a list in list where there are duplicated elements. "
expected1 = 'C8'
result4 = test_dup(test_case1)

if expected1 == result4:
    print('{}'.format(reason4))
else:
    print('{}'.format(reason4))
    print('There is not a single element duplicated!')

print()

#another try but this time with non-duplicated elements:
test_case4 = [['C8', 'S6', 'C3', 'KD', 'H8'], ['C4', 'QH', 'C6', 'S5', 'D9'], ['S2', 'H4', 'C6', 'D3', 'D6'], ['AS', 'C9', 'KH', 'AH', 'QC']]
reason7 = "Test a list in list where there are non-duplicated elements. "
expected4 = None
result7 = test_dup(test_case4)

if expected4 != result7:
    print('{}'.format(reason7))
else:
    print('{}'.format(reason7))
    print('There is not a single element duplicated!')

print()
#assign the collection_card returned by the operation
#deal(self, num_cards, num_players, deck) to parameter of
#the test function test_dup to see if the operation
#is actually giving random cards.

#first attempt with 2 cards for each of 3 players
test_case2 = card.deal(2,3,deck)
reason5 = "Test the list of collection_card returned by the operation deal(2,3,deck):"
expected2 = None
result5 = test_dup(test_case2)

if expected1 == result4:
    print('{}'.format(reason5))
    print('The operation is actually giving random cards.')
else:
    print('{}'.format(reason4))
    print('The operation does not work properly...')

print()

#second attempt with 4 cards for each of 6 players
test_case3 = card.deal(4,6,deck)
reason6 = "Test the list of collection_card returned by the operation deal(4,6,deck):"
expected3 = None
result6 = test_dup(test_case2)

if expected3 == result6:
    print('{}'.format(reason6))
    print('The operation is actually giving random cards.')
else:
    print('{}'.format(reason6))
    print('The operation does not work properly...')

print()

#test value(self, card)
#first attempt
test_case5 = 'AH'
expected5 = 1
result8 = card.value('AH')

if result8 == expected5 : 
    print('Testing value(self,card) operation:')
    print('Expecting {} to be {} - Obtaining {} -- Correct!'.format(test_case5,expected5, result8))

else:
    print('Testing value(self,card) operation:')
    print('The operation does not work properly...')

print()

#second attempt
test_case6 = '3H'
expected6 = 3
result9 = card.value('3H')

if result9 == expected6 : 
    print('Testing value(self,card) operation:')
    print('Expecting {} to be {} - Obtaining {} -- Correct!'.format(test_case6,expected6,result9))

else:
    print('Testing value(self,card) operation:')
    print('The operation does not work properly...')

print()

#third attempt
test_case7 = 'JH'
expected7 = 11
result10 = card.value('JH')

if result10 == expected7 : 
    print('Testing value(self,card) operation:')
    print('Expecting {} to be {} - Obtaining {} -- Correct!'.format(test_case7,expected7,result10))

else:
    print('Testing value(self,card) operation:')
    print('The operation does not work properly...')

print()

#test highest(self,list_of_cards)
#first attempt
test_case8 = ['5D','10H','QS','KD']
expected8 = 'KD'
result11 = card.highest(test_case8)

if result11 == expected8 :
    print('Testing highest(self, list of cards) operation:')
    print('The highest value in the list of {} is expected to be {}'.format(test_case8,expected8))
    print('The operation returns {} - which is correct!'.format(result11))

else:
    print('Testing highest(self, list of cards) operation:')
    print('The highest value in the list of {} is expected to be {}'.format(test_case8,expected8))
    print('The result is not what we expected!!!')

print()

#second attempt
test_case9 = ["5D","10H","QS","8C","JH"]
expected9 = 'QS'
result12 = card.highest(test_case9)

if result12 == expected9 :
    print('Testing highest(self, list of cards) operation:')
    print('The highest value in the list of {} is expected to be {}'.format(test_case9,expected9))
    print('The operation returns {} - which is correct!'.format(result12))

else:
    print('Testing highest(self, list of cards) operation:')
    print('The highest value in the list of {} is expected to be {}'.format(test_case9,expected9))
    print('The result is not what we expected!!!')

print()

#test lowest(self, list_of_cards)
#first attempt

test_case10 = ['5D','10H','QS','8C','JH']
expected10 = '5D'
result13 = card.lowest(test_case10)

if result13 == expected10 :
    print('Testing highest(self, list of cards) operation:')
    print('The lowest value in the list of {} is expected to be {}'.format(test_case10,expected10))
    print('The operation returns {} - which is correct!'.format(result13))

else:
    print('Testing highest(self, list of cards) operation:')
    print('The highest value in the list of {} is expected to be {}'.format(test_case10,expected10))
    print('The result is not what we expected!!!')

print()

#second attempt
test_case11 = ['5D','AH','4H','7S','KD']
expected11 = 'AH'
result14 = card.lowest(test_case11)

if result14 == expected11 :
    print('Testing highest(self, list of cards) operation:')
    print('The lowest value in the list of {} is expected to be {}'.format(test_case11,expected11))
    print('The operation returns {} - which is correct!'.format(result14))

else:
    print('Testing highest(self, list of cards) operation:')
    print('The highest value in the list of {} is expected to be {}'.format(test_case11,expected11))
    print('The result is not what we expected!!!')

print()
