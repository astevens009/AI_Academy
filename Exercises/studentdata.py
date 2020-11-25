# Exercise 1: Using the text file studentdata.txt write a program that 
# prints out the names of the students that have more than six quiz scores



# Algorithm 1:
# Extract the lines and separate the student name from the quiz scores in 
# a dictionary where the key = student name and the value (list) = quiz 
# scores; count the number of elements in the tuple


from Exercises.student_quiz_methods import greater_than_six


file = "E:/Kemet_DriveB/Recovery_DriveB/Recovery2018_DriveB/Files 2018/Practice & Training/AI Academy/Course_Examples/Files_Demo/Excercises/studentdata.txt"
# with open(file) as student_info:
#     quiz_line = student_info.readlines()

#     # TODO: Create a dictionary where the key is the student name and the 
#     # value is a list of quiz scores
#     quiz_scores = {}
    
#     # TODO: Convert the line into a list
#     for line in quiz_line:
#         quiz_data = line.split()

#         # TODO: Add the data to the dictionary
#         quiz_scores[quiz_data[0]] = quiz_data[1:]

#     # print("TEST: {}".format(quiz_scores))

#     # TODO: Print the name of students that have more than six quiz scores
#     for student in quiz_scores:
#         if len(quiz_scores[student].get()) > 6:
#             print(student)



# Algorithm 2:
# Count the number of elements in each line; if there are more than 7 items (the student name + 6 quiz scores), return the student name

with open(file) as student_info:
    quiz_lines = student_info.readlines()
    greater_than_six(quiz_lines)
    