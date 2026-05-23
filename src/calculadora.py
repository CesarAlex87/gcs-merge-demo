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
# Integrante 1: square_root(a)

# Integrante 2: power(a, b)
def power(a, b):
    return a ** b

# Integrante 3: modulo(a, b)
# Integrante 4: percentage(a, b)
# ============================================================


if __name__ == "__main__":
    print("Calculadora - Operaciones básicas")
    print(f"  10 + 5 = {add(10, 5)}")
    print(f"  10 - 5 = {subtract(10, 5)}")
    print(f"  10 * 5 = {multiply(10, 5)}")
    print(f"  10 / 5 = {divide(10, 5)}")
    
    # Prueba de tu función (Integrante 2)
    print(f"  2 ^ 3 = {power(2, 3)}")