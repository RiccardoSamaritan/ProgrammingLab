class Model():

    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):

    def avg_increase(self, data):
        
        # Valore precedente.
        prev_value = None

        try:
            all(isinstance(item, float) for item in data)
        except TypeError:
               print('Errore di TIPO! La lista deve essere di numeri, vale: "{}"'.format(item))
        except ValueError:
                print('Errore di VALORE! La lista deve essere di numeri, vale: "{}"'.format(item))
        
        # Numero elementi.
        if data != []:
            n = len(data)
        else:
            raise Exception('La lista di input è vuota')

        # Se il numero di elementi non è superiore a 1, ritorno 0 come predizione perché non ho informazioni sufficienti.
        if n <= 1:
            raise Exception('Impossibile fare una predizione, la lista deve avere almeno un elemento')
        
        # Media dell'incremento.
        avg_increase = 0

        # Incremento totale.
        increase = 0

        for item in data:
            try:
                value = float(item)
                if value >= 0:
                    if prev_value == None:
                        prev_value = value
                    else:
                        increase += value - prev_value
                        prev_value = value
                else:
                    raise Exception('Item è negativo: "{}"'.format(item))
            except TypeError:
               print('Errore di TIPO! Non posso convertire "item" a float, vale: "{}"'.format(item))
            except ValueError:
                print('Errore di VALORE! Non posso convertire "item" a float, vale: "{}"'.format(item))

        # Divido l'incremento totale per il numero di incrementi effettuati, ovvero n-1.
        avg_increase = increase / (n-1) 
        
        # Ritorno l'incremento medio tra ogni linea del mio dataset.
        return avg_increase

    def predict(self, data):

        avg_increase = self.avg_increase(data)

        if data == []:
            raise Exception('La lista di input è vuota')

        try:
            all(isinstance(item, float) for item in data)
        except TypeError:
               print('Errore di TIPO! La lista deve essere di numeri, vale: "{}"'.format(item))
        except ValueError:
                print('Errore di VALORE! La lista deve essere di numeri, vale: "{}"'.format(item))

        # Isolo in una variabile il primo elemento della lista
        last_value = data[-1]

        # Richiamando avg_increase posso avere la prediction del valore del prossimo elemento
        prediction = last_value + avg_increase

        return prediction



    