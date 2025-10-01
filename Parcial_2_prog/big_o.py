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


"""
Big o nos permite enteder que para una lista de 100 elementos, la busqueda lineal puede llegar a hacer 
100 comparaciones en el peor de los casos, mientras que la busqueda binaria solo tendra 7 comparaciones 
(2^7 = 128 > 100). Esto es especialmente util cuando trabajamos con listas muy grandes, ya que la diferencia en el 
numero de comparaciones se vuelve significativa.
"""