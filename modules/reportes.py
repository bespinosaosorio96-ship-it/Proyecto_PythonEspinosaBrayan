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
    aprobados_inicial = [c for c in campers if c['notas_inicial']['aprobado']]
    
    print("\n--- Campers que Aprobaron el Examen Inicial ---")
    if not aprobados_inicial:
        print("No hay campers que hayan aprobado el examen inicial.")
        pause_screen()
        return

    for camper in aprobados_inicial:
        print(f"ID: {camper['id']}, Nombre: {camper['nombres']} {camper['apellidos']}, Nota Teórica: {camper['notas_inicial']['teorica']}, Nota Práctica: {camper['notas_inicial']['practica']}, Promedio: {round((camper['notas_inicial']['teorica'] + camper['notas_inicial']['practica']) / 2, 2)}")
    pause_screen()

def listar_trainers():
    clear_screen()
    trainers = read_json('trainers')
    
    print("\n--- Entrenadores de CampusLands ---")
    if not trainers:
        print("No hay trainers registrados.")
        pause_screen()
        return

    for trainer in trainers:
        print(f"ID: {trainer['id']}, Nombre: {trainer['nombres']} {trainer['apellidos']}, Especialidad: {', '.join(trainer['especialidad'])}, Horario: {trainer['horario']}")
    pause_screen()

def listar_campers_bajo_rendimiento():
    clear_screen()
    campers = read_json('campers')
    bajo_rendimiento = [c for c in campers if c['riesgo'] == 'Alto']
    
    print("\n--- Campers con Bajo Rendimiento (Riesgo Alto) ---")
    if not bajo_rendimiento:
        print("No hay campers actualmente en bajo rendimiento (riesgo alto).")
        pause_screen()
        return

    for camper in bajo_rendimiento:
        print(f"ID: {camper['id']}, Nombre: {camper['nombres']} {camper['apellidos']}, Estado: {camper['estado']}, Riesgo: {camper['riesgo']}")
        # Opcional: mostrar detalles de los módulos con bajo rendimiento
        for modulo_nota in camper['modulos_notas']:
            if not modulo_nota['aprobado']:
                print(f"  - Módulo: {modulo_nota['modulo']}, Nota Final: {modulo_nota['nota_final']}")
    pause_screen()

def listar_campers_y_trainers_por_ruta():
    clear_screen()
    rutas = read_json('rutas')
    matriculas = read_json('matriculas')
    campers = read_json('campers')
    trainers = read_json('trainers')

    print("\n--- Campers y Trainers por Ruta de Entrenamiento ---")
    if not rutas:
        print("No hay rutas de entrenamiento para mostrar.")
        pause_screen()
        return

    for ruta in rutas:
        print(f"\n--- Ruta: {ruta['nombre']} ---")
        
        # Trainers de esta ruta
        trainers_ruta = [t for t in trainers if ruta['nombre'] in t['rutas_asignadas']]
        if trainers_ruta:
            print("  Trainers:")
            for trainer in trainers_ruta:
                print(f"    - ID: {trainer['id']}, Nombre: {trainer['nombres']} {trainer['apellidos']}")
        else:
            print("  No hay trainers asignados a esta ruta.")

        # Campers de esta ruta
        matriculas_ruta = [m for m in matriculas if m['ruta_asignada'] == ruta['nombre']]
        campers_ruta_ids = {m['id_camper'] for m in matriculas_ruta} # Usar set para evitar duplicados
        
        if campers_ruta_ids:
            print("  Campers:")
            for camper_id in campers_ruta_ids:
                camper_info = next((c for c in campers if c['id'] == camper_id), None)
                if camper_info:
                    print(f"    - ID: {camper_info['id']}, Nombre: {camper_info['nombres']} {camper_info['apellidos']}, Estado: {camper_info['estado']}")
        else:
            print("  No hay campers matriculados en esta ruta.")
    pause_screen()

def mostrar_rendimiento_modulos():
    clear_screen()
    rutas = read_json('rutas')
    campers = read_json('campers')
    matriculas = read_json('matriculas')

    print("\n--- Rendimiento de Campers por Módulo ---")
    if not rutas:
        print("No hay rutas de entrenamiento para analizar.")
        pause_screen()
        return
    
    for ruta in rutas:
        print(f"\n--- Ruta: {ruta['nombre']} ---")
        
        # Mapear campers a sus rutas y trainers para el reporte
        campers_en_ruta = {} # {camper_id: {'camper_obj': {}, 'trainer_id': 'X'}}
        for m in matriculas:
            if m['ruta_asignada'] == ruta['nombre']:
                camper_obj = next((c for c in campers if c['id'] == m['id_camper']), None)
                if camper_obj:
                    campers_en_ruta[m['id_camper']] = {'camper_obj': camper_obj, 'trainer_id': m['id_trainer']}

        if not campers_en_ruta:
            print("  No hay campers matriculados en esta ruta.")
            continue

        for modulo in ruta['modulos']:
            modulo_nombre = modulo['nombre']
            aprobados_modulo = 0
            perdidos_modulo = 0
            
            for camper_id, data in campers_en_ruta.items():
                camper_obj = data['camper_obj']
                for nota_modulo in camper_obj['modulos_notas']:
                    if nota_modulo['modulo'] == modulo_nombre:
                        if nota_modulo['aprobado']:
                            aprobados_modulo += 1
                        else:
                            perdidos_modulo += 1
                        break # Ya encontramos la nota para este módulo y camper

            print(f"\n  Módulo: {modulo_nombre}")
            print(f"    Aprobados: {aprobados_modulo}")
            print(f"    Perdidos: {perdidos_modulo}")
    
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