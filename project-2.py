from random import * 

attempts = 0
name = input("Introduce tu nombre: ")
random_number = randint(1, 100)
print(f"Bueno, {name}, he pensado en un numero entre 1 y 100 y tienes solo ocho intentos para adivinar")

while attempts < 8:
    selected_number = int(input("Cual crees que sea el numero? "))

    if selected_number < 1 or selected_number > 100:
        print("El numero debe estar entre 1 y 100")
        attempts += 1
    elif selected_number < random_number:
        print("Tu respuesta es incorrecta, has elegido un numero menor al numero secreto")
        attempts += 1
    elif selected_number > random_number:
        print("Tu respuesta es incorrecta, has elegido un numero mayor al numero secreto")
        attempts += 1
    elif selected_number == random_number:
        print(f"Has ganado!! y te ha tomado {attempts} intentos")
        break

if attempts == 8 and selected_number != random_number:
    print(f"Lo siento, has agotado tus intentos, El numero secreto era: {random_number}")
