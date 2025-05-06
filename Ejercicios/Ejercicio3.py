def contador(cadena):
    vocales = ["a", "e","i", "o", "u"]
    total = 0
    for char in vocales:
        total += 1
    return total

def main():
    cadena = input("Ingrese el enunciadi")
    print(f"La cadena contiene {contador(cadena)} vocales")

main()