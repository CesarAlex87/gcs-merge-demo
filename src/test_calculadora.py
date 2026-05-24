"""Tests para el módulo calculadora. Cada integrante añade tests para su función."""

import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from calculadora import add, subtract, multiply, divide, factorial


class TestOperacionesBasicas:

    def test_add(self):
        assert add(2, 3) == 5
        assert add(-2, 3) == 1
        assert add(0, 0) == 0

    def test_subtract(self):
        assert subtract(10, 5) == 5
        assert subtract(5, 10) == -5

    def test_multiply(self):
        assert multiply(3, 4) == 12
        assert multiply(-3, 4) == -12
        assert multiply(0, 5) == 0

    def test_divide(self):
        assert divide(10, 2) == 5
        assert divide(10, 4) == 2.5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            divide(10, 0)


# ============================================================
# ZONA DE TESTS NUEVOS - Cada integrante añade los suyos aquí
# Integrante 5: TestFactorial
# ============================================================


class TestFactorial:

    def test_factorial_zero(self):
        assert factorial(0) == 1

    def test_factorial_one(self):
        assert factorial(1) == 1

    def test_factorial_positive(self):
        assert factorial(5) == 120
        assert factorial(10) == 3628800

    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_factorial_non_integer(self):
        with pytest.raises(TypeError):
            factorial(3.5)
