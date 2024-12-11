# Inicialización de variables
numero1 = 0
numero2 = 0

# Solicitar los números iniciales
numero1 = float(input("Da el primer número: "))
numero2 = float(input("Da el segundo número: "))

while True:
    # Mostrar el menú
    print("\n(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) Cambiar números")
    print("(6) Salir")
    print("Números actuales:", numero1, numero2)
     
    # Solicitar la información al usuario:
    opcion = input("Selecciona uno de los numeros en pantalla ")

    #Realizar la operacion correspondiente
    if opcion == "1":
        resultado = numero1 + numero2
        print("El resultado es: ", resultado)
    elif opcion == "2":
        resultado = numero1 - numero2
        print("El resultado es: ", resultado)
    elif opcion == "3":
        resultado = numero1 * numero2
        print("El resultado es: ", resultado)
    elif opcion == "4":
        if numero2 != 0:
            resultado = numero1 / numero2
            print("El resultado es:", resultado)
        else:
            print("No puedes dividir por 0 ")
    elif opcion == "5":
        # Cambiar los numeros ingresados
        numero1 = float(input("Ingresa el primer numero "))
        numero2 = float(input("Ingresa el segundo numero "))
    elif opcion == "6":
        print("¡Gracias! ")
        break # Aqui saldriamos del bucle
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú. ")