"""
Crear una funció anomenada crear_paraula_llista(llista) que, donada una llista de paraules, 
ens retorni una paraula amb totes les inicials de les paraules de la llista.
"""
def crear_paraula_llista(llista): 
    # Aquesta funció crea una paraula amb les inicials de cada paraula de la llista 
    inicials = "" 
    for paraula in llista: 
        if paraula: 
            inicials += paraula[0] 
    return inicials