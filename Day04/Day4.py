with open(r"C:\Users\Steve\Desktop\Advent of Code\input\Day4.txt") as input:
    callouts = next(input).strip().split(",")
    cards = []
    while next(input, None) == "\n":
        cards.append(next(input).strip().split())
        for i in range(4):
            cards[-1].extend(next(input).strip().split())
            
def find_winner(callouts, cards):
    for callout in callouts:
        cards = [[num if num != callout else "" for num in card] for card in cards]
        for card in cards:
            # Check columns            
            for x in range(5):
                for y in range(5):
                    if card[x + 5*y] != "":
                        break
                    if y == 4:
                        return int(callout) * sum([int(num) for num in card if num != ""])
            # Check rows
            for y in range(5):
                for x in range(5):
                    if card[5*y + x] != "":
                        break
                    if x == 4:
                        return int(callout) * sum([int(num) for num in card if num != ""])

def find_loser(callouts, cards):
    for callout in callouts:
        cards = [[num if num != callout else "" for num in card] for card in cards]
        losers = []
        for card in cards:
            b = False
            # Check columns            
            for x in range(5):
                for y in range(5):
                    if card[x + 5*y] != "":
                        break
                    if y == 4:
                        if len(cards) == 1:
                            return int(callout) * sum([int(num) for num in card if num != ""])
                        b = True
            if b:
                continue
            # Check rows
            for y in range(5):
                for x in range(5):
                    if card[5*y + x] != "":
                        break
                    if x == 4:
                        if len(cards) == 1:
                            return int(callout) * sum([int(num) for num in card if num != ""])
                        b = True
            if b:
                continue
            losers.append(card)
##        print(cards, callout)
        cards = losers

##print(find_winner(callouts,cards))
print(find_loser(callouts,cards))
