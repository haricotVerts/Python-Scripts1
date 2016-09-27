
#!/usr/bin/env python -tt
""" File: pascal.py """


def isFloat(value):
    """Summary line: Returns true if the value is a float, and else false

    Description: If the value passed can be a float the a true is returned, and 
        if not an exception is raised and false is returned
    """

    try:
        float(value)
        return True

    except ValueError:
        return False




if __name__ == '__main__':
    """Summary line: Calculates the sum of a list of values

    Description: This program uses the sys package to capture command
        line arguments, filters out the non digits, and retiurns the 
        sum of all the values.
    """

    from   sys import argv
    import re


    values      = argv
    values_sum  = [float(_) for _ in values if _.isdigit() or isFloat(_)]

    print  sum(values_sum)




