# Prueba de integración del sistema de gestión de clientes
# Autor: Fabián López
# Propósito: Verificar la funcionalidad completa del sistema de gestión de clientes.

from main import Client, VIPClient, ClientManager, Category

def print_divider(title: str):
    """
    Imprime un divisor visual con un título para separar secciones.
    """
    print("\n" + "="*10 + f" {title} " + "="*10 + "\n")


def main():
    """
    Prueba de funcionamiento general del sistema de gestión de clientes.
    Cubre creación, actualización, eliminación y categorización de clientes.
    """

    print_divider("INICIO DE PRUEBA")

    # 1️ Crear gestor de clientes
    manager = ClientManager()

    # 2️ Crear clientes base y VIP
    client1 = Client(1, "Ana Torres", "ana.torres@email.com")
    client2 = Client(2, "Luis Pérez", "luis.perez@email.com")
    vip_client = VIPClient(3, "María Gómez", "maria.vip@email.com")

    # 3️ Agregar clientes
    print_divider("AGREGAR CLIENTES")
    manager.add_client(client1)
    manager.add_client(client2)
    manager.add_client(vip_client)

    # 4️ Listar clientes actuales
    print_divider("LISTA DE CLIENTES")
    manager.list_clients()

    # 5️ Asignar categorías
    print_divider("ASIGNAR CATEGORÍAS")
    manager.assign_category(1, Category.FRECUENTE)
    manager.assign_category(2, Category.REGULAR)

    # 6️ Listar por categoría
    print_divider("LISTAR POR CATEGORÍA - FRECUENTE")
    manager.list_by_category(Category.FRECUENTE)
    print_divider("LISTAR POR CATEGORÍA - VIP")
    manager.list_by_category(Category.VIP)

    # 7️ Actualizar correo de un cliente
    print_divider("ACTUALIZAR CORREO")
    manager.update_client_email(1, "ana.torres99@email.com")

    # 8️ Eliminar un cliente
    print_divider("ELIMINAR CLIENTE")
    manager.delete_client(2)

    # 9️ Listar clientes finales
    print_divider("LISTA FINAL DE CLIENTES")
    manager.list_clients()

    print_divider("PRUEBA FINALIZADA CON ÉXITO")


if __name__ == "__main__":
    main()
