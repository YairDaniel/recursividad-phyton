
def suma_iterativa(n):
    suma = 0

    while n > 9:
        suma += n % 10
        n //= 10

    return suma + n

def suma_recursiva(n):
    if n <= 9:
        return n
    else:
        return suma_recursiva(n // 10) + n % 10

numero = int(input("Ingresa un número: "))

suma_iterativa_resultado = suma_iterativa(numero)
suma_recursiva_resultado = suma_recursiva(numero)

print("Suma iterativa:", suma_iterativa_resultado)
print("Suma recursiva:", suma_recursiva_resultado)

input("Presiona Enter para salir...")
