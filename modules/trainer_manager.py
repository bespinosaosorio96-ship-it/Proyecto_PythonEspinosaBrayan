from modules.utils import read_json, clear_screen, pause_screen 
def listar_campers_asociados(id_trainer):
    clear_screen()
    matriculas = read_json('matriculas')
    campers = read_json('campers')
    
    matriculas_trainer = [m for m in matriculas if m['id_trainer'] == id_trainer]

    if not matriculas_trainer:
        print("No tiene campers asociados en este momento.")
        pause_screen()
        return

    print("\n--- Campers Asociados a su(s) Ruta(s) ---")
    # Usamos un set para evitar mostrar campers duplicados si están en múltiples matrículas (aunque improbable aquí)
    campers_mostrados = set() 
    for matricula_info in matriculas_trainer:
        camper_id = matricula_info['id_camper']
        if camper_id not in campers_mostrados:
            ruta_nombre = matricula_info['ruta_asignada']
            salon = matricula_info['salon_entrenamiento']
            
            for camper in campers:
                if camper['id'] == camper_id:
                    print(f"ID: {camper['id']}, Nombre: {camper['nombres']} {camper['apellidos']}, Estado: {camper['estado']}, Ruta: {ruta_nombre}, Salón: {salon}")
                    campers_mostrados.add(camper_id)
                    break
    pause_screen()

def ver_rutas_y_horarios(id_trainer):
    clear_screen()
    trainers = read_json('trainers')
    rutas_disponibles = read_json('rutas') # Para obtener detalles de las rutas

    trainer_actual = next((t for t in trainers if t['id'] == id_trainer), None)

    if not trainer_actual:
        print("Error: Trainer no encontrado.")
        pause_screen()
        return
    
    print(f"\n--- Rutas y Horarios de {trainer_actual['nombres']} {trainer_actual['apellidos']} ---")
    print(f"Horario General: {trainer_actual['horario']}")
    
    if not trainer_actual['rutas_asignadas']:
        print("No tiene rutas de entrenamiento asignadas actualmente.")
        pause_screen()
        return

    print("\nRutas Asignadas:")
    for ruta_nombre in trainer_actual['rutas_asignadas']:
        print(f"- {ruta_nombre}")
        # Opcional: mostrar detalles de la ruta si se desea
        ruta_detalles = next((r for r in rutas_disponibles if r['nombre'] == ruta_nombre), None)
        if ruta_detalles:
           print(f"  Módulos: {', '.join([m['nombre'] for m in ruta_detalles['modulos']])}")
        
    pause_screen()


def menu_trainer(id_trainer):
    while True:
        clear_screen()
        print("\n--- Menú Trainer ---")
        print("1. Listar Campers Asociados")
        print("2. Ver Rutas y Horarios Asignados") 
        print("3. Cerrar Sesión") 
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            listar_campers_asociados(id_trainer)
        elif opcion == '2':
            ver_rutas_y_horarios(id_trainer)
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            pause_screen()