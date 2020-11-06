# Exercise:
# Write a function the takes a string as a parameter and returns a new string that is the reverse of the old string.

# Base case: A string with length = 1

def reverse_string(listStr, outStr = ""):
    revList = listStr

    if len(revList) == 1:
        outStr += outStr.join(revList)
        return outStr
    else:
        # recursive case...
        outStr += outStr.join(revList[-1])
        revList.remove(revList[-1])
        return reverse_string(revList, outStr)
     
# TODO: Get the string from the user
input_string = input("Please enter a word or sentence: ")

# TODO: Convert the string to a list to be used in the recusrive call
str_list = list(input_string)

# TODO: Reverse the string and display it
print("The reverse of the string is: {}".format(reverse_string(str_list)))

