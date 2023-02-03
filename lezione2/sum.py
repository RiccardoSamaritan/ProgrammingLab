def sum_list(number_list):
    res = 0
    for item in number_list:
        res = res + item
    if number_list == []:
       return None
    return res
    