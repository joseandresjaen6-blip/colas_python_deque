# ==========================================
# ACTIVIDAD 2.1 - COLA DE NÚMEROS ENTEROS
# ==========================================

class Queue:

    def __init__(self):
        self.items = []

    # Agregar un elemento al final
    def enqueue(self, item):
        self.items.append(item)

    # Eliminar el elemento del frente
    def dequeue(self):
        if self.is_empty():
            raise IndexError("La cola está vacía")
        return self.items.pop(0)

    # Consultar el elemento del frente
    def front(self):
        if self.is_empty():
            raise IndexError("La cola está vacía")
        return self.items[0]

    # Comprobar si la cola está vacía
    def is_empty(self):
        return len(self.items) == 0

    # Obtener el tamaño de la cola
    def size(self):
        return len(self.items)

    # Mostrar los elementos sin acceder directamente a items
    def mostrar(self):
        elementos = []
        cantidad = self.size()

        for _ in range(cantidad):
            elemento = self.dequeue()
            elementos.append(elemento)
            self.enqueue(elemento)

        return elementos


# ==========================================
# 1. CREAR Y LLENAR LA COLA
# ==========================================

cola = Queue()

cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
cola.enqueue(40)
cola.enqueue(50)

print("==========================================")
print("        COLA INICIAL")
print("==========================================")
print(cola.mostrar())


# ==========================================
# 2. COMPROBAR OPERACIONES BÁSICAS
# ==========================================

print("\n==========================================")
print("        OPERACIONES BÁSICAS")
print("==========================================")

print("Tamaño de la cola:", cola.size())
print("Elemento del frente:", cola.front())
print("¿La cola está vacía?:", cola.is_empty())


# ==========================================
# 3. ELIMINAR EL FRENTE
# ==========================================

print("\n==========================================")
print("        ELIMINAR EL FRENTE")
print("==========================================")

eliminado = cola.dequeue()

print("Elemento eliminado:", eliminado)
print("Cola después de eliminar:", cola.mostrar())


# ==========================================
# 4. ELIMINAR EL FONDO
# ==========================================

def eliminar_fondo(cola):

    elementos = []
    cantidad = cola.size()

    for _ in range(cantidad):
        elementos.append(cola.dequeue())

    # Volvemos a meter todos menos el último
    for elemento in elementos[:-1]:
        cola.enqueue(elemento)


print("\n==========================================")
print("        ELIMINAR EL FONDO")
print("==========================================")

print("Antes:", cola.mostrar())

eliminar_fondo(cola)

print("Después:", cola.mostrar())


# ==========================================
# 5. ELIMINAR LA CIMA O FRENTE
# ==========================================

def eliminar_cima(cola):

    if not cola.is_empty():
        cola.dequeue()


print("\n==========================================")
print("        ELIMINAR LA CIMA / FRENTE")
print("==========================================")

print("Antes:", cola.mostrar())

eliminar_cima(cola)

print("Después:", cola.mostrar())


# ==========================================
# 6. VACIAR LA COLA
# ==========================================

def vaciar_cola(cola):

    while not cola.is_empty():
        cola.dequeue()


print("\n==========================================")
print("        VACIAR LA COLA")
print("==========================================")

print("Antes:", cola.mostrar())

vaciar_cola(cola)

print("Después:", cola.mostrar())
print("¿Está vacía?:", cola.is_empty())


# ==========================================
# 7. CREAR OTRA COLA PARA LAS SIGUIENTES
#    OPERACIONES
# ==========================================

cola = Queue()

cola.enqueue(5)
cola.enqueue(8)
cola.enqueue(-2)
cola.enqueue(10)
cola.enqueue(15)

print("\n==========================================")
print("        NUEVA COLA")
print("==========================================")

print("Cola:", cola.mostrar())


# ==========================================
# 8. MOVER EL PRIMER NEGATIVO AL FONDO
# ==========================================

def mover_negativo_al_fondo(cola):

    if cola.is_empty():
        return

    cantidad = cola.size()

    for _ in range(cantidad):

        elemento = cola.dequeue()

        if elemento < 0:
            cola.enqueue(elemento)

            # El resto de elementos ya quedó
            # en el orden correcto
            while _ + 1 < cantidad:
                elemento = cola.dequeue()
                cola.enqueue(elemento)
                _ += 1

            return

        cola.enqueue(elemento)


print("\n==========================================")
print("        MOVER NEGATIVO AL FONDO")
print("==========================================")

print("Antes:", cola.mostrar())

mover_negativo_al_fondo(cola)

print("Después:", cola.mostrar())


# ==========================================
# 9. MOVER EL NÚMERO MAYOR AL FRENTE
# ==========================================

def mover_mayor_a_la_cima(cola):

    if cola.is_empty():
        return

    elementos = []
    cantidad = cola.size()

    # Sacamos los elementos usando dequeue()
    for _ in range(cantidad):
        elementos.append(cola.dequeue())

    mayor = max(elementos)

    # Colocamos primero el mayor
    cola.enqueue(mayor)

    # Colocamos los demás elementos
    for elemento in elementos:
        if elemento != mayor:
            cola.enqueue(elemento)

    # La cola quedó con el mayor al frente


print("\n==========================================")
print("        MOVER MAYOR AL FRENTE")
print("==========================================")

print("Antes:", cola.mostrar())

mover_mayor_a_la_cima(cola)

print("Después:", cola.mostrar())


# ==========================================
# 10. RESULTADO FINAL
# ==========================================

print("\n==========================================")
print("        RESULTADO FINAL")
print("==========================================")

print("Cola final:", cola.mostrar())
print("Cantidad de elementos:", cola.size())
print("Elemento del frente:", cola.front())
print("¿Está vacía?:", cola.is_empty())