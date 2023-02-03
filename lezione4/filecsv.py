class CSVFile():
    
    def __init__(self,name):
        self.name = name

    def get_data(self):
        
        values = []
        my_file = open(self.name, 'r')
        
        if my_file == []:
            return None

        for line in my_file:
            elements = line.strip('\n').split(',')
            if elements[0] != 'Date':
                values.append(elements)
                
        return values
        