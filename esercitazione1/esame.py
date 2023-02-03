class ExamException(Exception):
    pass

class MovingAverage():

    def __init__(self, wl): # wl means "window lenght"
        
        self.wl = wl
        if type(self.wl) != int:
            raise ExamException('Errore di tipo in window lenght')
        if self.wl < 1:
            raise ExamException('Errore, window lenght < 1')

    def compute(self, my_list):

        if type(my_list) != list:
            raise ExamException('Errore di tipo in my_list')
        if my_list == []:
            raise ExamException('Errore, lista vuota')
        
        if len(my_list) < self.wl:
            raise ExamException('Errore, la finestra è più grande della lista di input')

        results = []
        for i in range(len(my_list) - self.wl + 1):
            try:
                avg = sum(my_list[i : i+self.wl]) / self.wl
                results.append(avg)
            except:
                raise ExamException('Errore, elemento della lista di tipo.')
        return results

#moving_average = MovingAverage(5)
#result = moving_average.compute([2,3,8,16])
#print(result)

    

    

    