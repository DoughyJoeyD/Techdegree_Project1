import csv
import random
import os
def get_names():
    experienced_players = []
    non_experienced_players = []
    os.remove('experienced_players.csv')
    os.remove('non_experienced_players.csv')
    with open('soccer_players.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        for line in csv_reader:
            if line[2] == "YES":
                with open('experienced_players.csv', 'a+') as new_file:
                    csv_writer = csv.writer(new_file, delimiter=',')
                    csv_writer.writerow(line)     
                print('Added to Experienced Players List')
            elif line[2] == "NO":
                with open('non_experienced_players.csv', 'a+') as new_file2:
                    csv_writer2 = csv.writer(new_file2, delimiter=',')
                    csv_writer2.writerow(line)
                    print('Added to Non Experienced Players List')
            else:
                continue                    
    print('Players')                          

def get_exp():
    try:
        os.remove('experienced_players.csv')
    except:
        pass

    with open('soccer_players.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open('experienced_players.csv', 'a+') as new_file:
            fieldnames = ['Name', 'Height (inches)', 'Soccer Experience', 'Guardian Name(s)']
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
            csv_writer.writeheader()
            for line in csv_reader:
                if line['Soccer Experience'] == 'YES':
                    csv_writer.writerow(line)

def get_nonexp():
    try:
        os.remove('non_experienced_players.csv')
    except:
        pass

    with open('soccer_players.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open('non_experienced_players.csv', 'a+') as new_file2:
            fieldnames = ['Name', 'Height (inches)', 'Soccer Experience', 'Guardian Name(s)']
            csv_writer2 = csv.DictWriter(new_file2, fieldnames=fieldnames, delimiter=',')
            csv_writer2.writeheader()
            for line in csv_reader:
                if line['Soccer Experience'] == 'NO':
                    csv_writer2.writerow(line)

def make_teams_exp():
    players_exp = []
    players_nonexp = []
    try:
        os.remove('teams.cvs')
        os.remove('teams.txt')
    except:
        pass

    with open('teams.cvs', 'a+') as new_file:
        fieldnames = ['Name', 'Height (inches)', 'Soccer Experience', 'Guardian Name(s)'] 
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
        csv_writer.writeheader()
        with open('experienced_players.csv', 'r') as csv_file:
            file = open('teams.txt', 'a+')
            csv_reader = csv.DictReader(csv_file)
            file.write('Name, Height, Experience, Parents' + '\n')
            for line in csv_reader:
                csv_writer.writerow(line)
                file.write(line['Name'] +", "+ line['Height (inches)'] +', '+ line['Soccer Experience'] +', '+ line['Guardian Name(s)'] + '\n')
        with open('non_experienced_players.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                csv_writer.writerow(line)
                             
###
# Re open exp and nonexp files
# write to teams file with append
# delete file everytime the command is run
#strip the file so it meets standards
# improve the code simplicity and design


get_exp()
get_nonexp()
make_teams_exp()                               