import student
from datetime import datetime
"""
function to write error log file
Input: errormessage
Output: none
"""
def write_to_error_log(error_message):
    try:
        #open log file
        log_file = open("error_log.txt", "a")
        #write error message to log file
        log_file.write(f"{datetime()}: {error_message}\n")
        #Close log file
        log_file.close()
    except Exception as err:
        print(err)

        return
def load_students(file_name):


    list_of_students =  []
    students_file =  open(file_name, "r")
    line_number = 1
    next(students_file)
    
    for line_of_data in students_file:
        line_number += 1
        student_data = line_of_data.split(",")
        try:
            if len(student_data) != 6:
                raise Exception(f"There is an error in your data file on line {line_number}")
        except Exception as err:
            print(str(err))
            continue

        try:
            first_name = student_data[0]
            last_name = student_data[1]
            major = student_data[2]
            credit = student_data[3]
            gpa = student_data[4]
            ID_number = student_data[5]
        except:
            print(f"Error:{err} on line {line_number}")
            continue
        
        new_student = student.Student(first_name , last_name , major , credit , gpa , ID_number)
        list_of_students.append(new_student)
    students_file.close()
    return list_of_students
def main():
    list_of_students = load_students("student_csv")
    for students in list_of_students:
        students.print_info()
    
    
main()
