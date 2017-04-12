#!/usr/bin/env python -tt
""" File: flights.py """

# Imports
import re           # Regular Expressions





def string_isalpha(string):
    """Summary line:  Check if all members of a string are aphanumeric
    
    Description:    The function loop over the string checking if each character is 
        alphanumeric. If one character does not pass the function returns false. 
        If the for loops is finished without a return of false a True value is returned.
    """
    
    for chr in string:
        if not chr.isalpha():
            return False
    
    return True
    
  
  
  
  
def check_code(airport_Start, airport_End, file):
    """Summary line:   Look through the database for airport code to ensure it is valid.

    Description:  Loop through the file conytaining the airport codes. If the code
        we are looking for are found a flag is set, if bout flags are set true is returned.
    """
  
    file_lines = file.readlines()   # Open up the file
    file.seek(0)                    # Make sure the seek is at line one

    start_flag = 0                  # Flags == 1 if airport code is in our database         
    end_flag   = 0                  # Flags == 0 if airport code is not in our database   
    
    
    for line in file_lines:         
        split_line = line.split(',')       # line information is comma seperated   
	
        if split_line[2] == airport_Start: # airport code 1 is in index 2
            start_flag = 1                 # if we find the code in databass set flag 
            
        if split_line[4] == airport_End:   # airport code 2 is in index 4
            end_flag   = 1                 # if we find the code in databass set flag 
            
        if start_flag == 1 and end_flag == 1: # if we find both codes return true
            return True
 
    file.seek(0)                           # Put the seek back to line 1
    
    return False

    
    
    
    
def find_start_routes(airport_Start, file):
    """Summary line:   Get a list of routes that have the desired starting location 

    Description:  The function searches the database for routes that start in the location we desire,
        It thern puts the route start and end location togethor in a set so we dont end up with 
        duplicates. Finally the we return a lisyt of all possible valid routes.
        
        route definition is stored with airpoort codes. for example if we use SFO as our start we could return 
        valid_routes_list = [(SFO, JFK),(SFO, DCC), ...]
    """
   
    file_lines        = file.readlines()
    valid_routes      = set()           # Route with start location matching ours is contained here, set will ignore duplicates
    valid_routes_list = []              # Valid routes in list form to return   
  
  
    # If the start loctaion in database matches our start location, add to set
    for line in file_lines:
        zac = line.split(',')           # line data is comma seperated
	
        if zac[2] == airport_Start:  
            valid_routes.add((zac[2], zac[4]))
        
        
    # Move roiutes from set to the list
    while len(valid_routes):
        valid_routes_list.append( valid_routes.pop() )
  
 
    file.seek(0)                     # return seek to line one
    
    
    return valid_routes_list
    
    
    
    
    
def find_routes(airport_Start, airport_End, file):
    """Summary line:  Search database for a flight route with the desired orgin and destination

    Description: Look through each line of the route database checking if the start and end loications 
        match the desired loctaions and then return the route information.
    """
   
    file_lines = file.readlines()   # 
    file.seek(0)                    # start at the top o fthe file

    
    for line in file_lines:         # search each ine of the file
        route = line.split(',')       # line information is split by commas
	
        # Break if we find a route that matches the start and end location we want
        if route[2] == airport_Start and route[4] == airport_End:
            break	
            
 
    file.seek(0)                    # return to the top of the file
    
    return route                      # return the route that we found
    
   
   
   
   
def find_airport(airport_Acroynm, file):
    """Summary line:   Find information about the desired airport.

    Description:    Take in a file of airport information, and the desired airport code. 
        The function will then yues regular expressions to parce the file data and return 
        important data about the airport. For example the airport_country, airport_city, 
        airport_Acroynm, airport_name, airport_code are returned values
    """
    
    # put the airport string in the correct form for searching
    airport_Acroynm1  =  ',"' + airport_Acroynm + '",'
        
    file_lines  = file.readlines()        # Get the file lines
    file.seek(0)                          # start at line 1
    line_count  = 0                       # Count the line that we are at
    
    # Search eash line of the file. 
    # look for the airport code in each line, if it is not o th current line airport_info is empty and we dont break
    # if the code is on the lin airport_info is not empty and we break the loop with the current line_count intact
    for line in file_lines:
        airport_info  = re.findall(airport_Acroynm1, line) 
        line_count   += 1

        if airport_info:   
            break	
            
    # the line containing the information we desire
    airport_info =  file_lines[line_count - 1]    
    
    # INformation on each line ie seperated by a comma
    airport_info = airport_info.split(',')                    
    
    # Get all the sirport information form the line in the file
    airport_country =  re.findall('[\w| ]+', airport_info[3])  
    airport_country =  ''.join([x for x in airport_country])

    airport_city    =  re.findall('[\w| ]+', airport_info[2])
    airport_city    =  ''.join([x for x in airport_city])

    airport_Acroynm =  re.findall('[\w| ]+', airport_info[4])
    airport_Acroynm =  ''.join([x for x in airport_Acroynm])
    
    airport_name    =  re.findall('[\w| ]+', airport_info[1])
    airport_name    =  ''.join([x for x in airport_name])

    airport_code    =  re.findall('[\w| ]+', airport_info[0])
    airport_code    =  ''.join([x for x in airport_code])

    
    # Reset the file seek index
    file.seek(0)
    
    
    # return the values in a packed tuple
    return airport_country, airport_city, airport_Acroynm, airport_name, airport_code

    
    
    
    
    
    
    
    
    
if __name__ == '__main__':  
    """Summary line: This script will displays the different flight routes avaliable between two cities.

    Description:  The program takes user input of the locations in sirport code form, and 
        immediatly checks if the codes are valid. It then looks in a airport file for the desired airpoirts 
        and displays specifoic oinformation. It then builds a dictioinary that will be used to find direct 
        an dindirect connections.
        
        Web dictionary: example         start_dest = sfo end_dest = kck
        1: [[(sfo, jfk)], [(jfk, bbb), (jfk, aba),(jfk, kck)...], []] , 2: ......
        a web of possible paths ais built. The first list putes routes that start at the start_destination,
        The second list containns rpoutess that start at the first lists destination. This dictionary is built then searched
        This example has no direct routes but one indiredct route. sfo jfk the jfk kck
    """
    
    ########## Get user to input the start and end locations, in airport code form.
    print "Enter start and end airport codes, and the program will returnm the possible routes"
    print "Example > SFO JFK"
    
    travel_locations  = raw_input('>' )                                    # Get the user input
    travel_locations  = [_ for _ in travel_locations.split(' ') if len(_)] # Filter out non-text(spaces)
                      
    # Raise error if the codes are not three characters long
    if (len(travel_locations[0]) != 3) or (len(travel_locations[1]) != 3):
        raise Exception("One or more of the airport codes is invalid becaiuse it is not three characters long", travel_locations)
    
    # Raise error if the codes are not characters
    if not string_isalpha(travel_locations[0]) or not string_isalpha(travel_locations[1]):
        raise Exception("One or more of the airport codes is invalid becaiuse it contains non alphabetical characters", travel_locations)
                                                
    # Seperate locations    
    start_dest = travel_locations[0].upper()
    end_dest   = travel_locations[1].upper()
    
    # Search file, and make sure the airport code is in our database
    with open('routes.txt', 'r') as f: 
        if not check_code(start_dest, end_dest, f):
            raise Exception("One or more of the codes is not recognised by our database, try another nearby airport")
        
  
    ########## Get information about the start and end destination
    with open('airports.txt', 'r') as f:	
        airport_start = find_airport(start_dest, f)
        airport_end   = find_airport(end_dest, f)
       
    # Print location datails of the two travel detinations
    print '\n We are starting at {} in {} {}, \n and flying to {} in {} {} \n'.format(airport_start[3], airport_start[1], 
           airport_start[0], airport_end[3], airport_end[1], airport_end[0],  )
   

    ########## get the starting airport routes, level 1
    with open('routes.txt', 'r') as f:        
        level1_routes = find_start_routes(airport_start[2], f)
        
    # Build part one of the dictionary web path
    flight_web_dict = dict()                  # Contains all the different paths(direct and layovers), from start and end location
    
   
    for x in range(0, len(level1_routes) ):   # For each of  the inital level 1 route we find
        flight_web_dict[x] = [[],[],[]]       # List 1= direct, list two = one layover,......
        
        flight_web_dict[x][0].append( (level1_routes[x][0], level1_routes[x][1]) ) # Add the level 1 routes to the offical route dictionary
    
   
    ########## Get all of the connecting routes from the first routes destinatrion, level 2 
    # Put the level 1 route destinations in a set to remove duplicaes
    # They become the lebvel 2 orgins. They are potential layover locations on our way to our destination.
    level2_orgins = set()
    
    for x in range(0, len(flight_web_dict)):
        level2_orgins.add( flight_web_dict[x][0][0][1] )
            
    
    with open('routes.txt', 'r') as f:  
        inter_dict = dict()                          # temporary dictionary holds the intermediate connections
        
        for airport in level2_orgins:                # Find all the routes that start with the level 2 airpport
            inter_dict[airport] = find_start_routes(airport , f)
            
    
    # fill the second level of the dictionary with all the possible connections
    for x in range(0, len(flight_web_dict)):
        flight_web_dict[x][1] = inter_dict[ flight_web_dict[x][0][0][1] ]
    
   
    ########## Search the route web for all the valid routes direct and indirct that pass have our desired start and end location
    # Dirct route check
    print '-- Direct routes --'
    
    # search level one of the route dictionary for matches and pront them
    for x in range(0, len(flight_web_dict)):
        if flight_web_dict[x][0][0][1] == end_dest:
            print flight_web_dict[x][0][0][0], ' to ', flight_web_dict[x][0][0][1] 
    
    
    # Indirect route check
    print '\n', '-- Indirect routes --'
            
    # search level two of the route dictionary for matches and pront them
    # also print information on the layover location
    for x in range(0, len(flight_web_dict)):                # the entire dict
        for y in range(0, len(flight_web_dict[x][1])):      # the second col.( one layover)
            if flight_web_dict[x][1][y][1]  == end_dest:    # the end destination and layover destination match
                print flight_web_dict[x][0][0][0], 'to', flight_web_dict[x][0][0][1]    # print the first route, orgin to layover
                print flight_web_dict[x][1][y][0], 'to', flight_web_dict[x][1][y][1]    # print second route layover to destination
                
                with open('airports.txt', 'r') as f:	    # look throught the airport inforation
                    airport_int = find_airport(flight_web_dict[x][0][0][1], f)          # get information based on the layover airporyt
        
                print 'Layover is at {} airport in {} {} \n'.format(airport_int[3],     # get information based on the layover airporyt
                    airport_int[1], airport_int[0]  )
            
  
  
  
    # ----- notes ------
    # airline    airline id                                plane type
    # AC,       330,          SFO, 3469,   YYC,178,Y,0,     CR
    # WS,       5416,SFO,3469,YYC,178,,0,73W
    
  
    # words = re.findall(r'\w+', f.read().lower())
    # words = re.findall('\w+[a]...[e]...[i]', f.read().lower())
    # a     = collections.Counter(words).most_common(100)
    
    # flight_web_dict[0]                                          the first path
    # flight_web_dict[0][0] / flight_web_dict[0][0][0]            the first path/ the fist pair
    # flight_web_dict[0][0][0][0] / flight_web_dict[0][0][0][1]   start and possibly the end loc...
    
    # flight_web_dict[0][1]     the second path 
    # flight_web_dict[0][1][x]  each of the pairs in the path
    # flight_web_dict[0][1][x][0] previous destination
    # flight_web_dict[0][1][x][1] new poissible destination

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
