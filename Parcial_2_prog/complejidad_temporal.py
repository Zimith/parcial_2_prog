def operacion(n):
    suma = 0
    for i in range(n):
        for j in range(i, n):
            suma += i * j
    return suma
