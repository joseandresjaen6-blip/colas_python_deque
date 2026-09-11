"""
Ejercicio 3 — Orden de llegada en un hospital
Simula la sala de espera de un hospital (sin prioridades médicas, solo orden de llegada):
• registrar_paciente(cola, nombre)
• atender_paciente(cola) — atiende al siguiente
• pacientes_esperando(cola)
• Busca si un paciente específico aún está en espera (sin desencolar)
"""
from collections import deque


def registrar_paciente(cola, nombre):
    """Registra un paciente al final de la cola."""
    cola.append(nombre)

    print(f"Paciente registrado: {nombre}")


def atender_paciente(cola):
    """Atiende al siguiente paciente."""

    if not cola:
        print("No hay pacientes esperando")
        return None

    paciente = cola.popleft()

    print(f"Atendiendo a: {paciente}")

    return paciente


def pacientes_esperando(cola):
    """Retorna la cantidad de pacientes en espera."""
    return len(cola)


def buscar_paciente(cola, nombre):
    """Busca un paciente sin desencolarlo."""

    if nombre in cola:
        print(f"El paciente {nombre} está en espera")
        return True

    print(f"El paciente {nombre} no está en espera")
    return False


# --- Prueba ---
cola_hospital = deque()

registrar_paciente(cola_hospital, "Ana")
registrar_paciente(cola_hospital, "Carlos")
registrar_paciente(cola_hospital, "María")
registrar_paciente(cola_hospital, "José")

print(
    f"Pacientes esperando: "
    f"{pacientes_esperando(cola_hospital)}"
)

buscar_paciente(cola_hospital, "María")

buscar_paciente(cola_hospital, "Pedro")

atender_paciente(cola_hospital)

print(
    f"Pacientes esperando después de atender: "
    f"{pacientes_esperando(cola_hospital)}"
)

print(f"Cola actual: {list(cola_hospital)}")