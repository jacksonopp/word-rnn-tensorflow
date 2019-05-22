import json as j

with open('/Users/jacksonoppenheim/Documents/MTGRNN/RNA/RNA.json', 'r') as f:
    RNA_dict = j.load(f)

#Whole Card File
cardWhole = open("/Users/jacksonoppenheim/Documents/MTGRNN/RNA/cards.txt", "w")
for cards in RNA_dict:
    cardWhole.write('Name: ')
    cardWhole.write(cards['name'])
    cardWhole.write('\n')
    try:
        cardWhole.write('Mana Cost: ')
        cardWhole.write(cards['manaCost'])
        cardWhole.write('\n')
        cardWhole.write('Card Type: ')
        cardWhole.write(cards['type'])
        cardWhole.write('\n')
        cardWhole.write('Text: ')
        cardWhole.write(cards['text'])
        cardWhole.write('\n \n')

    except:
        cardWhole.write("\n")
    cardWhole.write("\n")
cardWhole.close()
'''
#Card Name File
cardName = open('/Users/jacksonoppenheim/Documents/MTGRNN/RNA/cardName.txt', 'w')
for cards in RNA_dict:
    cardName.write(cards['name'])
    cardName.write('\n')
cardName.close()

#Card Text File
cardText = open('/Users/jacksonoppenheim/Documents/MTGRNN/RNA/cardText.txt', 'w')
for cards in RNA_dict:
    try:
        cardText.write(cards['text'])
        cardText.write('\n')
    except:
        print("nothing here")
cardText.close()
'''
