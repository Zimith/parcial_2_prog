# Pila (LIFO)
class Pila:
    def __init__(self):
        self.pila = []

    def agregar(self, elemento):  # Agrega un elemento a la cima
        self.pila.append(elemento)

    def quitar(self):  # Elimina y devuelve el elemento de la cima
        if self.vacio():
            raise IndexError("quitar de una pila vacía")
        return self.pila.pop()

    def vacio(self):  # Verifica si la pila está vacía
        return len(self.pila) == 0

    def size(self):  # Devuelve el número de elementos
        return len(self.pila)


# Cola (FIFO)
class Cola:
    def __init__(self):
        self.cola = []

    def agregar(self, elemento):  # Agrega un elemento al final
        self.cola.append(elemento)

    def quitar(self):  # Elimina y devuelve el primer elemento
        if self.vacio():
            raise IndexError("quitar de una cola vacía")
        return self.cola.pop(0)

    def vacio(self):  # Verifica si la cola está vacía
        return len(self.cola) == 0

    def size(self):  # Devuelve el número de elementos
        return len(self.cola)


if __name__ == "__main__":
    # Ejemplo del uso
    p = Pila()
    p.agregar(10)
    p.agregar(20)
    print(p.quitar())  # 20, último en entrar, primero en salir

    c = Cola()
    c.agregar(10)
    c.agregar(20)
    print(c.quitar())  # 10, primero en entrar, primero en salir
