palabra = input("Dime una palabra: ")

for i in range(1000000):
    if palabra.lower() == "fin":
        break
    else:
        print(f"{palabra.upper()} tiene {len(palabra)} letras")
        palabra = input("Dime una palabra: ")
        
for palabra in iter(input, "fin"):
    print(f"{palabra.capitalize()} tiene {len(palabra)} letras")
else:
    print("Termino...")