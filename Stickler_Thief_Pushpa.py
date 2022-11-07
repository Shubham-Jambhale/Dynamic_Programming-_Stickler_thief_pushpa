def get_max_coconuts (count) :
    if len(count) == 0:
        return 0
    
    #if only one length return the first element
    add1 = count[0]
    if len(count) == 1:
        return add1
    #if only 2 length return max of 1 and 2 
    add2 = max(count[0], count[1])
    if len(count) == 2:
        return add2
 
   #store max values 
    addition_counts= None
 
    #finding the maximum values of coconuts
    for i in range(2, len(count)):
        addition_counts = max(count[i]+add1, add2)
        add1 = add2
        add2 = addition_counts
 
    return addition_counts

if __name__ == '__main__':
    
    print("-----Output--------")
    coutn = [2,7,9,13,1]
    get_count = get_max_coconuts(coutn)
    print("no of coconuts we can get", get_count)
    print()
    print("-----Output--------")
    coutn = [1,1,1,1,1]
    get_count = get_max_coconuts(coutn)
    print("no of coconuts we can get", get_count)