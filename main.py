# SoftMarket - Código Caótico (Versión inicial)
# Simula el desorden y la falta de buenas prácticas

clientes = []

def agregar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    cliente = {
        "nombre": nombre,
        "correo": correo,
        "telefono": telefono
    }
    clientes.append(cliente)
    print("Cliente agregado exitosamente!")

def listar_clientes():
    print("=== Lista de Clientes ===")
    for c in clientes:
        print("Nombre:", c["nombre"])
        print("Correo:", c["correo"])
        print("Teléfono:", c["telefono"])
        print("-------------------------")

def buscar_cliente():
    nombre = input("Ingrese el nombre del cliente que desea buscar: ")
    encontrado = False
    for c in clientes:
        if c["nombre"].lower() == nombre.lower():
            print("Cliente encontrado!")
            print("Nombre:", c["nombre"])
            print("Correo:", c["correo"])
            print("Teléfono:", c["telefono"])
            encontrado = True
            break
    if not encontrado:
        print("Cliente no encontrado.")

def menu():
    while True:
        print("\n--- Sistema de Clientes SoftMarket ---")
        print("1. Agregar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

menu()
