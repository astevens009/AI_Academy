# Description:
# Demonstrating Python dictionary methods

tech_inventory = {'CPUs': 5,
                  'keyboards': 10,
                  'power cords': 20,
                  'monitors': 15,
                  'mice': 5}

# EXAMPLE 1: Iterating over dictionary keys
# NOTE: the order in which we get the keys is not defined
# for component_key in tech_inventory.keys():
#     # print("Key \'", component_key, "\' maps to value: ", tech_inventory[component_key])
#     print("Key \'{}\' maps to value: {}".format(component_key, tech_inventory[component_key]))

# EXAMPLE 2: Alternate (omit the direct call to the .keys() method)
# for component_key in tech_inventory:
#     # print("Key \'", component_key, "\' maps to value: ", tech_inventory[component_key])
#     print("Key \'{}\' maps to value: {}".format(component_key, tech_inventory[component_key]))

# EXAMPLE 3: Display dictionary values (as a tuple)
print(tech_inventory)
print(list(tech_inventory))
print(tech_inventory.values())

# EXAMPLE 4: Using in and not in
# if 'CPUs' in tech_inventory:
#     print("Number of CPUs: {}".format(tech_inventory['CPUs']))
# else:
#     print("There are no CPUs")

# if 'computer' not in tech_inventory:
#     print("\nThere are no computers in the inventory")
# else:
#     print("\nThere are {} computers in the inventory".format(tech_inventory['computer']))

# EXAMPLE 5: Using the get() method
# item = 'keyboards'
# print("\nThere are {} {} in the inventory".format(tech_inventory.get(item), item))

# EXAMPLE 5a: Using get() with second (alternative) parameter
# item = 'printers'

# Prints 0 if the item is not in the dictionary
# print("\nThere are {} {} in the inventory\n".format(tech_inventory.get(item, 0), item))