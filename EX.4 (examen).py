"""
Crear una funció anomenada cercar_numero_llista(llista, numero) que, 
donada una llista de números i un número,
ens retorni la posició del número dins la llista i-1 en cas que no existeixi dins la llista.
"""
def cercar_numero_llista(llista, numero): 
    # Aquesta funció cerca un número dins una llista i retorna la seva posició. 
    # # Si no es troba, retorna -1. 
    if numero in llista: 
        return llista.index(numero) 
    else: 
        return -1