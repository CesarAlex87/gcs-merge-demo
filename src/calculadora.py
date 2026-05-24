"""
Calculadora - Proyecto GCS Merge Demo
Cada integrante añade una nueva función matemática.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


# ============================================================
# ZONA DE FUNCIONES NUEVAS - Cada integrante añade la suya aquí
# Integrante 5: factorial(n)
# ============================================================


def factorial(n):
    """Calcula el factorial de un número entero no negativo."""
    if not isinstance(n, int):
        raise TypeError("El argumento debe ser un número entero")
    if n < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print("Calculadora - Operaciones básicas")
    print(f"  10 + 5 = {add(10, 5)}")
    print(f"  10 - 5 = {subtract(10, 5)}")
    print(f"  10 * 5 = {multiply(10, 5)}")
    print(f"  10 / 5 = {divide(10, 5)}")

    # Prueba de función (Integrante 5)
    print(f"  5! = {factorial(5)}")
