def sum_csv(file_name):
    
    res = 0
    
    my_file = open(file_name, 'r')
    
    if my_file == []:
        return None
    
    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            try:
                value = float(elements[1])
                res = res + value
            except:
                value = None
    if res == 0:
        return None
    
    return res

    