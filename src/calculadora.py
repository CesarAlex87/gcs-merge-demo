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
# ============================================================


def modulo(a, b):
    """Calcula el residuo de la división entre dos números."""
    if b == 0:
        raise ValueError("No se puede calcular módulo con divisor cero")
    return a % b


if __name__ == "__main__":
    print("Calculadora - Operaciones básicas")
    print(f"  10 + 5 = {add(10, 5)}")
    print(f"  10 - 5 = {subtract(10, 5)}")
    print(f"  10 * 5 = {multiply(10, 5)}")
    print(f"  10 / 5 = {divide(10, 5)}")
