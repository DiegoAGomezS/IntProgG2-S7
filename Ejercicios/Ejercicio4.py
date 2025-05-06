def promedio(n):
    calificaciones = []
    for i in range(n):
        cal = float(input(f"Ingrese la calificación {i+1}: "))
        calificaciones.append(cal)
    prom = sum(calificaciones)/n
    return prom, calificaciones

def main():
    n = int(input("Ingrese el número de calicicaciones: "))
    if n <= 0:
        print("Error, ingrese un número valido")
    else:
        prom, cal = promedio(n)
        print("Clificaciones ingresadas", cal)
        print(f"El promedio es: {prom}")

main()