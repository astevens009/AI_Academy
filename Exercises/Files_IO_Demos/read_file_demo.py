# Descriprion:
# Demonstrating the use of file functions in Python

captainfile = open("ship_captains.txt", "r")

# EXAMPLE 1: Reading each line of a file and extracting each word of the line
# for info in captainfile:
#     captain_info = info.split()
#     if captain_info[2] == "Captain" or captain_info[2] == "Commander":
#         print("{} {} {} commands {}".format(captain_info[2], captain_info[1], captain_info[0], captain_info[3]))

# EXAMPLE 2: Using the readline() method
# info_lines_list = captainfile.readlines()
# count = 1
# for line in info_lines_list:
#     captain_info = line.split()
#     print("Line {}: {} {} {} of the {}".format(count, captain_info[2], captain_info[1], captain_info[0], captain_info[3]))
#     count += 1

# captainfile.close()

# EXAMPLE 3: Writing to a file
# captainfile = open("ship_captains.txt", "a")

# print("\nAdding captain...")
# captainfile.write("Saru Bombassa Captain USS Discovery")

# captainfile.close()

# captainfile = open("ship_captains.txt", "r")
# info_lines_list = captainfile.readlines()
# print(info_lines_list[-1])

# captainfile.close()

# EXAMPLE 3a: Using the with clause


# EXAMPLE 4: Using a while loop
captainfile = open("ship_captains.txt", "r")

# Get the initial line
info_line = captainfile.readline()
while info_line:
    captain_info = info_line.split()
    print("{} {} {} of the {}".format(captain_info[2], captain_info[1], captain_info[0], captain_info[3]))

    # Get the next line
    info_line = captainfile.readline()

captainfile.close()