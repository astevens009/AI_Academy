from SF_Personnel import Starfleet_Personnel, Student, Instructor

# region Instantiate the Student class and print data

sisko = Student(10001, 'Lieutenant', 'Sisko', 'Benjamin', 'Earth', ['Intro to Calculus', 'Archeology 101', 'Leadership Essentials'], 'Archeology', 'N/A', (0.0, 0.0, 0.0))
    
dax = Student(10002, 'Lieutenant Commander', 'Dax', 'Jadzia', 'Trill', ['Xenobiology', 'Stellar Cartography', 'Leadership Essentials'], 'Xenolinguistics', "Chemistry", (0.0, 0.0, 0.0))

bashir = Student(10003, 'Ensign', 'Bashir', 'Julian', 'Earth', ['Intro to Calculus', 'Physics 101', 'Xenobiology'], 'Medical', 'Betazoid Art', (0.0, 0.0, 0.0))


print(sisko)
print(dax)
print(bashir)

# Modify Student Data
update_courses = sisko.get_academy_courses()

# TODO: Make printing the course list a method in the Student class
# print("\nCurrent Courses for {}: ({})".format(sisko.get_name(), sisko.get_starfleetID()))
# for course in update_courses:
#     print("\t", course)
sisko.show_student_courses()
    
update_courses.append('Bajoran Art')
update_courses.append('Trigonometry')
sisko.set_academy_courses(update_courses)
sisko.show_student_courses()

# endregion

# region Instantiate the Instructor class and print data

uhura = Instructor(50001, 'Captain', 'Uhura', 'Nyota', 'Earth', 'Engineering', ['Warp Propulsion', 'Xenolinguistics', 'Starship Mechanics'])
print(uhura)
uhura.show_curriculum()

scott = Instructor(50002, 'Captain', 'Scott', 'Montgomery', 'Earth', 'Engineering', ['Advanced Warp Propulsion', 'Mechanics & Computers', 'Thermodynamics 101'])
print(scott)
scott.show_curriculum()

# TODO: Make a method in the Instructor class that updates the curriculum
curriculum = scott.get_academy_courses()
curriculum.append('Dilithium Intermix Mechanics')
scott.set_academy_courses(curriculum)
scott.show_curriculum()

# endregion Instructor class