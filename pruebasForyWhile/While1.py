"""Leer una palabra a fila y convertitrla a mayuscula"""

palabra = input("Ingresa una palabra: ")

while palabra.lower() != "fin":
    print(f"{palabra.upper()} tiene {len(palabra)} letras")
    palabra = input("Ingresa una palabra: ")
else:
    print("Adios...")