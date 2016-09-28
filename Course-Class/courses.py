
#!/usr/bin/env python -tt
""" File: courses.py """


class Course:	
    """Summary line:  The class will create a object with perameters associated with a university class

    Description:  Course creates a object that represents a university course. It controls the attendance, 
        instructors, and desctiption.
    """

    def __init__(self, department="N/A", number="N/A", title="N/A", *instructors):
        self.department       = department  
        self.number           = number      
        self.title            = title		  
        self.students         = set()		  
        self.attendance_List  = {}
        self.instructors_List = instructors


    def mark_attendance(self, students):
        """Summary line: Mark if a students attendance in a dictionary

        Description:  For every student in list, ask the user to input weither they
            are absent or present.
        """
        
        print "type a for absent or p for present"

        for x in students:
            print x, "?"
            status = raw_input("> ")

            if 'p' in status:
                self.attendance_List[x] = 'present'
                
            elif 'a' in status:
                self.attendance_List[x] = 'absent'
            
            else:
                self.attendance_List[x] = 'N/A'

            
    def is_present(self, student):
        """Summary line:  Check if a student is present

        Description:  The attendance list dictionary is used to look up a students
            attendance and if present true is returned
        """
        
        try:
            if self.attendance_List[student] == 'present':
                return True
            
        # If a key that is not present is attempted to be accesed
        except KeyError:
            return False
        
        else:
            return False


    def __le__(self, other_Course):
        """Summary line: Use magic method to check a class prerequsit

        Description: If a class object has a number that is greater than another it is not 
            determined to be a prerequsit. If the class number is smaller than another class    
            the smaller is a prerequsit.
        """
        
        # Remove the leffers from the ourse number 110A -> 110
        selfNum  = "".join([digit for digit in self.number if digit.isdigit()])
        otherNum = "".join([digit for digit in other_Course.number if digit.isdigit()])
        
        return selfNum <= otherNum


        
        
if __name__ == '__main__':
    """Summary line:   Show examples of the Course class.

    Description:   Examples of the different methods that the course class contains.
    """
    
    ece_112 = Course("ECE", "112", 'Communication electronics', "Laft", "Seipal")
    eec_100 = Course()
    
    # Add students to the list for the class
    ece_112.students.update(["zach", "mack"])
    ece_112.students.add("jack")
    print ece_112.students
    
    # Mark Attendance
    ece_112.mark_attendance(ece_112.students)
    print ece_112.attendance_List

    # check attendance_List
    print ece_112.is_present('zach')
    print ece_112.is_present('mack')
    print ece_112.is_present('jack')
    
    # Check if prerequesit
    print ece_112 <= eec_100
    print eec_100 <= ece_112
    
    # Display the list of instructors
    print ece_112.instructors_List











