#Ejemplo Practico de Big O

# O(n) - Busqueda Lineal
def busqueda_lineal(lista, numero):
    for i in range(len(lista)): # Vamos a recorrer toda la lista en la peor de las casos
        if lista[i]== numero:
            return i
    return -1

# O(log n) - Busqueda Binaria
def busqueda_binaria(lista, numero):
    izq, der = 0, len(lista)-1
    while izq <= der: # dividimos la lista por la mitad para reducir el numero de comparaciones
        medio = (izq + der) // 2
        if lista[medio] == numero:
            return medio
        elif lista[medio] < numero:
            izq = medio + 1
        else:
            der = medio - 1
    return -1
