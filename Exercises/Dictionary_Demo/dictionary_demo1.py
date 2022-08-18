# Description
# Python Dictionaries

# EXAMPLE 1: Building from an empty dictionary
# TODO: Create an empty dictionary
eng2sp = {}

# TODO: Add items to the dictionary
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'

# print(eng2sp)

# EXAMPLE 2: Create a dictionary in one line
fleet_ships = {'NCC1701': 'USS Enterprise',
               'NCC26517': 'USS Excaliber',
               'NCC26632': 'USS Ganghi'}

print("Starfleet Ships: {}".format(fleet_ships))
print()

# EXAMPLE 3: Retrieve a value
ship1 = fleet_ships['NCC26517']
print("NCC26517 ship name: {}\n".format(ship1))
