import sys
import os
import csv

if __name__ == "__main__":
	def get_skill():
		with open('soccer_players.csv', newline='') as csvfile:
			reader = list(csv.reader(csvfile))
			for row in reader:
				print(row[0])
get_skill()				