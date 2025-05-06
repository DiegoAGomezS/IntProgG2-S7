def find(n):
    mayor = None
    menor = None
    for i in range (n):
        num = float(input(f" Ingrese el número #{i+1}: "))
        if mayor is None or num > mayor:
            mayor = num
        if menor is None or num < menor:
            menor = num
    return mayor, menor

def main():
    n = int(input("¿Cuántos números va a ingresar?: "))
    if n <= 0:
        print("Error. Ingrese un número válido")
    else:
        mayor, menor = find(n)
        print(f"El número mayor es: {mayor}")
        print(f"El número menor es: {menor}")

main()