class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name = None):
        
        # Set the file name
        self.name = name

    def get_data(self):

        # Check if the input provides a file to open
        if self.name == None:
            raise ExamExceptin ('Error, no file name in the input')
        # Try to open the file and read a line. If one of those two actions 
        # goes wrong, raise an exception.
        try:
            my_file = open(self.name, 'r')
        except:
            raise ExamException ('Error, cannot open the file')
        if my_file.read() == '':
            raise ExamException ('Error, no data in my_file')

        # Create a list to store data from the input file.
        time_series = []
        for line in my_file:
            # Split the line in two. The first part will be the epoch value, 
            # the second one will be the temperature value.
            elements = line.strip('\n').split(',')
            
            # Check if epoch value is an integer or if it can be converted to. 
            # If it's not, skip the line.
            try:
                elements[0] = int(elements[0])
            except:
                continue
            
            # Check if temperature value is a float or if it can be converted. 
            # If it's not, skip the line.
            try:
                elements[1] = float(elements[1])
            except: 
                continue

            # After the checks, add the line to time series list.
            time_series.append(elements)

        # If no line was added to the time series list (so it's empty), 
        # raise an exception.

        epoch_values = []
        
        # Add all epoch values from time series to a new list, in order to check 
        # if time series list is sorted and has no duplicates. If a check goes 
        # wrong, raise an exception. 
        for i in range(len(time_series)):
            epoch_values.append(time_series[i][0])
        if sorted(epoch_values) != epoch_values:
            raise ExamException('Error, time_series not sorted')
        if len(epoch_values) != len(set(epoch_values)):
            raise ExamException('Error, duplicated epoch in time_series')

        # Close the CSV file and return the time series
        my_file.close()
        return time_series

def compute_daily_max_difference(time_series):
    
    # If no line was added to the time series list (so it's empty), 
    # raise an exception.
    if time_series == []:
        raise ExamException ('Error, time series is empty')
        
    # Create a list to save each day temperatures.
    daily_temperatures = []

    # Create a list to save max difference between temperatures for each day. 
    # It's going to be the output list.
    daily_max_difference = []

    # Set the time on 00:00 AM of the first day of the time series
    current_time = time_series[0][0] - (time_series[0][0] % 86400)
    
    # Loop until current time variable exceeds the biggest epoch of the time series
    while current_time < time_series[-1][0]:

        # Add to daily temperatures list every value of the current day    
        # (current_time + 24 hours)
        daily_temperatures = [time_series[i][1] for i in range(len(time_series)) if current_time <= time_series[i][0] < (current_time+86400)]

        # If current day has less than 2 temperature values, 
        # daily max difference will be None
        if len(daily_temperatures) <= 1:
            daily_max_difference.append(None)
        
        # Otherwise append the difference between maximum and 
        # minimum temperatures of the day
        else:
            daily_max_difference.append(max(daily_temperatures)-min(daily_temperatures))
        
        # Clear daily temperatures list in order to start another iterative cycle
        daily_temperatures = []
        
        # Add 24 hours to move forward one day.
        current_time += 86400
    
    # Return the list of temperature max difference for each day.
    return daily_max_difference

            
            
        
            
        
            
            
        
    
    

    

        

        
            
            

        