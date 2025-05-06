def suma(num):
    suma_pares = 0
    suma_impares = 0
    while num != 0:
        if num % 2 == 0:
            suma_pares += num
        else:
            sum_impares += num
        num = int(input("Ingrese otro número (0 para terminar): "))
    return suma_pares , suma_impares

def main():
    num = int(input("Ingresa un número (0 para terminar): "))
    suma_pares , suma_impares = suma(num)
    
    print(f"La suma de los numeros pares es: {suma_pares}")
    print(f"La suma de los numeros impares es: {suma_impares}")

main()