# Autor: Fabián López
# Refactor: Aplicación del principio de responsabilidad única (SRP) en la gestión de clientes.
# Autor: Rafael Santos
# Refactor: Implementación de ClienteVIP
# Autor: Santiago Rodríguez
# Refactor: Implementación de categorías de clientes (Regular, Frecuente, VIP)
 
from enum import Enum
 
 
class Category(Enum):
    """
    Enumeración que define las categorías posibles de clientes.
    Permite evitar errores de texto y facilita la validación de categorías.
    """
    REGULAR = "Regular"
    FRECUENTE = "Frecuente"
    VIP = "VIP"
    NO_ASIGNADA = "No asignada"
 
 
class Client:
    """
    Clase que representa a un cliente dentro del sistema.
    Tiene un identificador único, un nombre, un correo electrónico y una categoría.
    """
 
    def __init__(self, client_id: int, name: str, email: str):
        # Se inicializan los atributos básicos del cliente
        self.client_id = client_id
        self.name = name
        self.email = email
        # Categoría por defecto
        self.category = Category.NO_ASIGNADA
 
    def set_category(self, category: Category):
        """
        Asigna una categoría al cliente, validando que pertenezca al Enum Category.
        """
        if not isinstance(category, Category):
            raise ValueError("La categoría debe ser un valor válido del Enum Category.")
        self.category = category
 
    def __str__(self):
        # Devuelve una representación legible y consistente del cliente
        return f"[{self.client_id}] {self.name} - {self.email} - Categoría: {self.category.value}"
 
 
class VIPClient(Client):
    """
    Clase que representa a un cliente VIP.
    Hereda de Client y añade un descuento exclusivo.
    """
 
    def __init__(self, client_id: int, name: str, email: str, discount: float = 0.20):
        # Se reutiliza el constructor de Client
        super().__init__(client_id, name, email)
        # Descuento fijo para clientes VIP
        self.discount = discount
        # La categoría del cliente VIP se asigna automáticamente
        self.category = Category.VIP
 
    def __str__(self):
        # Se sobreescribe la representación para distinguir a los clientes VIP
        return (
            f"[{self.client_id}] {self.name} - {self.email} "
            f"(Cliente VIP - Descuento: {self.discount * 100:.0f}%) "
            f"- Categoría: {self.category.value}"
        )
 
 
class ClientManager:
    """
    Clase encargada de realizar las operaciones CRUD sobre los clientes.
    CRUD = Create, Read, Update, Delete.
    Además, maneja la asignación y filtrado por categorías.
    """
 
    def __init__(self):
        # Lista donde se almacenan los objetos de tipo Client o VIPClient
        self.clients = []
 
    # ---------- Operaciones CRUD ----------
 
    def add_client(self, client: Client):
        """
        C - Agrega un nuevo cliente si no existe otro con el mismo ID.
        """
        if self.get_client_by_id(client.client_id):
            print(f"Ya existe un cliente con el ID {client.client_id}.")
            return
        self.clients.append(client)
        print(f"Cliente '{client.name}' agregado correctamente.")
 
    def list_clients(self):
        """
        R - Lista todos los clientes registrados.
        """
        if not self.clients:
            print("No hay clientes registrados.")
            return
 
        print("\nLista de clientes:")
        for client in self.clients:
            print(f"  - {client}")
 
    def update_client_email(self, client_id: int, new_email: str):
        """
        U - Actualiza el correo electrónico de un cliente existente.
        """
        client = self.get_client_by_id(client_id)
        if client:
            old_email = client.email
            client.email = new_email
            print(f"Correo de '{client.name}' actualizado de {old_email} a {new_email}")
        else:
            print(f"No se encontró un cliente con ID {client_id}.")
 
    def delete_client(self, client_id: int):
        """
        D - Elimina un cliente por su ID.
        """
        client = self.get_client_by_id(client_id)
        if client:
            self.clients.remove(client)
            print(f"Cliente '{client.name}' eliminado correctamente.")
        else:
            print(f"No se encontró un cliente con ID {client_id}.")
 
    # ---------- Métodos auxiliares ----------
 
    def get_client_by_id(self, client_id: int):
        """
        Busca un cliente por su ID en la lista de clientes.
        Devuelve el objeto Client si se encuentra, o None si no existe.
        """
        return next((client for client in self.clients if client.client_id == client_id), None)
 
    # ---------- Gestión de categorías ----------
 
    def assign_category(self, client_id: int, category: Category):
        """
        Asigna una categoría a un cliente existente, validando su existencia.
        """
        client = self.get_client_by_id(client_id)
        if client:
            client.set_category(category)
            print(f"Categoría '{category.value}' asignada a {client.name}.")
        else:
            print(f"No se encontró un cliente con ID {client_id}.")
 
    def list_by_category(self, category: Category):
        """
        Lista los clientes pertenecientes a una categoría específica.
        """
        # Se evita el uso de variables abreviadas para mayor claridad
        clients_in_category = [client for client in self.clients if client.category == category]
 
        if not clients_in_category:
            print(f"No hay clientes en la categoría '{category.value}'.")
        else:
            print(f"\nClientes en la categoría '{category.value}':")
            for client in clients_in_category:
                print("  -", client)