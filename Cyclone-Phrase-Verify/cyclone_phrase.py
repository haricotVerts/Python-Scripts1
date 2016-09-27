
#!/usr/bin/env python -tt
""" File: cyclonePhrase.py """	


def cyclonePhrase(phrase):
    """Summary line: Check if a input value is a cyclone phrase

    Description:  Take the input phrase and create a single string without spaces. 
        Then align the phrase so the cyclone terms are in a linear index. Then 
        check the values to see if the characters are in alphabetical order.
    """

    phrase =  phrase.lower()							
    phrase =  "".join(phrase.split()) 			
    a      =  [' ']*len(phrase)									

    # Index order transform 123456789, => 192837465 
    firstHalf   =  phrase[0  :  (len(phrase)+1)/2 : 1 ]		  
    secondHalf  =  phrase[-1 : -(len(phrase)+1)/2 : -1]
    a[0::2]     =  firstHalf[::1]					
    a[1::2]     =  secondHalf[::1]	
    
    # alphabetical order check
    for x in range(0, len(a) - 1):					
        if a[x] > a[x+1]:
            return False

    return True




if __name__ == '__main__':
    """Summary line: Check if a input value is a cyclone phrase

    Description:  Pass the users string into cyclonePhrase and print the result.
    """

    phraseIn = raw_input('Input a phrase > ')

    print cyclonePhrase(phraseIn)

