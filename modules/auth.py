from modules.utils import read_json, clear_screen, pause_screen, write_json
def login():    
    clear_screen()
    print("=== Sistema de Login ===")
    username = input("Usuario: ")
    password = input("Contraseña: ")
    
    usuarios = read_json('usuarios')
    
    usuario_encontrado = next((u for u in usuarios if u['username'] == username and u['password'] == password), None)
    
    if usuario_encontrado:
        print(f"\nBienvenido, {username}! Has iniciado sesión como {usuario_encontrado['rol']}.")
        pause_screen()
        return usuario_encontrado
    else:
        print("\nError: Usuario o contraseña incorrectos.")
        pause_screen()
        return None

def create_user_account(id_asociado, username, password, rol):
    usuarios = read_json('usuarios') # Lee el archivo general de usuarios
    
    if any(u['username'] == username for u in usuarios):
        print(f"Advertencia: El usuario '{username}' ya existe en el archivo de login. No se creará de nuevo.")
        return False
        
    new_user_login_entry = {
        'id_asociado': id_asociado,
        'username': username,
        'password': password,
        'rol': rol
    }
    usuarios.append(new_user_login_entry)
    write_json('usuarios', usuarios)
    return True