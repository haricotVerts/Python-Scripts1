
#!/usr/bin/env python -tt
""" File: distConv.py """


def mile_Kilo(miles):	
    """Summary line: Converts miles to kilometers.

    Description: Passed a int|float value representing distance in miles and 
        returnes the equivalent kilometer value.
    """

    kilometer =  miles/.62137

    return kilometer


def kilo_Mile(kilometer):	
    """Summary line: Converts kilometers to miles.

    Description: Passed a int|float value representing distance in kilometers and 
        returnes the equivalent mile value.
    """

    miles =  kilometer*.62137

    return miles





if __name__ == '__main__':	
    """Summary line: Convert miles and kilometers distances.

        Description: This program will take the user input, split the string, 
        remove extra null spaces, then call the convertion function and return
        its value.
    """

    print "\nThis program converts degrees miles and kilometers.\n"
    print """Enter M for miles or K for kilometers followed by 
a space and the distance value to convert ie (M 32) 
is 32 miles"""

    loop_Up_Table   = ['m', 'M', 'k', 'K']


    to_Convert      = raw_input('>')	
    to_Convert_Sort = [_ for _ in to_Convert.split(' ') if _ is not '']


    while (to_Convert_Sort[0] in loop_Up_Table):
        if to_Convert_Sort[0] in loop_Up_Table[0:2]:
            kilometer = mile_Kilo(float(to_Convert_Sort[1]))
            print "%.1f miles is %.1f kilometers\n" % (float(to_Convert_Sort[1]), kilometer)

        elif to_Convert_Sort[0] in loop_Up_Table[2:4]:
            miles = kilo_Mile(float(to_Convert_Sort[1]))
            print "%.1f kilometers is %.1f miles\n" % (float(to_Convert_Sort[1]), miles)


        to_Convert      = raw_input('>')	
        to_Convert_Sort = [_ for _ in to_Convert.split(' ') if _ is not '']







