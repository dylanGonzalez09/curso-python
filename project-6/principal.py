import numeros

def preguntar():
    print("Bienvenido al sistema de turnos")
    
    while True:
        print("[P] - perfumeria\n[F] - farmacia\n[C] - cosmetica")
        try:
            rubro = input("Ingrese el rubro al que desea acceder (P/F/C) o 'salir' para terminar: ").upper()
            ["P", "F", "C"].index(rubro)  # Validar entrada            
        except ValueError:
            print("Opcion no valida")
        else:
            break
    numeros.decorador(rubro)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("¿Desea sacar otro turno? (S/N): ").upper()
            ["S", "N"].index(otro_turno)  # Validar entrada
        except ValueError:
            print("Opcion no valida")
        else:
            if otro_turno == "N":
                print("Gracias por utilizar el sistema de turnos. ¡Hasta luego!")
                break

inicio()