
#!/usr/bin/env python -tt
""" File: anagrammer.py """


def anagramCheck(word_One, word_Two):
    """Summary line: Chectks if two input strings are annograms.

    Description: Two strings are input and a boolian is returned. 
        Return false if they are not the same length.
        The function checks word two for word one character membership.
        If there is a character match between words the character is removed.
        The words are annograms if all the characters match and a empty string 
        is remaining.
    """

    if len(word_One) != len(word_Two):
        return False


    word_One = [x for x in word_One]
    word_Two = [x for x in word_Two]

    for letter in word_One:
        if letter in word_Two:
            word_Two.remove(letter)

    if not word_Two: 
        return True

    return False




if __name__ == '__main__':	
    """Summary line:  Look through a dictionary file and check for annograms.

    Description: Each dictionary line is read, and the wod is passed to the 
        anagramCheck function to where a true of false is returned. 
    """

    print    "This program asks for a single word and returns the words anagrams"
    inString = raw_input("Enter a word: ")


    count2 = 0; 
    with open('dict.txt', 'r') as f:	
        lines = f.readlines()

        for word in lines:
            if anagramCheck(inString, word.strip('\n')):
                print "%s and %s are anagrams" % (lines[count2].strip('\n'), inString)
                print "%s is on line %d of the file \n" % (lines[count2].strip('\n'), count2) 

            count2 += 1






