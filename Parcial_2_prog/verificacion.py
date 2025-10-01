from LIFOyFIFO import Pila

def verificar_balanceado(expresion):
    pila = Pila()
    pares = {')': '(', '}': '{', ']': '['}
    for elemento in expresion:
        if elemento in pares.values():
            pila.agregar(elemento)
        elif elemento in pares.keys():
            if pila.vacio() or pila.quitar() != pares[elemento]:
                return "Invalido"
    if pila.vacio():
        return "Valido"
    else:
        return "Invalido"

if __name__ == "__main__":
    # Ejemplos de uso
    print(verificar_balanceado("{[()]}"))  # Valido
    print(verificar_balanceado("{[(])}"))  # Invalido
    print(verificar_balanceado("([{}])"))  # Valido
    print(verificar_balanceado("[({)}]"))  # Invalido
