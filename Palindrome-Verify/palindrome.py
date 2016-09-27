#!/usr/bin/env python -tt
""" File: palindrome.py """


"""Summary line: Checks if a string is a palindrome.

Description: This program will take a string input from a user and 
    will return true if the string is a palindrome. 
"""


print "\nThis program determines if a phrase is a palindrome."
print "Type ^c to exit.\n"


while True:
    try:
        phrase 	      =  raw_input("Please enter a phrase: " )
        phrase_Concat =  ''.join(phrase.split(' '))

    except Exception as KeyboardInterrupt:
        print("\nClosing the application. \n")
        break

    else:
        if phrase_Concat == phrase_Concat[::-1]:
            print "Yes!, \"%s\" is a palindrome.\n" % (phrase)

        else:
            print "No!, \"%s\" is not a palindrome.\n" % (phrase)



