# Complejidad O(n)

def elementos_pares(lista):
    contador = 0 # Inicializamos el contador de números pares
    for num in lista:  # Recorremos cada elemento de la lista una vez
        if num % 2 == 0:  # Verificamos si el número es par
            contador += 1  # Incrementamos el contador si es par
    return contador  # Retornamos el conteo de números pares


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Numero de elementos pares en la lista: {elementos_pares(lista)}")
