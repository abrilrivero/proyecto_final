admin_user = "abrilrivero"
admin_pass = "030423"
trabajadores = {}
print("🐶 BIENVENIDO AL SISTEMA DEL REFUGIO 🐾")
while True:
    print("\n1. Iniciar sesión")
    print("2. Registrar trabajador")
    print("3. Salir")
    opcion = input("Elige: ").strip().lower()
    if opcion == "1":
        usuario = input("Usuario: ").strip().lower()
        clave = input("Contraseña: ").strip()
        if usuario == admin_user and clave == admin_pass:
            print("Bienvenida jefa")
            break
        elif usuario in trabajadores and trabajadores[usuario] == clave:
            print("Bienvenido trabajador")
            break
        else:
            print("Usuario o contraseña incorrectos")
    elif opcion == "2":
        nuevo_user = input("Nuevo usuario: ").strip().lower()
        nueva_pass = input("Nueva contraseña: ").strip()
        if nuevo_user in trabajadores or nuevo_user == admin_user:
            print("Ese usuario ya existe")
            break
        else:
            trabajadores[nuevo_user] = nueva_pass
            print("Trabajador registrado")
    elif opcion == "3" or opcion == "salir":
        print("Saliendo...")
        
        break
    else:
        print("Opción inválida")
        break
