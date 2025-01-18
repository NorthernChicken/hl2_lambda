"""
Find the missing lambda cache locations in Half Life 2.
This script was originally written by huntfx in this Gist: https://gist.github.com/huntfx/ba8dde26845f7eb4f5dd604d5200d709
It has been updated by NorthernChicken at this repo:
"""

import os

# Change this line if you have games installed elsewhere
# STEAMAPPS = 'C:/Program Files (x86)/Steam/steamapps/common/'
STEAMAPPS = '/mnt/steamgames/SteamLibrary/steamapps/common/'

GAMESTATE = os.path.join(STEAMAPPS, 'Half-Life 2/hl2_complete/gamestate.txt')

# Locations from https://steamcommunity.com/sharedfiles/filedetails/?id=145616679
LOCATIONS = [
    'A Red Letter Day 1',
    'Route Kanal 1',
    'Route Kanal 2',
    'Route Kanal 3',
    'Route Kanal 4',
    'Route Kanal 5',
    'Route Kanal 6',
    'Route Kanal 7',
    'Water Hazard 1',
    'Water Hazard 2',
    'Water Hazard 3',
    'Water Hazard 4',
    'Water Hazard 5',
    'Water Hazard 6',
    'Water Hazard 7',
    'Water Hazard 8',
    'Water Hazard 9',
    'Water Hazard 10',
    'Black Mesa East 1',
    "We Don't Go To Ravenholm... 1",
    "We Don't Go To Ravenholm... 2",
    "We Don't Go To Ravenholm... 3",
    "We Don't Go To Ravenholm... 4",
    'Highway 17 1',
    'Highway 17 2',
    'Highway 17 3',
    'Highway 17 4',
    'Highway 17 5',
    'Sandtraps 1',
    'Sandtraps 2',
    'Nova Prospekt 1',
    'Nova Prospekt 2',
    'Nova Prospekt 3',
    'Entanglement 1',
    'Anticitizen One 1',
    'Anticitizen One 2',
    'Anticitizen One 3',
    'Anticitizen One 4',
    'Anticitizen One 5',
    'Anticitizen One 6',
    'Anticitizen One 7',
    'Anticitizen One 8',
    'Anticitizen One 9',
    'Anticitizen One 10',
    'Follow Freeman 1',
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
