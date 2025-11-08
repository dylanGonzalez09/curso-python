import os
import re
import datetime
import math
import time
# Extraer archivo zip
# import zipfile

# mi_file = zipfile.ZipFile('Proyecto+Dia+9.zip', 'r')
# mi_file.extractall()

ruta = 'C:\\Cursos\\Python\\Mi_Gran_Directorio'
patron = r'\w{4}-\d{5}'
coincidencias = {}

inicio = time.time()
for carpeta, subcarpeta, archivo in os.walk(ruta):
    for arch in archivo:
        file_path = f'{carpeta}\\{arch}'
        file = open(file_path)
        file_content = file.read()

        search_result = re.search(patron, file_content)

        if search_result != None:
            numero_serie = search_result.group()
            coincidencias[arch] = numero_serie
fin = time.time()

date = datetime.datetime.now()
year = date.year
day = date.day
month = date.month


print('-' * 50 + '\n')
print(f'Fecha de busqueda: {day}/{month}/{year}')
print('\nARCHIVO\t\tNRO. SERIE')
print('-' * len('ARCHIVO') + '\t\t' + '-' * len('NRO. SERIE'))
for llave, valor in coincidencias.items():
    print(f'{llave}\t{valor}')
print(f'\nNumeros encontrados: {len(coincidencias)}')
print(f'Duracion de la busqueda: {math.ceil(fin - inicio)} segundos')
print('\n' + '-' * 50)