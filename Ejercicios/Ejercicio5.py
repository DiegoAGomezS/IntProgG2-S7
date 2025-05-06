def factorialBucle(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= 1
        i += 1
    return fact

def main():
    n = int(input("Ingrese un número entero y positivo: "))
    if n <= 0:
        print("ERR0R!!! Ingrese un númro positivo...")
    else:
        print(f"El factorial de {n} es: {factorialBucle(n)}")
        
main()