import numpy as np

def moving_average(signal, window_size):
    n = len(signal)   #lunghezza del segnale (numero di elementi)
    k = (window_size-1)//2    #k è quanti valori prendiamo a sinistra e a destra del centro
    
    out= np.zeros(n, dtype=float) #creiamo un array di outout lungo n, pieno di 0.0 (float)
    
    for i in range(n):   #percorriamo ogni idice x del segnale
        start= max(0, i-k)  #calcoliamo l'inizio della finestra: non può scendere stto zero
        end= min(n-1, i + k)   #calcoliamo la fine della finestra: non può superare n-1
        
        window= signal[start:end +1]   #prendiamo i valori da start a end (end+1 perché slice esclude l'ultimo)')
        
        out[i] = window.sum() / len(window)   #facciamo la media dei valori dellafinestra e l mettiamo in out[i]
        
    return out   #ritorniamo il nuovo array smussato   

    
    
#%%
#3) moving_average(signal, window_size)
#   We want to smooth a 1-D NumPy array using a centered moving average.
#   - signal is a 1-D NumPy array of numbers
#   - window_size is a positive odd integer (1, 3, 5,...).
#   Let k = (window_size - 1) // 2
#   For each index i, consider the indices from max(0, i-k) to min(n-1, i+k),
#   where n is the length of signal, and take the average of those values.
#   Return a new 1-D NumPy array of floats with the same length as signal.