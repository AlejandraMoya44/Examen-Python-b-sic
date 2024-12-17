"""
Crear una funció anomenada senars_llista(llista) que, donada una llista de números, 
ens retorni una llista amb els números senars que hi ha.
"""
def senars_llista(llista): 
    senars = [nombre for nombre in llista if nombre % 2 != 0] 
    return senars