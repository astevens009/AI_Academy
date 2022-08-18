# Description:
# Demonstration of aliasing and copying in dictionary objects

species = {'human': 'Sisko', 'bajoran': 'Kira', 'cardassian': 'Dukat', 'klingon': 'Worf'}

# EXAMPLE 1: Using an alias and changing one of the dictionary elements
# print(species)
# print("Klingon: {}".format(species['klingon']))
# humanoids = species

# print(humanoids is species)

# # Changing item in the dictionary
# humanoids['klingon'] = 'Martok'
# print()
# print("Klingon: {}".format(species.get('klingon')))

# EXAMPLE 2: Creating a copy of the dictionary
humanoids = species.copy()
humanoids['klingon'] = 'Martok'
print(species)
print(humanoids)