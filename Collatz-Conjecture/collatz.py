
#!/usr/bin/env python -tt
""" File: collatz.py """


def collatz_Seq(currentInt):
    """Summary line: Determine the collatz step value and sequence.

    Description: Take a intiger input value and using the collatz theorem 
        calculate the steps needed to reach one. And save the intermediate steps
        in a list, Then return the value and list.
    """

    totalSteps    = int(0)
    intSequence   = []

    while (currentInt > 1):
        if (currentInt % 2) == 0:				
            currentInt /=  2
        else:									 
            currentInt = (currentInt*3) + 1

        intSequence.append(currentInt)			
        totalSteps += 1

    return  totalSteps, intSequence


def collatz(currentInt):
    """Summary line:  Determine the collatz step value.

    Description: Take a intiger input value and using the collatz theorem 
        calculate the steps needed to reach one. and return the value  
    """
	
    totalSteps    = int(0)
    intSequence   = []

    while (currentInt > 1):
        if (currentInt % 2) == 0:				 
            currentInt /=  2
        else:									 
            currentInt = (currentInt*3) + 1

        totalSteps += 1

    return  totalSteps




if __name__ == '__main__':
    """Summary line: Determine the collatz theorem for an intiger.
	
    Description:   Take an input of an intiger and determin the steps to reach one
        using the collatz theorem. Then optionally display the intermediat steps. 
        Lastly the longest sequence is displayed.
    """
    
    print    "This app determines the number terms to satisfy collatz's theorm"
    startInt = raw_input("Enter a number: ")

    totalSteps, intSequence = collatz_Seq(int(startInt))
    print """You began with %d, and 
it took %d steps to reach one (:""" % (int(startInt), totalSteps)	 										


    answer = raw_input("Do you want to print the whole sequence(Y/N): ")

    if (answer == 'y' or answer == 'Y'):
        if len(intSequence) > 100:
            answer = raw_input("Are you sure it is above 100 steps long(Y/N): ")

            if (answer == 'y' or answer == 'Y'):
                print intSequence

        else:
            print intSequence



    maxStep                  = {}			 	   
    maxStep["highStart"]     = int(startInt)
    maxStep["highStepCount"] = totalSteps

    boundInt = int(startInt) - 1

    # Check all values to find the longest sequence
    while boundInt > (int(startInt) - 1 ) / 2:		 
        currentInt = boundInt
        totalSteps = int(0)

        totalSteps = collatz(int(currentInt))

        if  maxStep["highStepCount"] < totalSteps:	
            maxStep["highStart"]     = int(boundInt)
            maxStep["highStepCount"] = totalSteps

        boundInt -= 1

    print """\nOf all the the numbers below or equal to %d, %d has the 
longest total number of iterations before reaching one, taking %d steps
""" % (int(startInt), maxStep["highStart"], maxStep["highStepCount"])









 





