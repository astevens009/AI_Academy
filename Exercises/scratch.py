test_line = "joe 10 15 20 30 40"
test_line2 = "bill 23 16 19 22"

# test_tuple = (test_line[1:])
# test_tuple = tuple(test_line)
#print(test_tuple)

data = test_line.split()
data2 = test_line2.split()

test_dict = {}
test_dict[data[0]] = data[1:]
test_dict[data2[0]] = data2[1:]

# print(test_dict)

for data in test_dict:
    print(data)

