"""
En este archivo se encuentran las 4 versiones del proyecto que fueron propuestas
antes de ser refactorizadas. Cada una de ellas refleja una etapa del desarrollo
y la evolución del proyecto, sin las optimizaciones finales.
"""



"""
*******************************
  VERSIÓN 1: PROPUESTA INICIAL - Mara Valentina Bayurk
*******************************
"""

print("Simulación de Puertas Lógicas")
print("1. AND")
print("2. OR")
print("3. NOT")
print("4. NAND")
print("5. NOR")
print("6. XOR")

opcion = int(input("Seleccione la puerta lógica (1-6) o 0 para salir: "))

if opcion == 0:
    print("Saliendo del programa.")
    
elif opcion == 3:
    a = int(input("Ingrese el valor binario (0 o 1): "))
    resultado = not a
    print(f"El resultado es: {int(resultado)}")

elif opcion in range(1, 7) and opcion != 3:
    a = int(input("Ingrese el primer valor binario (0 o 1): "))
    b = int(input("Ingrese el segundo valor binario (0 o 1): "))
    
    if opcion == 1:
        resultado = a and b
    elif opcion == 2:
        resultado = a or b
    elif opcion == 4:
        resultado = not(a and b)
    elif opcion == 5:
        resultado = not(a or b)
    elif opcion == 6:
        resultado = a ^ b

    print(f"El resultado es: {int(resultado)}")


"""
*******************************
  VERSIÓN 2: PROPUESTA INICIAL Cabrera Dario Ezequiel
*******************************


"""
opcion = 0  #incializo en 0 la variable opcion

while opcion != 7: #ciclo while que se ejecuta mientras opcion sea distinto de 7
    print("1- AND") #opcion 1 para puerta/operacion and
    print("2- OR") #opcion 2 para puerta/operacion or
    print("3- NOT") #opcion 3 para puerta/operacion not
    print("4- NAND") #opcion 4 para puerta/operacion nand
    print("5- NOR") #opcion 5 para puerta/operacion nor
    print("6- XOR") #opcion 6 para puerta/operacion xor
    print("7- Salir") #opcion 7 para cortar el ciclo y finalizar el simulador
    opcion = int(input("Elige una opción: ")) #opcion toma el valor que ingrese el usuario
    
    if opcion == 7: #Si opcion vale 7 se corta el ciclo
        print("Nos vemos!") #mensaje de despedida
    else: #que hacer si no es 7 la opcion
        a = int(input("Primer valor (0 o 1): ")) #se pide el primer valor al usuario
        b = int(input("Segundo valor (0 o 1): ")) #se pide el segundo valor al usuario y se pone el condicional del not
        
        puerta_and = 1 if a == 1 and b == 1 else 0 #valor de la puerta and
        puerta_or = 1 if a == 1 or b == 1 else 0 #valor de la puerta or
        puerta_nand = 1 if puerta_and == 0 else 0 #valor de la puerta nand
        puerta_nor = 1 if puerta_or == 0 else 0 #valor de la puerta nor
        puerta_xor = 0 if a == b else 1 #valor de la puerta xor
        puerta_not_a = 1 if a == 0 else 0  # NOT aplicado al primer valor
        puerta_not_b = 1 if b == 0 else 0  # NOT aplicado al segundo valor
        
        if opcion == 1: #si la opcion es 1
            print("Resultado AND:", puerta_and) #imprime la puerta and
        elif opcion == 2: #si la opcion es 2
            print("Resultado OR:", puerta_or) #imprime la puerta or
        elif opcion == 3:  # Si la opción es NOT
            print("Resultado NOT primer valor:", puerta_not_a) #imprime el not del primer valor
            print("Resultado NOT segundo valor:", puerta_not_b) #imprime el not del segundo valor
        elif opcion == 4: #si la opcion es 4
            print("Resultado NAND:", puerta_nand) #imprime la puerta nand
        elif opcion == 5: #si la opcion es 5
            print("Resultado NOR:", puerta_nor) #imprime la puerta nor
        elif opcion == 6: #si la opcion es 6
            print("Resultado XOR:", puerta_xor) #imprime la puerta xor
        else: #si no es ninguna de las opciones
            print("Opción inválida.") #mensaje de opcion invalida """



"""
*******************************
  VERSIÓN 3: PROPUESTA INICIAL Berrone Lanza Lina Lucia
*******************************
"""

puertaDeingreso = input("Ingrese el caracter de la compuerta a analizar : AND(a), OR(o), NOT(n), NAND(na), NOR(no) o XOR(x)")
entrada1 = int(input("Ingrese el primero 1 (abierto) o 0 (cerrado), para probar compuertas"))
entrada2 = int(input("Ingrese el primero 1 (abierto) o 0 (cerrado), para probar compuertas"))



if puertaDeingreso == "a" or puertaDeingreso == "A":
    if entrada1 == 1 and entrada2 == 1:
        print("La compuerta AND esta abierta, se permite el paso")
    else:
        print("La compuerta AND esta cerrada, no se permite el paso")
elif puertaDeingreso == "o" or puertaDeingreso == "O":
    if entrada1 == 1 or entrada2 == 1:
        print("La compuerta OR esta abierta, se permite el paso")
    else:
        print("La compuerta OR esta cerrada, no se permite el paso")
elif puertaDeingreso == "n" or puertaDeingreso == "N":
    print(f"Se niegan las entradas: ", int(not entrada1), "y" , int(not entrada2))
#Desde esta linea empiezan las compuertas adicionales, NAND, NOR y XOR
#NOR (NOT OR): Es la negación de la compuerta OR. Da una salida 1 solo si todas las entradas son 0.    
#XOR (Exclusive OR): Da salida **1 solo si las entradas son diferentes.
#NAND (NOT AND): Es la negación de la compuerta AND. Da una salida 0 solo si todas las entradas son 1.
elif puertaDeingreso == "na" or puertaDeingreso == "NA" or puertaDeingreso == "Na":
    if entrada1 == 1 and entrada2 == 1:
        print("La compuerta NAND esta cerrada, no se permite el paso")
    else:
        print("La compuerta NAND esta abierta, se permite el paso")
elif puertaDeingreso == "no" or puertaDeingreso == "NO" or puertaDeingreso == "No":
    if entrada1 == 0 and entrada2 == 0:
        print("La compuerta NOR esta abierta, se permite el paso")
    else:
        print("La compuerta NOR esta cerrada, no se permite el paso")
elif puertaDeingreso == "X" or puertaDeingreso == "x":
    if entrada1 != entrada2:
        print("La compuerta NOR esta abierta, se permite el paso")
    else:
        print("La compuerta NOR esta cerrada, no se permite el paso")
else:
    print("Compuerta no válida. Ingrese a, o o n.")


"""
*******************************
  VERSIÓN 4: PROPUESTA INICIAL Bonetti Kunt Daniela Sofia
*******************************
"""

valor1 = int(input("Ingresá el primer valor (0 o 1): "))
valor2 = int(input("Ingresá el segundo valor (0 o 1): "))


if valor1 == 1 and valor2 == 1:
    and_resultado = 1
else:
    and_resultado = 0
print("AND:", and_resultado)


if valor1 == 1 or valor2 == 1:
    or_resultado = 1
else:
    or_resultado = 0
print("OR:", or_resultado)



print("NOT (del primer valor):", int(not valor1))
print("NOT (del segundo valor):", int(not valor2))

if valor1 == 1 and valor2 == 1:
    nand_resultado = 00
    
else:
    nand_resultado = 1
print("NAND:", nand_resultado)


if valor1 == 1 or valor2 == 1:
    nor_resultado = 0
else:
    nor_resultado = 1
print("NOR:", nor_resultado)



"""
*******************************
  VERSIÓN 5: PROPUESTA INICIAL Bustamante Erica
*******************************
"""



def puerta_and(a, b):
    return a & b

def puerta_or(a, b):
    return a | b

def puerta_not(a):
    return 1 - a

def puerta_nand(a, b):
    return 1 - (a & b)

def puerta_nor(a, b):
    return 1 - (a | b)

def puerta_xor(a, b):
    return a ^ b

def main():
    print("Simulador de Puertas Lógicas")
    print("---------------------------")

    while True:
        print("1. Puerta AND")
        print("2. Puerta OR")
        print("3. Puerta NOT")
        print("4. Puerta NAND")
        print("5. Puerta NOR")
        print("6. Puerta XOR")
        print("7. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            a = int(input("Ingrese el valor binario A (0 o 1): "))
            b = int(input("Ingrese el valor binario B (0 o 1): "))
            resultado = puerta_and(a, b)
            print(f"{a} AND {b} = {resultado}")
        elif opcion == "2":
            a = int(input("Ingrese el valor binario A (0 o 1): "))
            b = int(input("Ingrese el valor binario B (0 o 1): "))
            resultado = puerta_or(a, b)
            print(f"{a} OR {b} = {resultado}")
        elif opcion == "3":
            a = int(input("Ingrese el valor binario A (0 o 1): "))
            resultado = puerta_not(a)
            print(f"NOT {a} = {resultado}")
        elif opcion == "4":
            a = int(input("Ingrese el valor binario A (0 o 1): "))
            b = int(input("Ingrese el valor binario B (0 o 1): "))
            resultado = puerta_nand(a, b)
            print(f"{a} NAND {b} = {resultado}")
        elif opcion == "5":
            a = int(input("Ingrese el valor binario A (0 o 1): "))
            b = int(input("Ingrese el valor binario B (0 o 1): "))
            resultado = puerta_nor(a, b)
            print(f"{a} NOR {b} = {resultado}")
        elif opcion == "6":
            a = int(input("Ingrese el valor binario A (0 o 1): "))
            b = int(input("Ingrese el valor binario B (0 o 1): "))
            resultado = puerta_xor(a, b)
            print(f"{a} XOR {b} = {resultado}")
        elif opcion == "7":
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

if _name_ == "_main_":
    main()
    
"""
*******************************
  VERSIÓN 6: PROPUESTA INICIAL Benitez Carolina Anabel 
*******************************
"""


# Simulador de Puertas Lógicas: AND, OR, NOT 

# Variable bandera que mantiene activo el programa hasta que el usuario decida salir
bandera = True

while bandera:
    print("SIMULADOR DE PUERTAS LÓGICAS ")
    print("Seleccione la operación que desea realizar:")
    print("1. AND")
    print("2. OR")
    print("3. NOT")
    print("4. Salir")

    # Entrada de opción 
    opcion = input("Ingrese una opción del 1 al 4: ")

    # Opción 1: Puerta AND
    if opcion == "1":
        print("PUERTA AND")
        a = input("Ingrese el primer valor (0 o 1): ")
        b = input("Ingrese el segundo valor (0 o 1): ")

        # Verificamos que las entradas sean válidas (solo 0 o 1)
        if a in ["0", "1"] and b in ["0", "1"]:
            resultado = int(a) & int(b) 
            print(f"{a} AND {b} = {resultado}")
        else:
            print("Entrada inválida. Solo se permiten 0 o 1.")

    # Opción 2: Puerta OR
    elif opcion == "2":
        print("PUERTA OR")
        a = input("Ingrese el primer valor (0 o 1): ")
        b = input("Ingrese el segundo valor (0 o 1): ")

        # Validación de entrada
        if a in ["0", "1"] and b in ["0", "1"]:
            resultado = int(a) | int(b)
            print(f"{a} OR {b} = {resultado}")
        else:
            print("Entrada inválida. Solo se permiten 0 o 1.")

    # Opción 3: Puerta NOT
    elif opcion == "3":
        print("PUERTA NOT")
        a = input("Ingrese un valor (0 o 1): ")

        # Validacion
        if a == "0":
            print(f"NOT {a} = 1")
        elif a == "1":
            print(f"NOT {a} = 0")
        else:
            print("Entrada inválida. Solo se permite 0 o 1.")

    # Opción 4: Salir del programa
    elif opcion == "4":
        print("¡Hasta luego!")
        bandera = False  # Se apaga la bandera para salir del ciclo
    else:
        print("Opción inválida.")