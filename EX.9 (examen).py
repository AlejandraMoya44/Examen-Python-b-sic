"""
Crear una funció anomenada majors_edat(edat1, edat2) que, donades dues edats, 
ens diu quina/es són majors d'edat i quines no.
"""
def majors_edat(edat1, edat2): 
    # Aquesta funció verifica si les dues edats són majors d'edat 
    if edat1 >= 18: 
        resultat1 = "major d'edat" 
    else: 
        resultat1 = "menor d'edat" 
    if edat2 >= 18: 
        resultat2 = "major d'edat" 
    else: 
        resultat2 = "menor d'edat" 
        
    return resultat1, resultat2