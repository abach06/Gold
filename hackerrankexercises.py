#for loop
#for i in range(0, 5):
 #   print ("i")
 #print ("i")
 
 #while loop
    
#i = 0
#while i < 5:
 #    print ("i")
#i += 1  
 
 w= len(sub_string)
    count = 0
    
    for i in range(len(string)-w+1):
        window = string[i: i+w]
        if window == sub_string:
            count = count + 1
    return count   
