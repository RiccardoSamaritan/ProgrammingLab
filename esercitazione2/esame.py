class ExamException(Exception):
    pass

class Diff():
    
    def __init__(self, ratio=1):
        self.ratio = ratio
        if type(ratio) != int and type(ratio) != float:
            raise ExamException('Errore, il ratio deve avere un valore numerico')
        if self.ratio < 1:
            raise ExamException('Errore, il ratio deve essere >= 1')

    def compute(self,my_list):

        if type(my_list) != list:
            raise ExamException('Errore di tipo in my_list')
        if len(my_list) < 2:
            raise ExamException('Errore, la lista deve avere almeno 2 elementi')

        results = []
        for i in range(len(my_list) - 1):
            try:
                results.append((my_list[i+1]-my_list[i])/self.ratio)
            except:
                raise ExamException('Errore di tipo per un elemento della lista.')
        return results

diff = Diff()
result = diff.compute([2,4,8,16])
print(result) # Deve stampare a schermo [2.0,4.0,8.0]

        
        