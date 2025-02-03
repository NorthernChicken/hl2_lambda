"""
Find the missing lambda cache locations in Half Life 2.
This script was originally written by huntfx in this Gist: https://gist.github.com/huntfx/ba8dde26845f7eb4f5dd604d5200d709
It has been updated by NorthernChicken at this repo:
"""

import os

# Change this line if you have games installed elsewhere
STEAMAPPS = 'C:/Program Files (x86)/Steam/steamapps/common/'

GAMESTATE = os.path.join(STEAMAPPS, 'Half-Life 2/hl2_complete/gamestate.txt')

# Locations from https://steamcommunity.com/sharedfiles/filedetails/?id=145616679
LOCATIONS = [
    '#1 A Red Letter Day: map d1_trainstation_05',
    '#2 Route Kanal: map d1_canals_01',
    '#3 Route Kanal: map d1_canals_01',
    '#4 Route Kanal: map d1_canals_01a',
    '#5 Route Kanal: map d1_canals_02',
    '#6 Route Kanal: map d1_canals_03',
    '#7 Route Kanal: map d1_canals_05',
    '#8 Route Kanal: map d1_canals_05',
    '#9 Water Hazard: map d1_canals_06',
    '#10 Water Hazard: map d1_canals_06',
    '#11 Water Hazard: map d1_canals_06',
    '#12 Water Hazard: map d1_canals_07',
    '#13 Water Hazard: map d1_canals_08',
    '#14 Water Hazard: map d1_canals_08',
    '#15 Water Hazard: map d1_canals_09',
    '#16 Water Hazard: map d1_canals_10',
    '#17 Water Hazard: map d1_canals_10',
    '#18 Water Hazard: map d1_canals_12',
    '#19 Black Mesa East: map d1_eli_01',
    "#20 We Don't Go To Ravenholm...: map d1_town_01",
    "#21 We Don't Go To Ravenholm...: map d1_town_01",
    "#22 We Don't Go To Ravenholm...: map d1_town_01a",
    "#23 We Don't Go To Ravenholm...: map d1_town_05",
    '#24 Highway 17: map d2_coast_01',
    '#25 Highway 17: map d2_coast_03',
    '#26 Highway 17: map d2_coast_04',
    '#27 Highway 17: map d2_coast_05',
    '#28 Highway 17: map d2_coast_07',
    '#29 Sandtraps: map d2_coast_09',
    '#30 Sandtraps: map d2_coast_11',
    '#31 Nova Prospekt: map d2_prison_02',
    '#32 Nova Prospekt: map d2_prison_03',
    '#33 Nova Prospekt: map d2_prison_05',
    '#34 Entanglement: map d2_prison_06',
    '#35 Anticitizen One: map 3_c17_02',
    '#36 Anticitizen One: map d3_c17_04',
    '#37 Anticitizen One: map d3_c17_05',
    '#38 Anticitizen One: map d3_c17_06a',
    '#39 Anticitizen One: map d3_c17_06b',
    '#40 Anticitizen One: map d3_c17_06b',
    '#41 Anticitizen One: map d3_c17_08',
    '#42 Anticitizen One: map d3_c17_08',
    '#43 Anticitizen One: map d3_c17_08',
    '#44 Anticitizen One: map d3_c17_08',
    '#45 Follow Freeman: map d3_c17_12b',
]


if __name__ == '__main__':
    try:
        with open(GAMESTATE, 'r') as f:
            for line in f:
                if line.startswith('\t\t"data"\t\t"0x'):
                    hex = line.strip().rsplit('\t', 1)[1][1:-1]
                    binary = bin(int(hex[2:], 16))[2:].zfill(45)
                    print('Found:', binary.count('1'))
                    print('Missing:', binary.count('0'))
                    for i, visited in enumerate(map(int, binary[::-1])):
                        if not visited:
                            print(LOCATIONS[i])
                    break

    except IOError:
        print('Error: Unable to find gamestate.txt.')
        print('You may need to find at least one lambda cache first.')
