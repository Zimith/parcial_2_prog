# Parcial 2 - Programación 2

## Alumno: Lucas Rodrigo Ochoa

## ¿Qué hay en este repositorio?

Este repositorio tiene todos los ejercicios del Parcial 2 sobre algoritmos y estructuras de datos.

### Archivos incluidos:

1. **complejidad_temporal.py** - El código que teníamos que analizar
2. **complejidadO(n).py** - Función que cuenta números pares 
3. **LIFOyFIFO.py** - Las clases Pila y Cola
4. **invertir_lista.py** - Función que da vuelta una lista usando pila
5. **verificacion.py** - Función que verifica paréntesis balanceados
6. **big_o.py** - Ejemplos extra de búsqueda (agregué esto de más)



## Ejemplos rápidos

**Contar pares:**

lista = [1, 2, 3, 4, 5, 6]
resultado = elementos_pares(lista)  # Devuelve 3


**Verificar paréntesis:**

verificar_balanceado("{[()]}")  # Devuelve "Valido"
verificar_balanceado("{[(])}")  # Devuelve "Invalido"


**Invertir lista:**

lista = [1, 2, 3]
resultado = invertir_lista(lista)  # Devuelve [3, 2, 1]


## Ejercicios resueltos

-  Definición de Big O y ejercicios
-  Análisis de complejidad O(n²)
-  Función O(n) para contar pares
-  Implementación de Pila y Cola
-  Invertir lista con pila
-  Verificar símbolos balanceados

## Nota
- Agregué el archivo `big_o.py` con ejemplos extra para entender mejor las diferencias entre algoritmos O(n) y O(log n).

- Algunos archivos incluyen la protección `if __name__ == "__main__":` para evitar ejecución que no queremos que aparezcan.