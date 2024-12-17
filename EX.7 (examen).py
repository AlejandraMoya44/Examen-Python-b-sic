"""
Crear una funció anomenada crear_llista_num_aletoris() 
que retorni una llista de 5 números aleatoris.
"""
import random 

def crear_llista_num_aletoris(): 
    # Genera una llista de 5 números aleatoris entre 1 i 100 
    llista_aleatoria = [] 
    for i in range(5): 
        llista_aleatoria.append(random.randint(1, 100))
    return llista_aleatoria