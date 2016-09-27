
#!/usr/bin/env python -tt
""" File: make_Table.py """


def make_Table(key_justify='left', value_justify='right', **keyValues):
    """Summary line: Create a table that stores jeys and values.

    Description:  The function takes in two optional values that determin the 
        table justification. The excess keyvalues represent the information inside the 
        table. The function creates a matrix that stores the needed margins to 
        satisify the justification. The table is the printed out using this matrix.
    """
    
    # Find the lengths of each of the values input
    length2 = [len(i) for i,j in keyValues.items()]
    length3 = [len(j) for i,j in keyValues.items()]

    
    # the matrix stores the margin for each key and value based on the justification
    if key_justify =='right':
        keyMatrix = [[max(length2)-len(i), 0] for i,j in keyValues.items()]
        valMatrix = [[0, max(length3)-len(j)] for i,j in keyValues.items()]

    elif key_justify =='center':
        keyMatrix = [[((max(length2)-len(i))+1)/2, (max(length2)-len(i))/2] for i,j in keyValues.items()]
        valMatrix = [[((max(length3)-len(j))+ 1)/2,(max(length3)-len(j))/2] for i,j in keyValues.items()]

    else:
        keyMatrix = [[0, max(length2)-len(i)] for i,j in keyValues.items()]
        valMatrix = [[max(length3)-len(j), 0] for i,j in keyValues.items()]
	
    
    # Print the table
    print '=' * (2 + max(length2) + 3 + max(length3) + 2)

    count2 = 0
    for i, j in keyValues.items():

        print "| {}{}{} | {}{}{} |".format(' '*keyMatrix[count2][0], i, ' '*keyMatrix[count2][1], 
					   ' '*valMatrix[count2][0], j, ' '*valMatrix[count2][1])
        count2 += 1

    print '=' * (2 + max(length2) + 3 + max(length3) + 2)





	
if __name__ == '__main__':
    """Summary line: Display the make_Table function operatio

    Description:  The program displays three different justification 
        settings of the make_Table function.
    """

    make_Table(
        key_justify='left', 
        value_justify='right',

        first_name="Sam",
        last_name="Redmond",
        shirt_color="pink",
        song="Style",
        artist_fullname="Taylor $wift",
        album="1989"
        )

    make_Table(
        key_justify='right', 
        value_justify='left',

        first_name="Sam",
        last_name="Redmond",
        shirt_color="pink",
        song="Style",
        artist_fullname="Taylor $wift",
        album="1989"
        )
       
    make_Table(
        key_justify='center', 
        value_justify='center',

        first_name="Sam",
        last_name="Redmond",
        shirt_color="pink",
        song="Style",
        artist_fullname="Taylor $wift",
        album="1989"
        )



        
        
        
