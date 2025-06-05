import itertools

def obtener_anios_nacimiento():
    
    anios_nacimiento_grupo = []
    contador_integrantes = 0
    ingreso_anios = True

    while ingreso_anios == True:
        entrada = input(f"Ingrese el año de nacimiento del integrante {contador_integrantes+1} o 'FIN' para terminar: ").upper()

        if entrada == 'FIN':
            ingreso_anios = False
        else:
            try:
                anio = int(entrada)
                if anio >= 1900 and anio <= 2025:
                    anios_nacimiento_grupo.append(anio)
                    contador_integrantes += 1
                else:
                    print("Por favor ingresar un año de nacimiento realista (Entre 1900 y 2025)")
            except ValueError:
                print("Entrada invalida. Por favor ingrese un número entero o 'FIN'")

    return anios_nacimiento_grupo, contador_integrantes

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    print("Iniciando prueba")

    anios_nacimiento, cantidad_integrantes = obtener_anios_nacimiento()

    if anios_nacimiento == []:
        print("No se ingresaron años de nacimiento")
    else :
        print(f"Años de nacimiento recopilados: {anios_nacimiento}")
        print(f"Cantidad de integrantes: {cantidad_integrantes}")

    if anios_nacimiento:
        contador_pares = 0
        contador_impares = 0

        for anio in anios_nacimiento:
            if anio % 2 == 0:
                contador_pares += 1
            else:
                contador_impares += 1

        print(f"La cantidad de años pares es: {contador_pares}")
        print(f"La cantidad de años impares: {contador_impares}")
    else:
        print ("No hay elementos en la lista")

    if anios_nacimiento:
        gen_z = True

        for anio in anios_nacimiento:
            if anio < 2000:
                gen_z = False

        if gen_z:
            print("Grupo Z")
        else:
            print("No es un 'Grupo Z'. Al menos un integrante antes del año 2000.")
    else:
        print ("No hay elementos en la lista")

    if anios_nacimiento:
        hay_anios_bisiestos = False

        for anio in anios_nacimiento:
            if es_bisiesto(anio):
                hay_anios_bisiestos = True

        if hay_anios_bisiestos:
            print("Tenemos un año especial")
        else:
            print("No hay años bisiestos")
    else:
        print("No hay elementos en la lista")
    
    if anios_nacimiento:
        anio_actual = 2025
        edades_actuales = []

        for anio in anios_nacimiento:
            edad = anio_actual - anio
            edades_actuales.append(edad)
    
        product_cartesiano = list(itertools.product(anios_nacimiento, edades_actuales))

        print("Producto Cartesiano")

        for par in product_cartesiano:
            print(par)
    else:
        print("No hay elementos en la lista")