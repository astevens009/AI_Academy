# Description:
# Module that defines the methods to process the studentdata.txt file

def greater_than_six(quizzes_list):
    print("The student(s) with more than 6 quizzes is/are: ")
    for data in quizzes_list:
        quiz_data = data.split()

        # Count the number of elements in the quiz_data list and 
        # subtract the first element of the list (which is the student's 
        # name)
        if (len(quiz_data) - 1) > 6:
            print(quiz_data[0])