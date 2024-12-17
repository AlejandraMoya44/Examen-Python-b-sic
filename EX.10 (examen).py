"""
Crear una funció anomenada menu() que, mostri les 9 + 1 opcions anteriors i ens retorni l'opció elegida per l'usuari. 
També hem de fer el programa principal que permeti, 
segons l'opció elegida, cridar una funció o l'altre amb els paràmetres pertinents.
"""
import random

def menu():
    # Mostra les opcions i retorna l'opció elegida per l'usuari
    print("\nSelecciona una opció:")
    print("1. Llegir llista enters")
    print("2. Filtrar números senars")
    print("3. Sumar números parells")
    print("4. Cercar número en la llista")
    print("5. Llegir llista paraules")
    print("6. Crear paraula amb inicials")
    print("7. Crear llista de números aleatoris")
    print("8. Comparar dues llistes")
    print("9. Verificar majors d'edat")
    print("10. Sortir")

    while True:
        try:
            opcio = int(input("Introdueix el número de l'opció: "))
            if 1 <= opcio <= 10:
                return opcio
            else:
                print("Introdueix un número entre 1 i 10.")
        except ValueError:
            print("Si us plau, introdueix un número vàlid.")

def llegir_llista_enters():
    return [int(x) for x in input("Introdueix una llista de números enters separats per espais: ").split()]

def senars_llista(llista):
    return [nombre for nombre in llista if nombre % 2 != 0]

def sumar_parells_llista(llista):
    return sum(nombre for nombre in llista if nombre % 2 == 0)

def cercar_numero_llista(llista, numero):
    return llista.index(numero) if numero in llista else -1

def llegir_llista_paraules():
    paraules = []
    print("Introdueix paraules una a una. Per acabar, introdueix '.'")
    while True:
        paraula = input("Introdueix una paraula: ")
        if paraula == ".":
            break
        paraules.append(paraula)
    return paraules

def crear_paraula_llista(llista):
    return "".join([paraula[0] for paraula in llista if paraula])

def crear_llista_num_aletoris():
    return [random.randint(1, 100) for _ in range(5)]

def comparar_llistes(llista1, llista2):
    return [2 if llista2[i] == llista1[i] else 1 if llista2[i] in llista1 else 0 for i in range(len(llista2))]

def majors_edat(edat1, edat2):
    return ("major d'edat" si edat1 >= 18 else "menor d'edat", "major d'edat" si edat2 >= 18 else "menor d'edat")

# Programa principal
if __name__ == "__main__":
    while True:
        opcio = menu()
        if opcio == 1:
            llista_enters = llegir_llista_enters()
            print("Llista enters:", llista_enters)
        elif opcio == 2:
            llista = llegir_llista_enters()
            llista_senars = senars_llista(llista)
            print("Números senars:", llista_senars)
        elif opcio == 3:
            llista = llegir_llista_enters()
            suma_parells = sumar_parells_llista(llista)
            print("Suma dels números parells:", suma_parells)
        elif opcio == 4:
            llista = llegir_llista_enters()
            numero = int(input("Introdueix un número a cercar: "))
            posicio = cercar_numero_llista(llista, numero)
            print(f"La posició del número {numero} és:", posicio)
        elif opcio == 5:
            llista_paraules = llegir_llista_paraules()
            print("Llista de paraules:", llista_paraules)
        elif opcio == 6:
            llista_paraules = llegir_llista_paraules()
            paraula_resultant = crear_paraula_llista(llista_paraules)
            print("Paraula formada per les inicials:", paraula_resultant)
        elif opcio == 7:
            llista_aleatoria = crear_llista_num_aletoris()
            print("Llista de 5 números aleatoris:", llista_aleatoria)
        elif opcio == 8:
            llista1 = llegir_llista_enters()
            llista2 = llegir_llista_enters()
            resultat = comparar_llistes(llista1, llista2)
            print("Resultat de la comparació:", resultat)
        elif opcio == 9:
            edat1 = int(input("Introdueix la primera edat: "))
            edat2 = int(input("Introdueix la segona edat: "))
            resultat1, resultat2 = majors_edat(edat1, edat2)
            print(f"Edat1 és {resultat1}")
            print(f"Edat2 és {resultat2}")
        elif opcio == 10:
            print("Sortint del programa.")
            break