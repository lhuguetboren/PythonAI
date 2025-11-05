import pytest
from crm_eventos import validar_email
from tabulate import tabulate

# Lista de casos (email, resultado esperado)
casos = [
    # ✅ Válidos
    ("usuario@example.com", True),
    ("nombre.apellido@dominio.es", True),
    ("user123@sub.dominio.org", True),
    ("a+b@dominio.co", True),

    # ❌ Inválidos
    ("usuarioexample.com", False),
    ("usuario@.com", False),
    ("usuario@dominio", False),
    ("usuario@@dominio.com", False),
    ("usuario@dominio..com", False),
    ("@dominio.com", False),
]

def test_email_valido():
    a = [1,2,3]
    assert validar_email("usuario@example.com") is True
    assert validar_email("nombre.apellido@dominio.es") is True
    assert validar_email("user123@sub.dominio.org") is True


@pytest.mark.parametrize("email, esperado", casos)
def test_validar_email(email, esperado):
    """Verifica la validación de emails mostrando resultados en tabla."""
    resultado = validar_email(email)
    assert resultado == esperado, f"Error en '{email}' (esperado {esperado}, obtenido {resultado})"

def test_mostrar_tabla():
    """Imprime una tabla con todos los casos y resultados."""
    filas = []
    for email, esperado in casos:
        resultado = validar_email(email)
        estado = "✅ OK" if resultado == esperado else "❌ ERROR"
        filas.append([email, esperado, resultado, estado])

    print("\n")
    print(tabulate(
        filas,
        headers=["Email", "Esperado", "Obtenido", "Estado"],
        tablefmt="grid"
    ))
