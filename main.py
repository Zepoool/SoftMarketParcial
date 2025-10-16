# Autor: Fabián López
# Refactor: Aplicación del principio de responsabilidad única (SRP) en la gestión de clientes.
# Autor: Rafael Santos
# Refactor: Implementación de ClienteVIP
 
class Client:
    """
    Clase que representa a un cliente dentro del sistema.
    Tiene un identificador único, un nombre y un correo electrónico.
    """
 
    def __init__(self, client_id: int, name: str, email: str):
        # Se inicializan los atributos básicos del cliente
        self.client_id = client_id
        self.name = name
        self.email = email
 
    def set_category(self, category: str):
        """
        Asigna una categoría al cliente (Regular, Frecuente, VIP.).
        """
        self.category = category.capitalize()
 
    def __str__(self):
        # Devuelve una representación legible del cliente
        category_info = f" - Categoría: {getattr(self, 'category', 'No asignada')}"
        return f"[{self.client_id}] {self.name} - {self.email}{category_info}"
 
 
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
 
    def __str__(self):
        # Se sobreescribe la representación para distinguir a los clientes VIP
        category_info = f" - Categoría: {getattr(self, 'category', 'No asignada')}"
        return f"[{self.client_id}] {self.name} - {self.email} (Cliente VIP - Descuento: {self.discount*100} %){category_info}"
 
 
class ClientManager:
    """
    Clase encargada de realizar las operaciones CRUD sobre los clientes.
    CRUD = Create, Read, Update, Delete.
    """
 
    def __init__(self):
        # Lista donde se almacenan los objetos de tipo Client
        self.clients = []
 
    # ---------- Operaciones CRUD ----------
 
    def add_client(self, client: Client):
        """
        C - Agrega un nuevo cliente si no existe otro con el mismo ID.
        """
        # Se verifica si ya existe un cliente con el mismo ID
        if self.get_client_by_id(client.client_id):
            print(f"Ya existe un cliente con el ID {client.client_id}")
            return
        # Si no existe, se agrega a la lista
        self.clients.append(client)
        print(f"Cliente '{client.name}' agregado correctamente.")
 
    def list_clients(self):
        """
        R - Lista todos los clientes registrados.
        """
        # Si la lista está vacía, se muestra un mensaje informativo
        if not self.clients:
            print("No hay clientes registrados.")
            return
 
        print("\nLista de clientes:")
        # Se recorre la lista de clientes e imprime cada uno
        for client in self.clients:
            print(f"  - {client}")
 
    def update_client_email(self, client_id: int, new_email: str):
        """
        U - Actualiza el correo electrónico de un cliente existente.
        """
        # Se busca el cliente por su ID
        client = self.get_client_by_id(client_id)
        if client:
            old_email = client.email
            # Se actualiza el correo
            client.email = new_email
            print(f"Correo de '{client.name}' actualizado de {old_email} a {new_email}")
        else:
            print(f"No se encontró un cliente con ID {client_id}")
 
    def delete_client(self, client_id: int):
        """
        D - Elimina un cliente por su ID.
        """
        # Se busca el cliente por su ID
        client = self.get_client_by_id(client_id)
        if client:
            # Si existe, se elimina de la lista
            self.clients.remove(client)
            print(f"Cliente '{client.name}' eliminado correctamente.")
        else:
            print(f"No se encontró un cliente con ID {client_id}")
 
    # ---------- Métodos auxiliares ----------
 
    def get_client_by_id(self, client_id: int):
        """
        Busca un cliente por su ID en la lista de clientes.
        Devuelve el objeto Client si se encuentra, o None si no existe.
        """
        for client in self.clients:
            if client.client_id == client_id:
                return client
        return None
 
    # ---------- asignacion de categoria ----------
 
    def assign_category(self, client_id: int, category: str):
        """
        Asigna una categoría a un cliente existente.
        """
        client = self.get_client_by_id(client_id)
        if client:
            client.set_category(category)
            print(f"Categoría '{category}' asignada a {client.name}.")
        else:
            print(f"No se encontró un cliente con ID {client_id}.")
 
    def list_by_category(self, category: str):
        """
        Lista los clientes pertenecientes a una categoría específica.
        """
        found = [c for c in self.clients if getattr(c, "category", "").lower() == category.lower()]
        if not found:
            print(f"No hay clientes en la categoría '{category}'.")
        else:
            print(f"\nClientes en la categoría '{category}':")
            for c in found:
                print("  -", c)
 
 
# ---------- Ejemplo de uso ----------
if __name__ == "__main__":
    # Se crea una instancia del gestor de clientes
    manager = ClientManager()
 
    # Se crean algunos clientes de ejemplo
    client1 = Client(1, "Ana Torres", "ana.torres@email.com")
    client2 = Client(2, "Luis Pérez", "luis.perez@email.com")
 
    # Se crea un cliente VIP de ejemplo (con descuento por defecto del 20%)
    vip_client = VIPClient(3, "María Gómez", "maria.vip@email.com")
 
    # Se agregan los clientes al sistema
    manager.add_client(client1)
    manager.add_client(client2)
    manager.add_client(vip_client)
 
    # Se listan los clientes actuales
    manager.list_clients()
 
    # Se actualiza el correo de un cliente existente
    manager.update_client_email(1, "ana.torres99@email.com")
 
    # Se elimina un cliente del registro
    manager.delete_client(2)
 
    # Se muestra la lista final de clientes
    manager.list_clients()
 
    # --- ASIGNACIÓN DE CATEGORÍAS ---
    print("\n--- ASIGNACIÓN DE CATEGORÍAS ---")
    manager.assign_category(1, "Frecuente")
    manager.assign_category(3, "VIP")
 
    # --- LISTAR CLIENTES POR CATEGORÍA ---
    print("\n--- LISTAR CLIENTES POR CATEGORÍA ---")
    manager.list_by_category("Frecuente")
    manager.list_by_category("VIP")
    manager.list_by_category("Regular")