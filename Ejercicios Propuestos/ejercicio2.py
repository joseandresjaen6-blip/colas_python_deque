"""
Ejercicio 2 — Buffer de mensajes
Implementa un buffer de mensajes con capacidad máxima de 10:
• enviar_mensaje(buffer, mensaje) — agrega un mensaje
• leer_mensaje(buffer) — lee y elimina el mensaje más antiguo
• Si el buffer está lleno al enviar, descarta el mensaje más antiguo automáticamente
• Implementa una función que muestre los últimos N mensajes sin eliminarlos
"""
# deque(maxlen=10)

from collections import deque
 

def enviar_mensaje(buffer, mensaje):
    """Agrega un mensaje al buffer."""
    buffer.append(mensaje)

    print(f"Mensaje enviado: '{mensaje}'")


def leer_mensaje(buffer):
    """Lee y elimina el mensaje más antiguo."""

    if not buffer:
        print("No hay mensajes en el buffer")
        return None

    mensaje = buffer.popleft()

    print(f"Mensaje leído: '{mensaje}'")

    return mensaje


def ultimos_mensajes(buffer, n):
    """Muestra los últimos N mensajes sin eliminarlos."""

    if not buffer:
        print("El buffer está vacío")
        return

    if n <= 0:
        print("N debe ser mayor que 0")
        return

    mensajes = list(buffer)

    if n > len(mensajes):
        n = len(mensajes)

    print(f"Últimos {n} mensajes:")

    for mensaje in mensajes[-n:]:
        print(f"- {mensaje}")


# --- Prueba ---
buffer = deque(maxlen=10)

for i in range(1, 12):
    enviar_mensaje(buffer, f"Mensaje {i}")

print(f"\nCantidad actual: {len(buffer)}")

print(f"Contenido: {list(buffer)}")

ultimos_mensajes(buffer, 5)

leer_mensaje(buffer)

print(f"Después de leer uno: {list(buffer)}")