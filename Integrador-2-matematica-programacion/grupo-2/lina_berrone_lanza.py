def ingresarDni():
    dnis = input("Ingrese los DNI, separados por ',':")
    dnis = dnis.split(',')
    return dnis 

def generarConjuntosUnicos(dnis):
    conjuntos = []
    for dni in dnis:
        conjunto_unico = set(dni) # set lo que hace es crear un conjunto de dígitos únicos y desordenados -> {3,2,4,1}
        conjuntos.append(conjunto_unico)
    return conjuntos

    
def diferencia_listas(lista1, lista2):
    resultado = []
    for elemento in lista1:
        if elemento not in lista2 and elemento not in resultado:
            resultado.append(elemento)
    return resultado

def diferencia_simetrica_listas(lista1, lista2):
    resultado = []
    for elemento in lista1:
        if elemento not in lista2 and elemento not in resultado:
            resultado.append(elemento)
    for elemento in lista2:
        if elemento not in lista1 and elemento not in resultado:
            resultado.append(elemento)
    return resultado

# Calcular la diferencia secuencial entre todos los conjuntos
def diferencia(conjuntos):
    diferencia = conjuntos[0]
    for conj in conjuntos[1:]:
        diferencia = diferencia_listas(diferencia, conj)
    return diferencia

# Calcular la diferencia simétrica entre todos los conjuntos
def diferenciaSimetrica(conjuntos):
    diferencia_simetrica = conjuntos[0]
    for conj in conjuntos[1:]:
        diferencia_simetrica = diferencia_simetrica_listas(diferencia_simetrica, conj)
    return diferencia_simetrica

#Calcular la suma de todos los digitos de cada DNI
def sumaTotal(dnis):
    suma_total = 0
    for dni in dnis:
        suma_dni = sum(int(d) for d in dni if d.isdigit())
        suma_total += suma_dni
    return suma_total
    

def ejecutarOperacionesAdicionales():
    print('___Operaciones Adicionales con DNIs___')
    dnis = ingresarDni()
    conjuntos= generarConjuntosUnicos(dnis)
    
    print('1. Conjuntos unicos:', conjuntos)
    print('2. Diferencia entre todos los conjuntos:', diferencia(conjuntos))
    print('3. Diferencia simetrica entre conjuntos:', diferenciaSimetrica(conjuntos))
    print('4. Suma total', sumaTotal(dnis))
    
ejecutarOperacionesAdicionales()


