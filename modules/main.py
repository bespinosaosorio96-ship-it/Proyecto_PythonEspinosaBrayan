
from modules.auth import login
from modules.camper_manager import menu_camper
from modules.trainer_manager import menu_trainer
from modules.coordinator_manager import menu_coordinador 
from modules.utils import clear_screen, pause_screen

def main():
    while True:
        usuario = login()
        if usuario:
            rol = usuario['rol']
            if rol == 'camper':
                menu_camper(usuario['id_asociado'])
            elif rol == 'trainer':
                menu_trainer(usuario['id_asociado'])
            elif rol == 'coordinador':
                menu_coordinador()
            else:
                print("Rol de usuario no reconocido.")
                pause_screen()
        else:
            clear_screen()
            print("Intento de login fallido. Por favor, inténtelo de nuevo.")
            pause_screen()