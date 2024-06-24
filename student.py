class Student():


    def __init__(self , first_name , last_name , major , credit , gpa , ID_number):

        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = float(credit)
        self.__gpa = float(gpa)
        self.__ID_number = int(ID_number)

    def get_first_name(self):
        return self.__first_name
    def set_new_first_name(self, new_name):
        try:
            self.__first_name = new_name
        except:
            print("Error: Enter the new name\n")
    def get_last_name(self):
        
        return self.__last_name
    def set_new_last_name(self, new_last_name):
        try:
            self.__last_name = new_last_name
        except:
            print("Error: Enter the new name\n")
    def get_major(self):
        return self.major
    def set_new_major (self, new_major):
        try:
            self.__major = new_major
        except:
            print("Error: Enter the new major\n")
    def get_credit(self):
        return self.__credit_hours
    
    def update_new_credit(self, new_credit):
        try:
            self.__credit_hours = new_credit + self.__credit_hours
        except:
            print("Error: Enter your new amount of credits as a number\n")
    def get_gpa(self):
        return self.__gpa
    def set_new_gpa(self, new_gpa):
        try:
            self.__gpa = new_gpa
        except:
            print("Error: Enter you're new gpa as a number\n")
    def get_Id_number(self):
        return self.__ID_number
    
    def get_class_level(self):
        if self.__credit_hours <= 30:
            return "Freshman"
        elif self.__credit_hours <= 60:
            return "Sophmore"
        elif self.__credit_hours <= 90:
            return "Junior"
        else:
            return "Senior"

    def print_info(self):
        print(f"Name:{self.__first_name} {self.__last_name}   Major:{self.__major}    Credits:{self.__credit_hours}   gpa:{self.__gpa},   ID:{self.__ID_number}")
    
    
    
