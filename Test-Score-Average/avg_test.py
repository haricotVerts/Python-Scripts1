
#!/usr/bin/env python -tt
""" File: avgTest.py """


def calAverage(testScores):
    """Summary line: Computes the average of a group of integers.

    Description: This program will takes a group of integers seperated 
        by commas and return the average of the values.
    """

    examSum = sum(testScores)
    return (examSum / len(testScores))




if __name__ == '__main__':
    """Summary line: Computes the average of a group of integers.

    Description: This program will takes a group of integers seperated 
        by commas and return the average of the values. The input string is 
        split based on comma, than has the null chars removed. The list of 
        numbers is then passed to calAverage to create the average.
    """

    null_Chars = ['', ' ']


    print "\nThis program computes the average of three exam scores."
    examScores  = raw_input('Enter the scores seperated by commas (ex 5,2,1):')

    examScores  = [x for x in examScores.split(',') if x not in null_Chars]

    print "%.2f" % calAverage([float(x) for x in examScores])



