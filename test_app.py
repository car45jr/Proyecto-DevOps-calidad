"""
Módulo de pruebas unitarias: test_app.py
Herramienta de pruebas: pytest
Objetivo: Validar el comportamiento de las operaciones de la calculadora
          y asegurar la calidad del código mediante pruebas automatizadas.
"""

import pytest
from app import sumar, restar, multiplicar, dividir


def test_sumar_positivos():
    """Caso 1: Verifica la suma correcta de dos números enteros positivos."""
    resultado = sumar(5, 3)
    assert resultado == 8


def test_restar_positivos():
    """Caso 2: Verifica la resta correcta de dos números enteros positivos."""
    resultado = restar(10, 4)
    assert resultado == 6


def test_multiplicar_positivos():
    """Caso 3: Verifica la multiplicación correcta de dos números enteros positivos."""
    resultado = multiplicar(6, 7)
    assert resultado == 42


def test_dividir_exacta():
    """Caso 4: Verifica la división exacta de dos números enteros."""
    resultado = dividir(15, 3)
    assert resultado == 5.0


def test_dividir_entre_cero():
    """Caso 5: Verifica que dividir entre cero lance ZeroDivisionError con mensaje claro."""
    with pytest.raises(ZeroDivisionError, match="No es posible dividir entre cero"):
        dividir(10, 0)


def test_operaciones_con_negativos():
    """Caso 6: Verifica operaciones matemáticas con números negativos."""
    assert sumar(-5, -3) == -8
    assert restar(-5, -2) == -3
    assert multiplicar(-4, 3) == -12
    assert dividir(-10, 2) == -5.0


def test_operaciones_con_decimales():
    """Caso 7: Verifica operaciones matemáticas con números decimales (float)."""
    assert sumar(1.5, 2.5) == 4.0
    assert restar(5.5, 2.0) == 3.5
    assert multiplicar(2.5, 4.0) == 10.0
    assert dividir(7.5, 2.5) == 3.0
