import csv
import os
import random
os.remove('teams_new.txt')

sharks = []
raptors = []
dragons = []

def get_experienced():
    global sharks
    global raptors
    global dragons
    players = []
    with open('soccer_players.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        sharks.append('[Sharks: ]')
        raptors.append('[Raptors: ]')
        dragons.append('[Dragons: ]')

        for line in csv_reader:
            if line[2] == 'YES':
                if len(sharks) <= 3:
                    sharks.append(line)
                elif len(raptors) <= 3:
                    raptors.append(line)
                elif len(dragons) <= 3:
                    dragons.append(line)
                else:
                    print('Teams are full')
                    print(line[0] + 'cant be added')

def get_nonexp():
    global sharks
    global raptors
    global dragons

    with open('soccer_players.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for line in csv_reader:
            if line[2] == 'NO':
                if len(sharks) <= 6:
                    sharks.append(line)
                elif len(raptors) <= 6:
                    raptors.append(line)
                elif len(dragons) <= 6:
                    dragons.append(line)
                else:
                    print('Teams are full')
                    print(line[0] + 'cant be added')
def sharks_team():
    global sharks
    names = []
    for x in sharks[1:]:
        names.append(str(x[0]+ ", " + x[1]+ ', ' + x[3]))
    with open('teams_new.txt', 'a+') as file:
        file.write("Sharks" + '\n')
        for item in names:
            file.write(item + '\n')

def raptors_team():
    global raptors
    names = []
    for x in raptors[1:]:
        names.append(str(x[0]+ ", " + x[1]+ ', ' + x[3]))
    with open('teams_new.txt', 'a+') as file:
        file.write('\n')
        file.write("Raptors" + '\n')
        for item in names:
            file.write(item + '\n')
def dragons_team():
    global dragons
    names = []
    for x in dragons[1:]:
        names.append(str(x[0]+ ", " + x[1]+ ', ' + x[3]))
    with open('teams_new.txt', 'a+') as file:
        file.write('\n')
        file.write("Dragons" + '\n')
        for item in names:
            file.write(item + '\n')
get_experienced()
get_nonexp()
sharks_team()
raptors_team()
dragons_team()
