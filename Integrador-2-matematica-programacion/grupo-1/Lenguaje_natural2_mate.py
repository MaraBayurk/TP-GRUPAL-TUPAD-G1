# si al menos un conjunto tiene menos o 
# igual de cuatro elementos, entonces es un conjunto con 
# poca diversidad.

# definimos la funciòn 

def poca_diversidad(conjuntos):
    for i, conjunto in enumerate(conjuntos):
        if len(conjunto) <= 4:
            return f"El conjunto {i+1} ({conjunto}) tiene poca diversidad."
    return "Ningún conjunto tiene poca diversidad."

# Definir los conjuntos
A = {1, 2, 3, 4, 5, 7, 9}
B = {1, 2, 3, 5, 7}
C = {0, 1, 4, 6, 8, 9}
D = {0, 1, 3, 4, 7}
E = {0, 2, 3, 4}
F = {1, 2, 3, 4, 6, 7, 8}

conjuntos = [A, B, C, D, E, F]

# Verificar la diversidad
print(poca_diversidad(conjuntos))