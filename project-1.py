# ANALIZADOR DE TEXTO
text = input("Ingresa un texto: ").lower()
text.split(" ")
letter1 = input("Ingresa una letra: ").lower()
letter2 = input("Ingresa otra letra: ").lower()
letter3 = input("Ingresa una ultima letra: ").lower()

letters_list = [letter1, letter2, letter3]

for letter_index in range(len(letters_list)):
    print(f"La letra: {letters_list[letter_index]} aparece: {text.count(letters_list[letter_index])} veces")

print(f"El texto contiene {len(text.split(" "))} palabras")
print(f"La primera letra del texto es: {text[0]} y la ultima es: {text[-1]}")
print(f"La cadena invertida es: {text[::-1]}")
if "Python".lower() in text:
    print(f"La palabra Python si esta dentro del texto")
else:
    print(f"La palabra Python NO esta dentro del texto")
