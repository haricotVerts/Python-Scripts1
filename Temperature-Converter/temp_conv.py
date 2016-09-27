
#!/usr/bin/env python -tt
""" File: tempConv.py """


# This method takes a celcius intiger and conferts it to farenhight
def celToFer(celcius):	
    """Summary line: Convert celcius to freinheight

    Description: Passed an int and return an int each representing the 
        temprature in the respective units.
    """

    freinheight = ((celcius*9.0)/5.0)+32.0
    return freinheight


# This method takes a farengehight intiger and conferts it to celcius
def ferToCel(freinheight):	
    """Summary line: Convert freinheight to celcius

    Description: Passed an int and return an int each representing the 
        temprature in the respective units.
    """

    celcius = ((freinheight - 32.0)*5.0)/9.0
    return celcius

	
# This method takes a kelvin input and converts it to cel
def kelToCel(kelvin):
    """Summary line: Convert kelvin to celcius

    Description: Passed an int and return an int each representing the 
        temprature in the respective units.
    """

    celcius = kelvin - 273.15
    return celcius

	
# This method takes a kelvin input and converts it to cel
def celTokel(celcius):
    """Summary line: Convert celcius to kelvin

    Description: Passed an int and return an int each representing the 
        temprature in the respective units. 
    """

    kelvin = celcius + 273.15
    return kelvin




if __name__ == '__main__':
    """Summary line: Take input from user and return a converted value.	Using 
        either kelvin celcius or ferinneight.

    Description: Prompt user for input, split the srting value and remove null spaces.
        The input string values are decoded and then the int value is passed to the desired 
        method.
    """



    print "\nThis program converts degrees celcius and ferinhight."
    print """
Enter the current units followed by the ones desifred then the current value
For Example to convert 32 deg celcius to kelvin input 'C K 32'"""

    lookUpTable   = ['c', 'C', 'f', 'F', 'k', 'K']

    toConvert     = raw_input('>')
    toConvertSort = toConvert.split(' ')
    toConvertSort = [x for x in toConvertSort if x is not '']

    while (toConvertSort[0] and toConvertSort[1] in lookUpTable):
        # c k c to f
        if toConvertSort[0] in lookUpTable[0:2]:
            if toConvertSort[1] in lookUpTable[4:6]:
                kelvin = celTokel(int(toConvertSort[2]))
                print "%.1f celcius is %.1f kelvin\n" % (int(toConvertSort[2]), kelvin)

            elif toConvertSort[1] in lookUpTable[2:4]:
                freinheight = celToFer(int(toConvertSort[2]))
                print "%.1f celcius is %.1f freinheight\n" % (int(toConvertSort[2]), freinheight)	

        # k c # k f 
        elif toConvertSort[0] in lookUpTable[4:6]:
            if toConvertSort[1] in lookUpTable[0:2]:
                celcius = kelToCel(int(toConvertSort[2]))
                print "%.1f kelvin is %.1f celcius\n" % (int(toConvertSort[2]), celcius)

            elif toConvertSort[1] in lookUpTable[2:4]:
                celcius = kelToCel(int(toConvertSort[2]))
                freinheight = celToFer(int(celcius))
                print "%.1f kelvin is %.1f freinheight\n" % (int(toConvertSort[2]), freinheight)

        # f c  # f k 
        elif toConvertSort[0] in lookUpTable[2:4]:
            if toConvertSort[1] in lookUpTable[0:2]:
                celcius = ferToCel(int(toConvertSort[2]))
                print "%.1f freinheight is %.1f celcius\n" % (int(toConvertSort[2]), celcius)

            elif toConvertSort[1] in lookUpTable[4:6]:
                celcius = ferToCel(int(toConvertSort[2]))
                kelvin = celTokel(int(celcius))
                print "%.1f freinheight is %.1f kelvin\n" % (int(toConvertSort[2]), kelvin)		


        toConvert     = raw_input('>')
        toConvertSort = toConvert.split(' ')
        toConvertSort = [x for x in toConvertSort if x is not '']






