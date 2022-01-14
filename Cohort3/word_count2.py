from collections import Counter

# TODO: Add code to use Counter


def count_words(wd_list):
    wd_dict = {}
    # wd_count = 0

    for word in wd_list:
        if word in wd_dict:
            wd_dict[word] += 1
        else:
            # Add the word to the dictionary and set it's count to 1
            wd_dict[word] = 1

    return wd_dict



def show_word_count(list_dict):
    for wd in list_dict:
        print("Word: {}, Count: {}\n".format(wd, list_dict[wd]))

print()

list1 = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

list2 = ['jack', 'be', 'nimble', 'jack', 'be', 'quick', 'jack', 'jumps', 'over', 'the', 'candlestick']


# Take the two lists provided and count the frequency of each word in each list.
# Create a dictionary with the key equal to each unique word and count as the value.

list1_dict = count_words(list1)
list2_dict = count_words(list2)

show_word_count(list1_dict)
print()
show_word_count(list2_dict)

# Using set intersection()
# Print off a list of words that are in both lists.
list1_set = set(list1)
list2_set = set(list2)

# print("{}\n{}\n".format(list1_set, list2_set))
print("\nWords that appear in both lists: {}".format(list1_set.intersection(list2_set)))

# Using set difference()
# Print off a list of words that are in the first list and not the second.
print("\nWords that appear in first list but not the second: {}".format(list1_set.difference(list2_set)))

# Print off a list of words that are in the second list and not in the first.
print("\nWords that appear in second list but not the first: {}".format(list2_set.difference(list1_set)))