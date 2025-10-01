from LIFOyFIFO import Pila

def invertir_lista(lista):
    pila = Pila()
    
    # Apilar todos los elementos de la lista
    for elemento in lista:
        pila.agregar(elemento)
    
    lista_invertida = []
    
    # Desapilar todos los elementos para obtener la lista invertida
    while not pila.vacio():
        lista_invertida.append(pila.quitar())
    
    return lista_invertida

if __name__ == "__main__":
    # Ejemplo de uso
    lista = [1, 2, 3, 4, 5]
    lista_invertida = invertir_lista(lista)
    print(f"Original: {lista}, Invertida: {lista_invertida}")
