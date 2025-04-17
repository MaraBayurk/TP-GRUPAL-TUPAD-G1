# PROPUESTA CON ESTRUCTURAS REPETITIVAS
        
opcion = 0  #incializo en 0 la variable opcion

while opcion != 7: #ciclo while que se ejecuta mientras opcion sea distinto de 7
    print("--Inicio de Simulación de Puertas Lógicas--")    
    print("1- AND")
    print("2- OR")
    print("3- NOT")
    print("4- NAND")
    print("5- NOR")
    print("6- XOR")
    print("7- Salir")
    
    opcion = int(input("Elige una opción: ")) #opcion toma el valor que ingrese el usuario
    if opcion > 7 or opcion < 0:
        print("Opción inválida.")
        break
    
    if opcion == 7:
        print("Saliste del programa")
        
    else:
        a = int(input("Primer valor (0 o 1): "))
        b = int(input("Segundo valor (0 o 1): "))
        
        puerta_and = a and b
        puerta_or = a or b
        puerta_nand = int(not(a and b))
        puerta_nor = int(not(a or b))
        puerta_xor = a ^ b
        puerta_not_a = int(not a)
        puerta_not_b = int(not b)
        
        if opcion == 1: # AND
            print("Resultado AND:", puerta_and)
        elif opcion == 2: # OR
            print("Resultado OR:", puerta_or)
        elif opcion == 3:  # NOT
            print("Resultado NOT primer valor:", puerta_not_a)
            print("Resultado NOT segundo valor:", puerta_not_b)
        elif opcion == 4: # NAND
            print("Resultado NAND:", puerta_nand)
        elif opcion == 5: # NOR
            print("Resultado NOR:", puerta_nor)
        elif opcion == 6: # XOR
            print("Resultado XOR:", puerta_xor)    

      
            
# PROPUESTA CON ESTRUCTURAS SECUENCIALES

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

if valor1 == 1 and valor2 == 1:
    nand_resultado = 0
    
else:
    nand_resultado = 1

print("NAND:", nand_resultado)


if valor1 == 1 or valor2 == 1:
    nor_resultado = 0
else:
    nor_resultado = 1

print("NOR:", nor_resultado)

if valor1 == 1 and valor2 == 1:
    xor_resultado = 0
else:
    xor_resultado = 1

print("XOR:", xor_resultado)
print("NOT (del primer valor):", int(not valor1))
print("NOT (del segundo valor):", int(not valor2))




# PROPUESTA CON ESTRUCTURAS REPETITIVAS Y SIN REFACORTORIZACION


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
        print("La compuerta XOR esta abierta, se permite el paso")
    else:
        print("La compuerta XOR esta cerrada, no se permite el paso")
else:
    print("Compuerta no válida. Ingrese a, o, n, na, no o x.")


# REFACTORIZACION CON IA


puertaDeingreso = input("Ingrese el caracter de la compuerta a analizar: AND(a), OR(o), NOT(n), NAND(na), NOR(no) o XOR(x): ").strip().lower()
entrada1 = int(input("Ingrese el primer valor (1 para abierto o 0 para cerrado): "))
entrada2 = int(input("Ingrese el segundo valor (1 para abierto o 0 para cerrado): "))

# Validar que las entradas sean 0 o 1
if entrada1 not in [0, 1] or entrada2 not in [0, 1]:
    print("Error: Las entradas deben ser 0 o 1.")
else:
    if puertaDeingreso == "a":
        print("La compuerta AND está", "abierta, se permite el paso" if entrada1 and entrada2 else "cerrada, no se permite el paso")
    elif puertaDeingreso == "o":
        print("La compuerta OR está", "abierta, se permite el paso" if entrada1 or entrada2 else "cerrada, no se permite el paso")
    elif puertaDeingreso == "n":
        print(f"Se niegan las entradas: {int(not entrada1)} y {int(not entrada2)}")
    elif puertaDeingreso == "na":
        print("La compuerta NAND está", "abierta, se permite el paso" if not (entrada1 and entrada2) else "cerrada, no se permite el paso")
    elif puertaDeingreso == "no":
        print("La compuerta NOR está", "abierta, se permite el paso" if not (entrada1 or entrada2) else "cerrada, no se permite el paso")
    elif puertaDeingreso == "x":
        print("La compuerta XOR está", "abierta, se permite el paso" if entrada1 != entrada2 else "cerrada, no se permite el paso")
    else:
        print("Error: Compuerta no válida. Ingrese a, o, n, na, no o x.")

