
#!/usr/bin/env python -tt
""" File: kv_store.py """


class TimedKVStore:
    """Summary line:  The class is a key value structure that stores the time a values is added

    Description:   The structure is initalised as a dictionary with a list as a value. This allows
        key value strusture as well as a sortable list for the values. The put method adds a list to
        in the key position, stotring the input value and the time. The get method will get the 
        most resent added value or if a time is given the value just before the given time.
    """
    
    def __init__(self):
        self.dict  = defaultdict(list)


    def put(self, key, value):
        self.dict[key].append( [value, time.time()] )		


    def get(self, key, time=0):
        xx = 0
        if time:
            for x in self.dict[key]:
                if self.dict[key][xx][1] < time:
                    return self.dict[key][xx][0]
                xx += 1


            return None

        return self.dict[key][len(self.dict['1']) - 1][0]
		
		
		


	
if __name__ == '__main__':
    """Summary line:  Display the TimedKVStore class usage. 

    Description:    Display the TimedKVStore class usage. 
    """
    
    from collections import defaultdict
    import time
  
    
    d  = TimedKVStore()
    
    t0 = time.time()
    d.put("1", 1)
 
    # Add delay because computer executes statemnets nearly sumiltaniously
    time.sleep(0.1) 
 
    t1 = time.time()
    d.put("1", 1.1)
    
    print d.get("1")        # 1.1
    print d.get("1", t1)    # 1
    print d.get("1", t0)    # None

    
    
    
    
    
    
    
    
