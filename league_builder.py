import csv
import os

if __name__ == "__main__": # just incase you want to run it twice
    try:
        os.remove('teams.txt')
    except:
        pass
    sharks = []  #establish some gloabl vars to hold the teams
    raptors = []
    dragons = []

    def get_experienced():
        global sharks               #Get the experienced players sorted
        global raptors              # load global vars
        global dragons
        players = []
        with open('soccer_players.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            sharks.append('[Sharks: ]')
            raptors.append('[Raptors: ]')       #Open csv with soccer_players
            dragons.append('[Dragons: ]')       #Iterate through it and sort
            for line in csv_reader:             # by the 3rd item in the line
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
        global sharks               # Same thing but with the non experienced
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
        for x in sharks[1:]:  #Sorts the sharks into nice looking text in the teams.txt file
            names.append(str(x[0]+ ", " + x[2]+ ', ' + x[3]))
        with open('teams.txt', 'a+') as file:
            file.write("Sharks" + '\n')
            for item in names:
                file.write(item + '\n')

    def raptors_team():
        global raptors
        names = []
        for x in raptors[1:]:  #Sorts the raptors into nice looking text in the teams.txt file
            names.append(str(x[0]+ ", " + x[2]+ ', ' + x[3]))
        with open('teams.txt', 'a+') as file:
            file.write('\n')
            file.write("Raptors" + '\n')
            for item in names:
                file.write(item + '\n')
    def dragons_team():
        global dragons
        names = []
        for x in dragons[1:]:  #Sorts the dragons into nice looking text in the teams.txt file
            names.append(str(x[0]+ ", " + x[2]+ ', ' + x[3]))
        with open('teams.txt', 'a+') as file:
            file.write('\n')
            file.write("Dragons" + '\n')
            for item in names:
                file.write(item + '\n')
    def send_letter():
        for line in sharks[1:]:
            name = line[0]     # Creates a letter or text file with a few lines of text based on each player
            newfilename = name.replace(' ', '_') # removes the space from name and adds a '_'
            newfilename2 = newfilename.lower() # lower cases the name
            with open('%s.txt' % newfilename2, 'w+') as file: # file named with var filename2 which we just created
                file.write("Dear %s," % line[3] + '\n')
                file.write("Congrats, Your Child, %s, Has Been selected to play for the Sharks" % line[0] + '\n')
                file.write('First Practice is Wednesday @ 3:30pm' '\n')
                file.write('Be there or be Square')
        for line in dragons[1:]:
            name = line[0]
            newfilename = name.replace(' ', '_')
            newfilename2 = newfilename.lower()   #Repeated steps from above but for dragons
            with open('%s.txt' % newfilename2, 'w+') as file:
                file.write("Dear %s," % line[3] + '\n')
                file.write("Congrats, Your Child, %s, Has Been selected to play for the Dragons" % line[0] + '\n')
                file.write('First Practice is Wednesday @ 1:30pm' + '\n')
                file.write('Be there or be Square')
        for line in raptors[1:]:
            name = line[0]
            newfilename = name.replace(' ', '_')
            newfilename2 = newfilename.lower()   #Repeated Once again
            with open('%s.txt' % newfilename2, 'w+') as file:
                file.write("Dear %s," % line[3] + '\n')
                file.write("Congrats, Your Child, %s, Has Been selected to play for the Raptors" % line[0] + '\n')
                file.write('First Practice is Wednesday @ 3:30pm' + '\n')
                file.write('Be there or be Square')


## Now we can run the app
## Call all the functions we just created
    get_experienced()
    get_nonexp()
    sharks_team()
    raptors_team()
    dragons_team()
    send_letter()
