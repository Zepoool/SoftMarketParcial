# Autor: Fabián López
# Refactor: Aplicación del principio de responsabilidad única (SRP) en la gestión de clientes.

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

    def __str__(self):
        # Devuelve una representación legible del cliente
        return f"[{self.client_id}] {self.name} - {self.email}"


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


# ---------- Ejemplo de uso ----------
if __name__ == "__main__":
    # Se crea una instancia del gestor de clientes
    manager = ClientManager()

    # Se crean algunos clientes de ejemplo
    client1 = Client(1, "Ana Torres", "ana.torres@email.com")
    client2 = Client(2, "Luis Pérez", "luis.perez@email.com")

    # Se agregan los clientes al sistema
    manager.add_client(client1)
    manager.add_client(client2)

    # Se listan los clientes actuales
    manager.list_clients()

    # Se actualiza el correo de un cliente existente
    manager.update_client_email(1, "ana.torres99@email.com")

    # Se elimina un cliente del registro
    manager.delete_client(2)

    # Se muestra la lista final de clientes
    manager.list_clients()
