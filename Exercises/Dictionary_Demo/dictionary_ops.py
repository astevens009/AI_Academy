# Description
# Demonstration of Python dictionary operations

# Sample dictionary
fleet_ships = {'NCC1701': 'USS Enperrprise',
               'NCC26517': 'USS Excaliber',
               'NCC26632': 'USS Gandhi',
               'NCC10532': 'USS Horatio',
               'NCC11638': 'USS Agamemnon'
               }

# EXAMPLE 1: Using the del operator
# print("Fleet ships: {}\n\nRemoving the Gandhi...".format(fleet_ships))

# del fleet_ships['NCC26632']
# print("Fleet ships: {}\n".format(fleet_ships))

# EXAMPLE 2: Modifying the value of an element
# print("\nUpdating {}".format(fleet_ships['NCC1701']))
# fleet_ships['NCC1701'] = "USS Enterprise"
# print("Fleet ships: {}\n".format(fleet_ships))

# EXAMPLE 2a: More modifications...
tech_inventory = {'computers': 5,
                  'keyboards': 20,
                  'power cords': 10,
                  'monitors': 15}

print()
print("Inventory: {}".format(tech_inventory))

tech_inventory['computers'] += 10
print("\nModified Inventory: {}\n".format(tech_inventory))