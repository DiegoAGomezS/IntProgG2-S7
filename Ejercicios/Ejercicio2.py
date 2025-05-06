def bucle(M):
    prod = 0       #Acumulador del producto
    cont = 0       #Contador de números pares unidos
    num = 2        #Primer numero par
    while cont < M:
        prod *= num
        cont += 1
        num += 2   #Avanza al siguiente numero par
    return f"El producto de {M} números pares es: {prod}"
    
    
def main():
    M = int(input("Ingrese un numero entero y positivo: "))
    if M <= 0:
        print("Error, necesitamos números mayor a 0...")
    else:
        resultado = bucle(M)
        print(resultado)

main()