import numpy as np
from copy import deepcopy

#user inputs
x_coordinate = 3
y_coordinate = 1
updated_value = 5

#sample data
data = np.asarray([
        [1,1,1,2,2,1,1,1],
        [1,1,2,3,2,2,1,2],
        [2,1,2,1,3,2,2,2],
        [2,1,1,1,2,2,3,3],
        [2,3,3,2,2,2,2,2]       
       ])

#global variables        
store = []
scanned_coordinates = []
x_dim = data.shape[0]
y_dim = data.shape[1]

def scanner(initial_x_pos,initial_y_pos,value_to_check_for):   
    
    print('spawning search at ',initial_x_pos,initial_y_pos)
           
    #store correct matches
    if data[initial_x_pos,initial_y_pos] != value_to_check_for:
        print('stopping further search from {0}.{1}'.format(str(initial_x_pos),str(initial_y_pos))) 
        
    elif data[initial_x_pos,initial_y_pos] == value_to_check_for:
        print('found match at ({0},{1})'.format(str(initial_x_pos),str(initial_y_pos)))
        
        #define search coordinates
        search_list = [[initial_x_pos+i,initial_y_pos] for i in [-1,1]]\
                          +[[initial_x_pos,initial_y_pos+i] for i in [-1,1]]
    
        #remove out of bounds cases from search
        for row,(i,j) in enumerate(search_list):
            if (i < 0) | (i >= x_dim) | (j < 0) | (j >= y_dim):
                print('removing out of bounds ({0},{1})'.format(str(i),str(j)))
                search_list.pop(row)
    
        #remove already searched coordinates
        if scanned_coordinates == []:
            #print('start of scan')
            scanned_coordinates.append([initial_x_pos,initial_y_pos])
        else:
            search_list = [row for row in search_list if row not in scanned_coordinates]
            
        #update explored territory
        for row in search_list:
            scanned_coordinates.append(row)   
            
        print('scanned coordinates ',scanned_coordinates)
        print('refined search list',search_list)
        store.append([initial_x_pos,initial_y_pos])
        
        #recursively spawn checkers
        return [scanner(i,j,value_to_check_for) for row,[i,j] in enumerate(search_list)]
            

    

#call the scanner
scanner(x_coordinate,y_coordinate,data[x_coordinate,y_coordinate])

#prepare and print the output
output = deepcopy(data)
for row in store:
    output[row[0],row[1]] = updated_value    
print(output)
