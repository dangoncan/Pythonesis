import platform

# Obtener el nombre del dispositivo
device_name = platform.node()

# Saludar al usuario
print("Bienvenido a la consola del dispositivo " + device_name)

# Bucle de espera de ordenes
while True:
    # Leer orden del usuario
    command = input("Ingresa una orden: ")

    # Procesar orden
    if command == "salir":
        break
    elif command == "info":
        print("Información del dispositivo: " + device_name)
    else:
        print("Comando no reconocido.")

# Mensaje de despedida
print("Hasta luego!")