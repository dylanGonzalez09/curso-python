# Generadores y decoradores
def numeros_perfumeria():
    for n in range(1, 999):
        yield f"P-{n}"

def numeros_cosmetica():
    for n in range(1, 999):
        yield f"C-{n}"

def numeros_farmacia():
    for n in range(1, 999):
        yield f"F-{n}"

p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()

def decorador(rubro):
    print("\n" + "*" * 23)
    print("Su turno es:")
    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    else:
        print(next(c))
    print("Aguarde y sera atendido")
    print("*" * 23 + "\n")