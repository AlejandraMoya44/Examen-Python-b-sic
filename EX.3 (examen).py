"""
Crear una funció anomenada sumar_parells_llista(llista) que, donada un llista de númerso, 
ens retorni la suma de tots els números parells que té.
"""
def sumar_parells_llista(llista): 
    # Aquesta funció suma tots els números parells d'una llista 
    suma = 0 
    for nombre in llista: 
        if nombre % 2 == 0: 
            suma += nombre 
    return suma