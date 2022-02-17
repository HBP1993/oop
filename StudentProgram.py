
import StudentClass as s

def main():
    
    
     
    Student_info = s.Student(555, 'Yash', '2/2/2002', 'Sr')

    
    Student_info.calculate_age()
    Student_info.set_classification()

    
    print(f"Student's ID: {Student_info.get_StudentID()}, Student's Name: {Student_info.get_Name()}, Student's DOB, {Student_info.get_DOB()}, Student's Class: {Student_info.get_Classification()}")
    
    

main()