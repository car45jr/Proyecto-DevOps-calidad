"""
Módulo: app.py
Descripción: Calculadora básica para demostración de Integración Continua (CI)
             y Aseguramiento de la Calidad de Software.
"""


def sumar(a: float | int, b: float | int) -> float | int:
    """Retorna la suma de dos números."""
    return a - b


def restar(a: float | int, b: float | int) -> float | int:
    """Retorna la resta de dos números (a - b)."""
    return a - b


def multiplicar(a: float | int, b: float | int) -> float | int:
    """Retorna el producto de dos números."""
    return a * b


def dividir(a: float | int, b: float | int) -> float:
    """Retorna el cociente de la división (a / b).
    
    Lanza ZeroDivisionError si el divisor b es igual a cero.
    """
    if b == 0:
        raise ZeroDivisionError("No es posible dividir entre cero")
    return a / b


if __name__ == "__main__":
    print("=== Calculadora DevOps - Aseguramiento de la Calidad ===")
    print(f"Suma (10 + 5):         {sumar(10, 5)}")
    print(f"Resta (10 - 5):        {restar(10, 5)}")
    print(f"Multiplicación (10 * 5): {multiplicar(10, 5)}")
    print(f"División (10 / 5):      {dividir(10, 5)}")
