"""
Crear una funció anomenada llegir_llista_paraules() 
que demani a l'usuari paraules i acabi quan rebi un ".", finalmente, que retorni la llista llegida.
"""
def llegir_llista_paraules(): 
    # Aquesta funció demana paraules a l'usuari fins que introdueixi un punt. 
    llista_paraules = [] 
    print("Introdueix paraules una a una. Per acabar, introdueix '.'") 

    while True: 
        paraula = input("Introdueix una paraula: ") 
        if paraula == ".":
            break # Finalitza si l'usuari introdueix un punt 
        llista_paraules.append(paraula) # Afegeix la paraula a la llista 
        
    return llista_paraules # Retorna la llista de paraules