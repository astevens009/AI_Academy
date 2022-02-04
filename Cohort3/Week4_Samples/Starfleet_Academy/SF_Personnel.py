class Starfleet_Personnel:
    def __init__(self, sfID, rank, last_name, first_name, home_planet):
        self.__starfleetID = sfID
        self.__starfleet_rank = rank
        self.__last_name = last_name
        self.__first_name = first_name
        self.__home_planet = home_planet
        
        
    def __str__(self):
        starfleet_info = "\nPERSONNEL INFORMATION:\nStarfleet ID: {}\nStarfleet Rank: {}\nName: {}, {}\nHome Planet: {}\n".format(self.__starfleetID, self.__starfleet_rank, self.__last_name, self.__first_name, self.__home_planet)
        
        return starfleet_info
    
    
    
    def get_starfleetID(self):
        return self.__starfleetID
    
    
    
    def get_starfleet_rank(self):
        return self.__starfleet_rank
    
    
    
    def get_name(self):
        full_name = self.__last_name + ", " + self.__first_name
        return full_name
    
    
    def get_home_planet(self):
        return self.__home_planet
    
    
    def set_starfleetID(self, sfID):
        self.__starfleetID = sfID
    
    
    
    def set_starfleet_rank(self, rank):
        self.__starfleet_rank = rank
    
    
    
    def set_name(self, f_name, l_name):
        self.__first_name = f_name
        self.__last_name = l_name
    
    
    
    def set_home_planet(self, planet):
        self.__home_planet = planet
    
    



class Student(Starfleet_Personnel):
    def __init__(self, sfID, rank, last_name, first_name, home_planet, academy_courses, course_major, course_minor, grades):
        """Provide Starfleet Academy student information

        Args:
            academy_courses (list): All courses taken in the academic year
            course_major (string): The student's selected major course while attending Starfleet academy
            course_minor (string): The student's selected minor course while attending Starfleet academy
            grades (tuple): Grades; to be associated with the course(s)
        """
        super().__init__(sfID, rank, last_name, first_name, home_planet)
        self.__academy_courses = academy_courses # NOTE: make this a dictionary?
        self.__course_major = course_major
        self.__course_minor = course_minor
        self.__grades = grades      # NOTE: make this a tuple
        
        
    def __str__(self):
        info = super().__str__()
        student_info = "\nACADEMY FACULTY INFORMATION:\n" + info + "\nCOURSE REGISTRATION:\n\tCourse Major: {}\n\tCourse Minor: {}\n".format(self.__course_major, self.__course_minor)
        
        return student_info
    
    
    
    def get_academy_courses(self):
        return self.__academy_courses
    
    
    
    def get_course_major(self):
        return self.__course_major
    
    
    
    def get_course_minor(self):
        return self.__course_minor
    
    
    
    def get_grades(self):
        return self.__grades
    
    
    
    def set_academy_courses(self, courses):
        print("Modifying courses...")
        self.__academy_courses = courses
    
    
    
    def set_course_major(self, major):
        print("Modifying course major...")
        self.__course_major = major
    
    
    
    def set_course_minor(self, minor):
        print("Modifying course minor...")
        self.__course_minor = minor
    
    
    
    def set_grades(self, grades):
        self.__grades = grades
        
        
        
    def show_student_courses(self):
        print("\nCurrent Courses for {}: ({})".format(self.get_name(), self.get_starfleetID()))
        for course in self.__academy_courses:
            print("\t", course)
            
        print()
    
    
    
    
    
    
    # TODO: Create a function to format and print the list of courses and their subsequent grades
    
    
    
class Instructor(Starfleet_Personnel):
    def __init__(self, sfID, rank, last_name, first_name, home_planet, department, academy_courses):
        super().__init__(sfID, rank, last_name, first_name, home_planet)
        self.__sf_department = department
        self.__academy_courses = academy_courses    # list: courses that the instructor will teach

    def __str__(self):
        info = super().__str__()
        instructor_info = info + "\nAcademy Instructor Information:\n\tDepartment: {}\n".format(self.__sf_department)
        
        return instructor_info
    
    def get_department(self):
        return self.__sf_department
    
    
    def get_academy_courses(self):
        return self.__academy_courses
        

    
    def set_department(self, dept_name):
        print("Modifying department...")
        self.__sf_department = dept_name
    
    
    def set_academy_courses(self, academy_courses):
        print("Modifying course curriculum...")
        self.__academy_courses = academy_courses
        
        
    def show_curriculum(self):
        print("CURRICULUM FOR {}:\n".format(self.get_name()))
        for course in self.__academy_courses:
            print("\t", course)
            
        print()
        


# TODO: Create a objects for the course, instructor and maybe assignments

if __name__ == '__main__':
    sisko = Student(10001, 'Lieutenant', 'Sisko', 'Benjamin', 'Earth', ['Intro to Calculus', 'Archeology 101', 'Leadership Eessntials'], 'Archeology', 'N/A', (0.0, 0.0, 0.0))
    print(sisko)
    
    uhura = Instructor(50001, 'Captain', 'Uhura', 'Nyota', 'Earth', 'Engineering', ['Warp Propulsion', 'Xenolinguistics', 'Starship Mechanics'])
    print(uhura)
    