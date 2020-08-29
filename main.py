from math import comb
from pprint import pprint
import numpy as np
import itertools

no_positions = 11
iterations = 0
best_team_score = 0

#list of 18 players from fantasy football, each player has a name, position, expected points and price 
playerList = np.array([
["De Bruyne", "m", 250, 11.5], ["B.Fernandes", "m", 210, 10.5], ["Werner", "f", 200, 9.5],
    ["Jimenez", "f", 190, 8.5], ["Ings", "f", 195, 8.5], ["Martial", "f", 200, 9], ["Sterling", "m", 230, 11.5],
    ["Son", "m", 175, 8.5], ["Greenwood", "m", 160, 7.5], ["Armstrong", "m", 130, 5.5], ["Saint-Maximin", "m", 130, 5.5],
    ["Alexander-Arnold", "d", 210, 7.5], ["Van Dijk", "d", 180, 6.5], ["Robertson", "d", 190, 7],
    ["Doherty", "d", 180, 6], ["Tarkowski", "d", 140, 5.5], ["Pope", "g", 170, 5.5], ["Ryan", "g", 150, 4.5],
])
############################################################################################################################

#rearranges playerList to be in descending order of value (expected points/price)
key_values = playerList[:,2].astype(int) / playerList[:,3].astype(float)
index_array = np.argsort(key_values)[::-1]

sortedPlayerList = []

for x in range (0, len(index_array)):
    sortedPlayerList.append(playerList[index_array[x]])

playerList = sortedPlayerList
#############################################################################################################################

#calculates and prints number of possible team combos to give an idea how long the program will run for
combinations = comb(len(playerList), no_positions)
print(combinations)
#############################################################################################################################

#generates each 11 player team combo 
for x in range(no_positions, no_positions+1):
    for subset in itertools.combinations(playerList,x):

        iterations = iterations + 1 #tracks number of teams generated (for the purpose of program progress stats)

        captain_points = 0
        captain = ""
        money = 96 
        score = 0
        f = 0
        m = 0
        d = 0
        g = 0



        for x in range(0, len(subset)):
            if subset[x][1] == "f": f = f + 1
            if subset[x][1] == "m": m = m + 1
            if subset[x][1] == "d": d = d + 1
            if subset[x][1] == "g": g = g + 1
            if float(subset[x][2]) > captain_points: captain_points = float(subset[x][2]); captain = subset[x][0]
            money = money - float(subset[x][3])
            score = score + float(subset[x][2])


        if score < best_team_score: continue

        if f == 0: continue
        if f > 3: continue
        if f == 1: money = money - 9
        if f == 2: money = money - 4.5
        if m == 0: continue
        if m == 1: continue
        if m > 5: continue
        if m == 2: money = money - 13.5
        if m == 3: money = money - 9
        if m == 4:money = money - 4.5
        if d > 5: continue
        if d == 0: continue
        if d == 1 : continue
        if d == 2 : continue
        if d == 3: money = money - 8
        if d == 4: money = money - 4
        if g !=1: continue
        if g + d + m + f != 11: continue

        if money < 0: continue
        print("----------------------------------------------------------------------------------------------------------")
        pprint(subset)
        print("Points: " + str(score + float(captain_points)) + ", Captain: " + captain + ", itb: " + str(money) )
        print("Completed: " + str("{:.2f}".format(iterations/combinations*100) +"%"))
        best_team_score = score

print("Completed: " + str("{:.2f}".format(iterations/combinations*100) +"%"))



