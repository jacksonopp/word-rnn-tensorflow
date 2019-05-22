import json as j

with open('/Users/jacksonoppenheim/Documents/MTGRNN/Cards/GS1/GS1.json', 'r') as f:
    DOM_dict = j.load(f)

#Whole Card File
cardWhole = open("/Users/jacksonoppenheim/Documents/MTGRNN/Cards/GS1/GS1.txt", "w")
for cards in DOM_dict:
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
