def contador(numero):
    frecuencias = [0] * 10
    numero = abs(numero)
    if numero == 0:
        frecuencias[0] += 1
    else:
        while numero > 0:
            digito = numero % 10
            frecuencias[digito] +=1
            numero //= 10
    return frecuencias

def main():
    num = int(input("Ingrese un número entero"))
    frecuencias = contador(num)
    print("Frecuencia de cada dígito: ")
    for i in range(10):
        print(f"{i}: {frecuencias[i]}")

main()