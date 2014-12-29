import people
import institutions
import random

people.debug = True
citizens = []
main_bank = institutions.Bank("Main")
def print_citizens():
	for p in citizens:
		print p.to_string()
	
#create 10 people
for i in range(10):
	citizens.append(people.Person(main_bank))

#print out 10 people
print_citizens()

#randomize the list of people
random.shuffle(citizens)
print_citizens()
print main_bank.list_clients()
