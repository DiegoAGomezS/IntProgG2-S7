def contador(cadena):
    palabras = cadena.split() 
    return len(palabras)

def main():
    enunciado = input("Ingrese un enunciado de su elección: ")
    print(f"La cadena contiene: {contador(enunciado)} palabras")
    
main()