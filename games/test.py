
import re
import random
from itertools import combinations

# Text containing missions and difficulties
mission_text = """
(2/3/3) Win more tricks than everyone else
(3/4/5) Win more tricks than everyone else together
(2/2/3) Win fewer tricks than everyone else
(2/2/3) Win more tricks than the captain (the captain can’t take this mission)
(2/2/2) Win fewer tricks than the captain (the captain can’t take this mission)
(4/3/3) Win the same number of tricks as the captain (the captain can’t take this mission)
(2/3/3) Win a trick where all cards are of lower value than 7 without submarines
(2/3/4) Win a trick where all cards are of greater value than 5
(2/3/3) Win a trick with a 6
(2/3/4) Win a trick with a 5
(3/4/5) Win a trick with a 3
(1/2/2) Win a 5 with a 7
(3/4/5) Win an 8 with a 4
(2/3/4) Win any 6 with a another 6
(3/4/5) Win a trick with a 2
(1/1/1) Win the DIAMOND 3
(1/1/1) Win the HEART 1
(1/1/1) Win the CLUB 4
(1/1/1) Win the SPADE 6
(3/4/5) Win all four 3s
(3/4/5) Win at least three 5s
(3/4/5) Win at least three 9s
(2/2/2) Win at least two 7s
(4/5/6) Win all four 9s
(3/4/4) Win exactly three 6s
(2/3/3) Win exactly two 9s
(2/3/3) Win the CLUB 1,2 and 3
(2/2/3) Win the CLUB 6 and the HEART 7
(2/2/3) Win the DIAMOND 5 and HEART 6
(2/2/3) Win the SPADE 5 and CLUB 8
(2/2/3) Win the CLUB 5 and DIAMOND 8
(2/2/3) Win the DIAMOND 9 and HEART 8
(2/2/2) Win the DIAMOND 1 and SPADE 7
(2/3/3) Win the HEART 9 and CLUB 7
(3/4/4) Win the SPADE 3 and the HEART 4 and 5
(3/4/5) Win the SPADE 2 in the last trick
(4/4/4) Win exactly one DIAMOND and one SPADE card
(3/3/3) Win at least seven HEART cards
(2/3/3) Win at least five DIAMOND cards
(3/4/4) Win exactly two SPADE cards
(3/4/4) Win exactly two CLUB cards
(3/3/4) Win exactly one DIAMOND card
(2/2/2) Win no DIAMOND cards
(2/3/4) Win at least one card of each colour (excluding submarines)
(3/4/5) Win all cards of at least one colour (excluding submarines)
(2/5/6) Win a trick that has only even numbers (2,4,6,8)
(2/4/5) Win a trick that has only numbers (1,3,5,7,9)
(3/3/4) Win a trick with a total value higher than 23/28/31 (3/4/5 players) without submarines
(3/3/4) Win a trick with a total value lower than 8/12/16 (3/4/5 players) without submarines
(3/3/4) Win a trick with a total value of 22 or 23
(3/3/3) Win exactly one submarine (deal new cards if someone has all submarines in hand)
(3/3/3) Win the 1 submarine and no other (deal new cards if someone has submarines no. 1 and 4 or 1,2,3 in hand)
(3/3/3) Win the 2 submarine and no other (deal new cards if someone has submarines no. 2 and 4 or 1,2,3 in hand)
(1/1/1) Win the 3 submarine
(3/3/4) Win exactly two submarines (deal new cards if someone has submarines no. 2,3,4 in hand)
(3/4/4) Win exactly three submarines (deal new cards if someone has all submarines in hand)
(1/1/1) Win no submarines
(3/3/3) Win the DIAMOND 7 with a submarine
(3/3/3) Win the SPADE 9 with a submarine
(4/3/3) Don’t open a trick with a DIAMOND, HEART or CLUB card
(2/1/1) Don’t open a trick with a DIAMOND or SPADE card
(2/2/2) Don’t win any SPADE cards
(2/2/2) Don’t win any HEART cards
(3/3/3) Don’t win any DIAMOND or CLUB cards
(3/3/3) Don’t win any HEART or SPADE cards
(3/3/2) Don’t win any 8s or 9s
(1/1/1) Don’t win any 9s
(1/2/2) Don’t win any 5s
(2/2/2) Don’t win any 1s
(3/3/3) Don’t win any 1s, 2s or 3s
(1/2/3) Don’t win any of the first four tricks
(1/2/2) Don’t win any of the first three tricks
(2/3/3) Don’t win any of the first five tricks
(4/3/3) Don’t win any tricks
(3/2/2) Do not win two consecutive tricks
(2/3/3) Win the last trick
(2/3/4) Win the first three tricks
(1/1/2) Win the first two tricks
(1/1/1) Win the first trick
(3/4/4) Win the first and the last trick
(4/4/4) I win only the last trick
(4/3/3) I win only the first trick
(3/2/2) Win exactly one trick
(2/2/2) Win exactly two tricks
(1/1/1) Win two consecutive tricks
(2/3/4) Win three consecutive tricks
(2/3/5) Win exactly four tricks
(3/3/4) Win exactly three consecutive tricks
(3/3/3) Win exactly two consecutive tricks
(3/2/2) Win X tricks (predict the exact number and show)
(4/3/3) Win X tricks (predict the exact number but keep hidden)
(4/4/4) Win the same amount of DIAMOND and HEART cards (more than 0)
(2/3/3) Win the same amount of SPADE and HEART cards in a trick (more than 0)
(2/3/3) Win the same amount of DIAMOND and CLUB cards in a trick (more than 0)
(1/1/1) Win more HEART cards than CLUB cards (0 CLUB cards are allowed)
(1/1/1) Win more DIAMOND cards than SPADE cards (0 SPADE cards are allowed)
"""

def parse_missions(text):
    missions = []
    pattern = re.compile(r'\((\d+)/(\d+)/(\d+)\) (.+)')
    for line in text.strip().split('\n'):
        match = pattern.match(line.strip())
        if match:
            difficulties = list(map(int, match.groups()[:3]))
            description = match.groups()[3]
            missions.append((description, difficulties))
    return missions

def get_mission_difficulty(mission, player_count):
    if player_count == 3:
        return mission[1][0]
    elif player_count == 4:
        return mission[1][1]
    elif player_count == 5:
        return mission[1][2]
    else:
        return None

def main():
    missions = parse_missions(mission_text)

    player_count = int(input("Enter player count (3, 4, or 5): "))
    if player_count not in [3, 4, 5]:
        print("Invalid player count. Please enter 3, 4, or 5.")
        return
    
    deck = missions[:]
    random.shuffle(deck)
    while True:
        taken = []
        difficulty = int(input("Enter desired difficulty: "))
        index = 0
        while difficulty > 0:
            if len(deck) == 0:
                deck = [not_taken for not_taken in missions if not_taken not in taken]
                random.shuffle(deck)
            top = deck[-1]
            mission_difficulty = get_mission_difficulty(top, player_count)
            if mission_difficulty <= difficulty:
                taken += [top]
                difficulty -= mission_difficulty
            del deck[-1]
        for val in taken:
            print("- {} ({})".format(val[0], get_mission_difficulty(val, player_count)))

if __name__ == "__main__":
    main()

