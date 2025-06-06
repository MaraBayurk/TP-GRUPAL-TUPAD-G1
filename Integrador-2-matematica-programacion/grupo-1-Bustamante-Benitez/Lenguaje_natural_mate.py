# Si todos los conjuntos tienen al 
# menos 2 elementos en comunes, entonces tienen 
# una similitud media.

# Definir la funcion 
def similitud_media(conjuntos):
    # Calcular la intersección de todos los conjuntos
    interseccion = set(conjuntos[0])
    for conjunto in conjuntos[1:]:
        interseccion = interseccion & conjunto

    # Verificar si la intersección tiene al menos 2 elementos
    if len(interseccion) >= 2:
        return True
    else:
        return False

# Definir los conjuntos
A = {1, 2, 3, 4, 5, 7, 9}
B = {1, 2, 3, 5, 7}
C = {0, 1, 4, 6, 8, 9}
D = {0, 1, 3, 4, 7}
E = {0, 2, 3, 4}
F = {1, 2, 3, 4, 6, 7, 8}

conjuntos = [A, B, C, D, E, F]

# Verificar la similitud media
if similitud_media(conjuntos):
    print("Todos los conjuntos tienen una similitud media.")
else:
    print("No todos los conjuntos tienen una similitud media.")

# Calcular la intersección de todos los conjuntos
interseccion = set(conjuntos[0])
for conjunto in conjuntos[1:]:
    interseccion = interseccion & conjunto
print("Elementos comunes:", interseccion)