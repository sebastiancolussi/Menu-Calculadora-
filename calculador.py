

# Calculadora reutilizable, con los condicionales if no podemos reutilizar el codigo


def sumar(a, b):
    return a+b


def restar(a, b):
    return a-b


def multiplicar(a, b):
    return a*b


def dividir(a, b):
    return a/b


def menu_calculadora():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    opcion = input("--> ")
    return opcion


num1 = float(input("Elegi un numero: "))

while True:
    op = menu_calculadora()
    num2 = float(input("Elegi otro numero: "))
    if op == "1":
        resultado = sumar(num1, num2)
    elif op == "2":
        resultado = restar(num1, num2)
    elif op == "3":
        resultado = multiplicar(num1, num2)
    elif op == "4":
        resultado = dividir(num1, num2)
    else:
        print("Enter a valid operator")

    print("Resultado: ", resultado)

    num1 = resultado
    seguir = input("Seguir operando? (y/n): ")
    if seguir == "n":
        break
