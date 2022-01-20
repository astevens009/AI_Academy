import math

def compute_kinetic(mass, velocity):
    kinetic_energy = 1/2 * mass * math.pow(velocity, 2)
    return kinetic_energy


def get_mass_velocity(count):
    # NOTE: mv_list will be lists of the masses and velocities
    mv_list = []
    
    # NOTE: get the mass and velocity
    mv_list.append((float(input("Please enter person {} mass: ".format(count+1)))))
    mv_list.append((float(input("Please enter person {} velocity: ".format(count+1)))))
    
    # NOTE: store the mass & velocity in ke_list
    ke_list.append(mv_list)

RNG = 5
subject = ""
if RNG > 1:
    subject = "people"
else:
    subject = "person"

print("\nWelcome to the Kinetic Energy Calculator. Enter the mass and velocity of {} {} an I'll compute their kinetic energy.".format(RNG, subject))

# NOTE: ke_list is a list that will contain lists of the masses and velocities
ke_list = []


# TODO: Create a list of lists to perform calculations on
for count in range(RNG):
    get_mass_velocity(count)
   
# TODO: Use decorators and logging here 
# print("TEST: ke_list = {}\n".format(ke_list))

for mv in ke_list:
    print("The kinetic energy of a person with mass {} and velocity {} is: {}J\n".format(mv[0], mv[1], compute_kinetic(mv[0], mv[1])))



# TODO: Create a dictionary to perform calculations on
