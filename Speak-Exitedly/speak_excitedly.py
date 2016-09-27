
#!/usr/bin/env python -tt
""" File: speak_excitedly.py """


def speak_excitedly(message, num_exclamation=1, capitalize=False):
    """Summary line: Is passed a string and two optional values that determine 
        how much excitment to be added to the string thta is returned.

    Description: Take the string, add exclmation marks, and optionally capitalize.
    """

    message = message + '!' * num_exclamation

    if capitalize:
        message = message.upper()

    return message




if __name__ == '__main__':	
    """Summary line: Show examples of the speak_excitedly function implemntation.

    Description: The program displays different combinations of positional and 
        keyward arguments that cn be passed to the speak_excitedly method.
    """

    print speak_excitedly('I Love Python')
    print speak_excitedly('Keyword arguments are cool', 4)
    print speak_excitedly('I guess Java is okay...', 0)
    print speak_excitedly("Let's go bears", 2, True)



