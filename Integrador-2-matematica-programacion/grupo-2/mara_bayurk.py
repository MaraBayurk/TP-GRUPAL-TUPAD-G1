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

def calcularUnion(conjuntos):
    return set.union(*conjuntos)

def calcularInterseccion(conjuntos):
    return set.intersection(*conjuntos)


# def calcularUnion(dnis):
#    conjuntos = generarConjuntosUnicos(dnis)
#    unionConjuntos = set()  # Inicializamos un conjunto vacío para la unión
#    for conjunto in conjuntos:
#        unionConjuntos = unionConjuntos.union(conjunto)
#    return unionConjuntos


# def calcularInterseccion(dnis):
#    conjuntos = generarConjuntosUnicos(dnis)
#    interseccionConjuntos = conjuntos[0]  # Inicializamos con el primer conjunto
#    for conjunto in conjuntos[1:]:
#        interseccionConjuntos = interseccionConjuntos.intersection(conjunto)   
#    return interseccionConjuntos

def conteoFrecuencia(dnis):
    frecuencia = {} # es un diccionario que almacena la frecuencia de cada dígito clave: digito y el valor: frecuencia
    for dni in dnis:
        for digito in dni:
            if digito in frecuencia: # valida si existe el dígito en el diccionario
                frecuencia[digito] += 1
            else:
                frecuencia[digito] = 1
    return frecuencia

    
def ejecutarOperaciones():
    print('___Operaciones con DNIs___')
    dnis = ingresarDni()
    conjuntos = generarConjuntosUnicos(dnis)
    

    print('1. Conjuntos unicos', generarConjuntosUnicos(dnis))
    print('2. Unión de conjuntos', calcularUnion(conjuntos))
    print('3. Intersección de conjuntos', calcularInterseccion(conjuntos))
    print('4. Conteo de frecuencia de dígitos', conteoFrecuencia(conjuntos))
    
ejecutarOperaciones()

