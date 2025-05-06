n = int(input("Ingrese por favor un número: "))
sum = 0

if n <= 0:
    print("Error. Ingrese un número válido")
else:
    for i in range (1, n +1):
        sum += 1
    print(f"La sumatoria del i a {n} es {sum}")