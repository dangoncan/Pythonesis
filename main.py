import platform

# Obtener el nombre del dispositivo
device_name = platform.node()

#Diccionario
options = {
    'info': 'Información del dispositivo: ' + device_name,
    'reiniciar': 'Reiniciando dispositivo...',
    'salir': 'Hasta luego!'
}

# Saludar al usuario
print("Bienvenido a la consola del dispositivo " + device_name)

# Bucle de espera de ordenes
while True:
    # Leer orden del usuario
    command = input("Ingresa una orden: ")

    # Procesar orden
    if command in options:
        print(options[command])
        if command == 'reiniciar':
            # Codigo para reiniciar el dispositivo
            pass
        elif command == 'salir':
            break
        else:
            print("Comando no reconocido.")