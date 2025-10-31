from random import *

# JUEGO AHORCADO

palabras = ["python", "java", "kotlin", "javascript", "hangman", "programacion"]
vidas = 6
palabra_al_azar = choice(palabras)
guiones = ["_" for palabra in palabra_al_azar]



print(f"La palabra adivinar tiene {guiones} letras")

def chequear_letra(letra):
    letra_index = palabra_al_azar.index(letra)
    global guiones
    guiones = [letra if letra == palabra_al_azar[letra_index] or guion != '_' else '_' for letra, guion in zip(palabra_al_azar, guiones)]
    print(f"Correcto adivinaste la letra, ahora la palabra es: {guiones}")

def validar_letra(letra):
    if(letra not in palabra_al_azar):
        global vidas
        if(vidas == 1):
            print(f"Has perdido todas tus vidas. La palabra era: {palabra_al_azar}")
            return
        vidas -= 1
        print(f"Has perdido una vida. Te quedan {vidas} vidas.")
        pedir_letra()
    else:
        chequear_letra(letra)
        if "_" not in guiones:
            print("Felicidades, has adivinado la palabra!")
        else:
            pedir_letra()

def pedir_letra():
    letra = input("Adivina una letra: ")
    validar_letra(letra)



pedir_letra()



