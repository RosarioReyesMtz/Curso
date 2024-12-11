from Node import Node
import logging

# Configurar el logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0  # Inicializa el tamaño a 0
        self.limit = limit  # Establece el límite de la pila

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            logger.info("La pila esta totalmente vacia!")  # Mensaje corregido
            return None

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item  # Guardar el nodo a eliminar
            self.top_item = self.top_item.get_next_node()  # Actualizar top_item al siguiente nodo
            self.size -= 1  # Reducir el tamaño en 1
            return item_to_remove.get_value()  # Retornar el valor del nodo eliminado
        else:
            logger.info("La pila esta totalmente vacia!")  # Mensaje corregido
            return None

    def push(self, value):
        if self.has_space():
            item = Node(value)  # Crear un nuevo nodo con el valor proporcionado
            item.set_next_node(self.top_item)  # Establecer el siguiente nodo como el actual top_item
            self.top_item = item  # Actualizar top_item a este nuevo nodo
            self.size += 1  # Incrementar el tamaño en 1
        else:
            logger.info("La pila esta llena ¡No queda espacio!")  # Mensaje corregido

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0