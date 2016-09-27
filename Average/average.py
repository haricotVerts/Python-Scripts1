
#!/usr/bin/env python -tt
""" File: average.py """


def average(*numInts):
    """Summary line: Passed unknown number of positional arguments, and	
        then calculate the average of all the numbers.

    Description:  Assumbing only numbers are input, calculate the sum
        or return npone if no values passed.
    """

    if not numInts:
        return None

    x = 0
    for int in numInts:
        x += int 

    return float(x) / float(len(numInts))




if __name__ == '__main__':	
    """Summary line:  Display examples of the average function.

    Description:  The program shows how the function can take a unspecified 
        amount of arguments and retrun the average value.
    """

    print average()
    print average(5)
    print average(6,8,9,11)




