# Description:
# Demonstrating how to open and write to a new file

captains_file = open("ship_captains.txt", "r")
update_captains = open("captain_names.dat", "w")

# Get initial line
line_info = captains_file.readline()
while line_info:
    captain_data = line_info.split()
    name_info = captain_data[0] + ", " + captain_data[1] + "\n"
    update_captains.write(name_info)

    # Get next line; when there are no more lines the loop terminates
    line_info = captains_file.readline()

update_captains.close()
captains_file.close()
