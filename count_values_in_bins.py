import numpy as np

def count_values_in_bins(data, bin_edges):
#    B= number of Bins
    B = len(bin_edges) -1
    counts = np.zero(B, dtype=int)  #creo un arrai lungo B, pieno di 0, dove mettereo i conteggi
    
    for x in data: #prendi u valore alla volta nell'array data, ogni valore dell'array viene attribuita ad x
        if x < bin_edges[0] or x > bin_edges[-1]:  # Values outside [bin_edges[0], bin_edges[-1]]
            continue              #salta questo valore a vai al giro successivo
        placed = False    # non ho ancora trvato il bin di x
        for i in range (B-1): #controlliamo tutti i range tranne l'ultimo (perché include il bordo destra)
            if (x>bin_edges[i]) and (x< bin_edges[i+1]):  # se x è dentro dal lato sisnistro (incluso) e prima del lato destro(escluso)
                counts[i] += 1      #se x sta in questo bin, aumento l conteggio di quel bin
                placed= True          #adesso x è in un bin
                break    #esco dal ciclo bin perché x può stare in un solo bin
    if not placed:    
        if (x >= bin_edges[i]) and (x< bin_edges[B]):
            counts[B-1] += 1    #aumenta il conteggio dell'ultimo bin
            

#%%
#2) count_values_in_bins(data, bin_edges)
#   We want to count how many values fall into each numeric bin.
#  - data is a 1-D NumPy array of numbers.
#   - bin_edges is a 1-D NumPy array of length B+1, strictly increasing.
#   These edges define B bins:
#      Bin 0: [bin_edges[0], bin_edges[1])
#      Bin 1: [bin_edges[1], bin_edges[2])
#      ...
#      Bin B-2: [bin_edges[B-2], bin_edges[B-1])
#      Bin B-1: [bin_edges[B-1], bin_edges[B]]   (last bin is inclusive on the right)
#   Values outside [bin_edges[0], bin_edges[-1]] are ignored.
#..............   Return a 1-D NumPy array of length B with the counts per bin.