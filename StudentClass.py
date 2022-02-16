class Student:
    def __init__(self, StudentID, Name, DOB, classification):
        self.__StudentID = StudentID
        self.__Name = Name
        self.__DOB = DOB
        self.__classification = classification
        
    def set_StudentID( self, StudentID):
        self.__StudentID = StudentID
        
    def set_Name(self, Name):
        self.__Name = Name
        
    def set_DOB(self, DOB):
        self.__DOB = DOB
        
    def set_classification(self, classification):
        self.__classification = classification
        
    def get_StudentID(self):
        return self.__StudentID
    
    def get_DOB(self):
        return self.__DOB
      
    def get_classification(self):
        return self.__classification
    