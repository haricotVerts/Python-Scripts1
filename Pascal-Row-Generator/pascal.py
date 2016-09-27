
#!/usr/bin/env python -tt
""" File: pascal.py """


def pascRowNext(currentRow):
    """Summary line: Takes a row (n) from the pascal table and returns row (n + 1).

    Description: This function is passed a list of the row, and returns a list
        of the next row.
    """

    # Check for an empty list
    if not currentRow:					
        return [1]

    # Check row sum to see if it is a valid row
    if sum(currentRow) != 2**(len(currentRow) - 1):
        raise Exception('The input list is not part of the pascal sequence')

    # Add 0, sum row and inverted row
    currentRow.append(0)				 
    currentInverse = currentRow[::-1]	 

    return [int1 + int2 for int1, int2 in zip(currentRow, currentInverse)]	



if __name__ == '__main__':
    """Summary line: Takes a list input from the pascal sequence, and returns
        the next list in the pascal sequence.

    Description: This program will take in input string, and create a list based off
        commas. The list of strings is then converted to list of integers and pased to 
        pascRowNext
    """
    pascalRow = raw_input("Input a pascal triangle row(ex. 1,2,1) > ")
    pascalRow = pascalRow.split(',')
    pascalRow = [int(x) for x in pascalRow]		


    print " next row is", pascRowNext(pascalRow)


# This program takes a pascal triangle row in list form and outputs the 
# next itteration of the triangle






