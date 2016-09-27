
#!/usr/bin/env python -tt
""" File: acronym.py """


"""Summary line: Turns a string into an acronym.

Description: This program will take a string input from a user and 
    will return the acronym version of the string phrase. The acronym
    is found by spliting the string into a list, removing null characters, and 
    extracting the 0 index on each word in the list.
"""


print "\nThis program determines the acronym of a phrase" 
print "Type ^c to exit.\n"


while True:
    try:
        phrase = raw_input('Enter a phrase, ie "Fucked up beyond all recognition": ')

    except Exception as KeyboardInterrupt:
        print("\nClosing the application. \n")
        break

    else:
        phraseSplit = phrase.split(' ')				
        acronym     = ''.join([x[0] for x in phraseSplit if x is not ''])

        print '%s is the acronym for "%s" \n' %  ((acronym).upper(), phrase)	






