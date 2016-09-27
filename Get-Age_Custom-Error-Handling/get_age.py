
#!/usr/bin/env python -tt
""" File: get_age.py """


def get_age():
    """Summary line: Ask user to input age and return the value if it is valid.

    Description: Reprompt the user if input value is not a digit and raise error 
        if value is out of range
    """

    age = raw_input("How old are you? ")  

    # if input is not a number, repeat
    while not age.isdigit():		   
        print "Invalid intiger? input"
        age = raw_input("How old are you? ") 

    # if inpput is out of range raise an exception
    if int(age) < 0 or 123 < int(age): 
        raise ValueError("The value", age, "Is out of the range 0 to 122")

    return age


def get_age1():
    """Summary line: Ask user to input age and return the value if it is valid.

    Description: Reprompt the user if input value is not a digit and raise error 
        if value is out of range
    """

    age = raw_input("How old are you? ")  

    # if input is not a number, repeat
    while not age.isdigit():		    
        print "Invalid intiger? input"
        age = raw_input("How old are you? ") 

    # if inpput is out of range raise an exception
    if int(age) < 0 or 123 < int(age): 
        raise OutOfRangeError("The value", age, "Is out of the range 0 to 122")

    return age


class OutOfRangeError(ValueError):
    """Summary line: Error for out of range values

    Description: Raise this error if a value is out of a desired numerical range.
    """

    def __init__(self, *value):
        ValueError.__init__(self, *value)
        self.parameter = value

    def __error_String__(self):
        return repr(self.perameter)





if __name__ == '__main__':	
    """Summary line: Test the get age functions.

    Description: The Functions are made to test rasing errors and creating 
        custom error classes.
    """

    print get_age()
    print get_age1()





