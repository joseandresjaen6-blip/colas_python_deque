"""
Ejercicio 1 — Cola de impresión
Implementa un sistema de cola de impresión con las siguientes funciones:
• agregar_documento(cola, nombre, paginas) — encola un documento
• imprimir_siguiente(cola) — desencola e imprime el siguiente documento
• documentos_en_espera(cola) — retorna la cantidad de documentos pendientes
• mostrar_cola(cola) — muestra todos los documentos en orden

"""
from collections import deque


def agregar_documento(cola, nombre, paginas):
    """Encola un documento con su nombre y cantidad de páginas."""
    documento = (nombre, paginas)
    cola.append(documento)

    print(f"Documento agregado: '{nombre}' - {paginas} páginas")


def imprimir_siguiente(cola):
    """Desencola e imprime el siguiente documento."""

    if not cola:
        print("No hay documentos en espera")
        return None

    documento = cola.popleft()
    nombre, paginas = documento

    print(f"Imprimiendo: '{nombre}' - {paginas} páginas")

    return documento


def documentos_en_espera(cola):
    """Retorna la cantidad de documentos pendientes."""
    return len(cola)


def mostrar_cola(cola):
    """Muestra todos los documentos en orden."""

    if not cola:
        print("Cola de impresión vacía")
        return

    print("Documentos en espera:")

    for nombre, paginas in cola:
        print(f"- {nombre} ({paginas} páginas)")


# --- Prueba ---
cola_impresion = deque()

agregar_documento(
    cola_impresion,
    "Trabajo de Python",
    10
)

agregar_documento(
    cola_impresion,
    "Informe de Base de Datos",
    15
)

agregar_documento(
    cola_impresion,
    "Tarea de Ingeniería",
    5
)

mostrar_cola(cola_impresion)

print(
    f"Documentos en espera: "
    f"{documentos_en_espera(cola_impresion)}"
)

imprimir_siguiente(cola_impresion)

print(
    f"Documentos en espera: "
    f"{documentos_en_espera(cola_impresion)}"
)

mostrar_cola(cola_impresion)