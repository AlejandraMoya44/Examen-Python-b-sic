"""
Crear una funció anomenada comparar_llistes(llista1, llista2) que, donades dues llistes de 5 elements cada una, retorni una llista on posarem 0 si 
l'element de llista2 no està dins la llista1, 1 si l'element hi és,
però no està a la mateixa posició i 2 si està a la mateixa posició (Part de comparació del MasterMind).
"""
def comparar_llistes(llista1, llista2): 
    # Compara dues llistes de 5 elements i retorna una llista de resultats 
    resultat = [] 
    for i in range(len(llista2)): 
        if llista2[i] == llista1[i]: 
            resultat.append(2) # Mateixa posició 
        elif llista2[i] in llista1: 
            resultat.append(1) # Diferent posició 
        else: resultat.append(0) # No està a llista1 
    return resultat