from modules.utils import read_json, clear_screen, pause_screen

def listar_campers_inscritos():
    clear_screen()
    campers = read_json('campers')
    inscritos = [c for c in campers if c['estado'] == 'Inscrito']
    
    print("\n--- Campers en Estado 'Inscrito' ---")
    if not inscritos:
        print("No hay campers en estado 'Inscrito'.")
        pause_screen()
        return

    for camper in inscritos:
        print(f"ID: {camper['id']}, Nombre: {camper['nombres']} {camper['apellidos']}, Estado: {camper['estado']}")
    pause_screen()

def listar_campers_aprobados_inicial():
    clear_screen()
    campers = read_json('campers')
    aprobados= [c for c in campers if c['notas_inicial'].get('aprobado', False)]

    print("\n--- Campers que Aprobaron el Examen Inicial ---")
    if not aprobados:
        print("No hay campers que hayan aprobado el examen inicial.")
        pause_screen()
        return

    for camper in aprobados:
        print(f"ID: {camper['id']}, Nombre: {camper['nombres']} {camper['apellidos']}, Nota Teórica: {camper['notas_inicial']['teorica']}, Nota Práctica: {camper['notas_inicial']['practica']}, Promedio: {round((camper['notas_inicial']['teorica'] + camper['notas_inicial']['practica']) / 2, 2)}")
    pause_screen()

def listar_trainers():
    clear_screen()
    trainers = read_json('trainers')
    
    print("\n--- Lista de Trainers de CampusLands ---")
    if not trainers:
        print("No hay trainers registrados.")
        pause_screen()
        return

    for trainer in trainers:
        print(f"ID: {trainer['id']}, Nombre: {trainer['nombres']} {trainer['apellidos']}, Especialidad: {trainer['especialidad']}, Rutas Asignadas: {', '.join(trainer['rutas_asignadas'])}")
    pause_screen()

def listar_campers_bajo_rendimiento():
    clear_screen()
    campers = read_json('campers')
    bajo_rendimiento = [c for c in campers if c['riesgo'] == 'Bajo']

    print("\n--- Campers con Bajo Rendimiento ---")
    if not bajo_rendimiento:
        print("No hay campers con bajo rendimiento.")
        pause_screen()
        return

    for camper in bajo_rendimiento:
        print(f"ID: {camper['id']}, Nombre: {camper['nombres']} {camper['apellidos']}, Estado: {camper['estado']}, Riesgo: {camper['riesgo']}")
    pause_screen()


def mostrar_rendimiento_modulos():
    clear_screen()
    campers = read_json('campers')
    
    print("\n--- Rendimiento por Módulos (Aprobados/Perdidos) ---")
    if not campers:
        print("No hay campers registrados.")
        pause_screen()
        return

    modulos_dict = {}
    for camper in campers:
        for nota in camper['modulos_notas']:
            modulo = nota['modulo']
            if modulo not in modulos_dict:
                modulos_dict[modulo] = {'aprobados': 0, 'perdidos': 0}
            if nota['aprobado']:
                modulos_dict[modulo]['aprobados'] += 1
            else:
                modulos_dict[modulo]['perdidos'] += 1

    for modulo, conteo in modulos_dict.items():
        print(f"Módulo: {modulo}, Aprobados: {conteo['aprobados']}, Perdidos: {conteo['perdidos']}")
    pause_screen()

def listar_campers_y_trainers_por_ruta():
    clear_screen()
    campers = read_json('campers')
    trainers = read_json('trainers')
    
    ruta_id = input("Ingrese el ID de la ruta (e.g., R001): ").strip()
    
    campers_en_ruta = [c for c in campers if any(r['ruta_id'] == ruta_id for r in c.get('rutas', []))]
    trainers_en_ruta = [t for t in trainers if ruta_id in t.get('rutas_asignadas', [])]

    print(f"\n--- Campers y Trainers Asociados a la Ruta {ruta_id} ---")
    
    if not campers_en_ruta:
        print("No hay campers asociados a esta ruta.")
    else:
        print("\nCampers:")
        for camper in campers_en_ruta:
            print(f"ID: {camper['id']}, Nombre: {camper['nombres']} {camper['apellidos']}, Estado: {camper['estado']}, Riesgo: {camper['riesgo']}")

    if not trainers_en_ruta:
        print("\nNo hay trainers asociados a esta ruta.")
    else:
        print("\nTrainers:")
        for trainer in trainers_en_ruta:
            print(f"ID: {trainer['id']}, Nombre: {trainer['nombres']} {trainer['apellidos']}, Especialidad: {trainer['especialidad']}")

    pause_screen()




def menu_reportes():
    while True:
        clear_screen()
        print("\n--- Módulo de Reportes ---")
        print("1. Campers en estado 'Inscrito'")
        print("2. Campers que aprobaron el examen inicial")
        print("3. Entrenadores de CampusLands")
        print("4. Campers con bajo rendimiento")
        print("5. Campers y Trainers asociados a una ruta")
        print("6. Rendimiento por módulos (Aprobados/Perdidos)")
        print("7. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            listar_campers_inscritos()
        elif opcion == '2':
            listar_campers_aprobados_inicial()
        elif opcion == '3':
            listar_trainers()
        elif opcion == '4':
            listar_campers_bajo_rendimiento()
        elif opcion == '5':
            listar_campers_y_trainers_por_ruta()
        elif opcion == '6':
            mostrar_rendimiento_modulos()
        elif opcion == '7':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            pause_screen()