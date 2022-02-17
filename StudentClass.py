from datetime import date

class Student:

    def __init__(self, StudentID, Name, DOB, Classification):
        self.__StudentID = StudentID
        self.__Name = Name
        self.__DOB = DOB
        self.__Classification = Classification
        self.__age = 0
        self.__reg_date = 0
        
    def set_studentID(self, StudentID):
        self.__studentID = StudentID

    def calculate_age(self):
        today = date.today()
        self.__age = today.year - int(self.__DOB.split('/')[2])



    def set_classification(self):
        if self.__Classification == "Sr":
            return "Registration for senior is from 11/01 to 11/03"
        elif self.__Classification == "Jr":
            return "Registration for juniors is from 11/04 to 11/06"
        elif self.__Classification == "S":
            return "Registration for sophomores is from 11/07 to 11/09"
        elif self.__Classification == "F":
            return "Registration for freshmen is from 11/10 to 11/12"
        else:
            return "No registration dates are avaliable."

    
    def get_StudentID(self):
        return self.__StudentID
    
    def get_Name(self):
        return self.__Name
    
    def get_DOB(self):
        return self.__DOB
    
    def get_Classification(self):
        return self.__Classification