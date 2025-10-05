
from webbrowser import get
from modules.utils import read_json, write_json, clear_screen, pause_screen, generate_matricula_id
from modules.reportes import menu_reportes
from modules.auth import create_user_account 

def menu_coordinador():
    while True:
        clear_screen()
        print("--- Menú Coordinador ---")
        print("1. Registrar Nuevo Camper")
        print("2. Registrar Notas Examen Inicial")
        print("3. Crear Ruta de Entrenamiento")
        print("4. Gestionar Áreas de Entrenamiento")
        print("5. Registrar Nuevo Trainer")
        print("6. Matricular Camper en Ruta")
        print("7. Registrar/Editar Notas de Módulo")
        print("8. Listar Campers Registrados")
        print("9. Asignar Trainer y Salón a Ruta")
        print("10. Reportes")
        print("11. Cerrar Sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_camper()
        elif opcion == '2':
            registrar_notas_inicial()
        elif opcion == '3':
            crear_ruta_entrenamiento()

        elif opcion == '4':
            gestionar_areas_entrenamiento()
        elif opcion == '5':
            registrar_trainer()
        elif opcion == '6':
            matriculas()
        elif opcion == '7':
            registrar_notas_modulo_coordinador()
        elif opcion == '8':
            listar_campers()
        elif opcion == '9':
            asignar_trainer_y_salon_a_ruta()
        elif opcion == '10':
            menu_reportes()
        elif opcion == '11':
            print("Cerrando sesión...")
            pause_screen()
            break
        else:
            print("Opción no válida.")
            pause_screen()  

def registrar_camper():
    clear_screen()
    print("\n--- Registrar Nuevo Camper ---")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    direccion = input("Dirección: ")
    acudiente = input("Nombre del Acudiente: ")
    telefono_celular = input("Teléfono Celular: ")
    telefono_fijo = input("Teléfono Fijo: ")
    estado = input("Estado (Activo/Inactivo): ")
    riesgo = input("Nivel de Riesgo (Bajo/Medio/Alto): ")

    campers = read_json('campers')
    nuevo_id = generate_matricula_id(campers)

    nuevo_camper = {
        "id": nuevo_id,
        "nombres": nombres,
        "apellidos": apellidos,
        "direccion": direccion,
        "acudiente": acudiente,
        "telefonos": {
            "celular": telefono_celular,
            "fijo": telefono_fijo
        },
        "estado": estado,
        "riesgo": riesgo,
        "notas_inicial": {
            "teorica": None,
            "practica": None,
            "aprobado": None
        },
        "modulos_notas": [],
        "rutas_matriculadas": []
    }

    campers.append(nuevo_camper)
    write_json('campers', campers)
    print(f"\nCamper registrado exitosamente con ID: {nuevo_id}")
    pause_screen()  

def listar_campers():
    clear_screen()
    print("\n--- Lista de Campers Registrados ---")
    campers = read_json('campers')
    if not campers:
        print("No hay campers registrados.")
    else:
        for camper in campers:
            print(f"ID: {camper['id']}, Nombre: {camper['nombres']} {camper['apellidos']}, Estado: {camper['estado']}, Riesgo: {camper['riesgo']}")


def registrar_notas_inicial():
    clear_screen()
    print("\n--- Registrar Notas Examen Inicial ---")
    campers = read_json('campers')
    listar_campers()
    id_camper = input("Ingrese el ID del camper para registrar notas: ")
    for camper in campers:
        if camper['id'] == id_camper:
            try:
                nota_teorica = float(input("Nota Teórica (0-100): "))
                nota_practica = float(input("Nota Práctica (0-100): "))
                promedio= (nota_teorica + nota_practica) / 2
                aprobado=promedio>=60
                camper['notas_inicial']['teorica'] = nota_teorica
                camper['notas_inicial']['practica'] = nota_practica
                camper['notas_inicial']['aprobado'] = aprobado
                write_json('campers', campers)
                print(f"Notas registradas exitosamente para el camper ID: {id_camper}")
                pause_screen()
                return
            except ValueError:
                print("Entrada inválida. Las notas deben ser números.")
                pause_screen()
                return
    print("Camper no encontrado.")
    pause_screen()

def registrar_trainer():
    clear_screen()
    print("\n--- Registrar Nuevo Trainer ---")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    especialidad = input("Especialidad: ")
    telefono_celular = input("Teléfono Celular: ")
    telefono_fijo = input("Teléfono Fijo: ")

    trainers = read_json('trainers')
    nuevo_id = f"T{len(trainers)+1:03d}"

    nuevo_trainer = {
        "id": nuevo_id,
        "nombres": nombres,
        "apellidos": apellidos,
        "especialidad": especialidad,
        "telefonos": {
            "celular": telefono_celular,
            "fijo": telefono_fijo
        },
        "rutas_asignadas": []
    }

    trainers.append(nuevo_trainer)
    write_json('trainers', trainers)
    print(f"\nTrainer registrado exitosamente con ID: {nuevo_id}")
    pause_screen()

def modulos():
    return [
        "Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)",
        "Programación Web (HTML, CSS y Bootstrap)",
        "Programación formal (Java, JavaScript, C#)",
        "Bases de datos (Mysql, MongoDb y Postgresql)",
        "Backend (NetCore, Spring Boot, NodeJS y Express)"
    ]

def crear_ruta_entrenamiento():
    clear_screen()
    print("\n--- Crear Nueva Ruta de Entrenamiento ---")
    nombre = input("Nombre de la Ruta: ")
    descripcion = input("Descripción: ")

    rutas = read_json('rutas')
    nuevo_id = f"R{len(rutas)+1:03d}"

    nueva_ruta = {
        "id": nuevo_id,
        "nombre": nombre,
        "descripcion": descripcion,
        "modulos": modulos(),
        "trainer_asignado": {}
    }

    rutas.append(nueva_ruta)
    write_json('rutas', rutas)
    print(f"\nRuta de entrenamiento creada exitosamente con ID: {nuevo_id}")
    pause_screen()
    modulos_asignados = modulos()
    selected_modulos = []
    print("\nMódulos Disponibles:")
    for idx, modulo in enumerate(modulos_asignados):
        print(f"{idx + 1}. {modulo}")
    seleccion = input("Seleccione los módulos (números separados por comas, e.g., 1,3,5): ")
    try:
        indices = [int(i.strip()) - 1 for i in seleccion.split(',')]
        for i in indices:
            if 0 <= i < len(modulos_asignados):
                selected_modulos.append(modulos_asignados[i])
        nueva_ruta['modulos'] = selected_modulos
        write_json('rutas', rutas)
        print(f"Módulos asignados exitosamente a la ruta ID: {nuevo_id}")
        pause_screen()
    except ValueError:
        print("Selección inválida.")
        pause_screen()

def gestionar_areas_entrenamiento():
    while True:
        clear_screen()
        print("\n--- Gestionar Áreas de Entrenamiento ---")
        print("1. Listar Áreas")
        print("2. Agregar Nueva Área")
        print("3. Eliminar Área")
        print("4. Volver al Menú Anterior")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            listar_areas()
        elif opcion == '2':
            agregar_area()
        elif opcion == '3':
            eliminar_area()
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")
            pause_screen()
def listar_areas():
    clear_screen()
    print("\n--- Lista de Áreas de Entrenamiento ---")
    areas = read_json('areas')
    if not areas:
        print("No hay áreas registradas.")
    else:
        for area in areas:
            print(f"ID: {area['id']}, Nombre: {area['nombre']}, Descripción: {area['descripcion']}")
    pause_screen()
def agregar_area():
    clear_screen()
    print("\n--- Agregar Nueva Área de Entrenamiento ---")
    nombre = input("Nombre del Área: ")
    descripcion = input("Descripción: ")

    areas = read_json('areas')
    nuevo_id = f"A{len(areas)+1:03d}"

    nueva_area = {
        "id": nuevo_id,
        "nombre": nombre,
        "descripcion": descripcion
    }

    areas.append(nueva_area)
    write_json('areas', areas)
    print(f"\nÁrea de entrenamiento agregada exitosamente con ID: {nuevo_id}")
    pause_screen()
def eliminar_area():
    clear_screen()
    print("\n--- Eliminar Área de Entrenamiento ---")
    areas = read_json('areas')
    listar_areas()
    id_area = input("Ingrese el ID del área a eliminar: ")
    for area in areas:
        if area['id'] == id_area:
            areas.remove(area)
            write_json('areas', areas)
            print(f"Área con ID: {id_area} eliminada exitosamente.")
            pause_screen()
            return
    print("Área no encontrada.")
    pause_screen()
    trainers = read_json('trainers')
def matriculas():
    clear_screen()
    print("\n--- Matricular Camper en Ruta ---")
    campers = read_json('campers')
    listar_campers()
    id_camper = input("Ingrese el ID del camper a matricular: ")
    for camper in campers:
        if camper['id'] == id_camper:
            if not camper['notas_inicial']['aprobado']:
                print("El camper no ha aprobado el examen inicial.")
                pause_screen()
                return
            rutas = read_json('rutas')
            if not rutas:
                print("No hay rutas de entrenamiento disponibles.")
                pause_screen()
                return
            print("\nRutas Disponibles:")
            for ruta in rutas:
                print(f"ID: {ruta['id']}, Nombre: {ruta['nombre']}")    
            id_ruta = input("Ingrese el ID de la ruta para matricular al camper: ")
            for ruta in rutas:
                if ruta['id'] == id_ruta:
                    fecha_inicio = input("Fecha de Inicio (YYYY-MM-DD): ")
                    fecha_fin = input("Fecha de Finalización (YYYY-MM-DD): ")
                    salon = input("Salón de Entrenamiento: ")

                    nueva_matricula = {
                        "ruta_id": id_ruta,
                        "fecha_inicio": fecha_inicio,
                        "fecha_fin": fecha_fin,
                        "salon": salon
                    }
                    if 'rutas_matriculadas' not in camper:
                        camper['rutas_matriculadas'] = []
                    camper['rutas_matriculadas'].append(nueva_matricula)

        
                    write_json('campers', campers)
                    print(f"Camper ID: {id_camper} matriculado exitosamente en la ruta ID: {id_ruta}")
                    pause_screen()
                    return
            print("Ruta no encontrada.")
            pause_screen()
            return
    print("Camper no encontrado.")
    pause_screen()


def registrar_notas_modulo_coordinador():
    clear_screen()
    print("\n--- Registrar/Editar Notas de Módulo ---")
 
    all_campers = read_json('campers') 
    
    if not all_campers:
        print("No hay campers registrados para gestionar notas.")
        pause_screen()
        return


    listar_campers() 
    
    id_camper_input = input("Ingrese el ID del camper para registrar/editar notas de módulo: ").strip()
    
    found_camper = None
    camper_index = -1 
    for i, c in enumerate(all_campers):
        if c.get('id') == id_camper_input:
            found_camper = c
            camper_index = i
            break
    
    if found_camper is None:
        print("Camper no encontrado.")
        pause_screen()
        return


    rutas_matriculadas_del_camper = found_camper.get('rutas_matriculadas', [])

    if not rutas_matriculadas_del_camper:
        print(f"El camper {found_camper.get('nombre', 'N/A')} {found_camper.get('apellido', 'N/A')} no está matriculado en ninguna ruta.")
        pause_screen()
        return

    print("\nRutas Matriculadas:")
    for idx, matricula in enumerate(rutas_matriculadas_del_camper):
        print(f"{idx + 1}. Ruta ID: {matricula.get('ruta_id', 'N/A')}, Fecha Inicio: {matricula.get('fecha_inicio', 'N/A')}, Fecha Fin: {matricula.get('fecha_fin', 'N/A')}")
    
    seleccion = input("Seleccione la ruta (número): ").strip()
    try:
        indice_ruta = int(seleccion) - 1
        if not (0 <= indice_ruta < len(rutas_matriculadas_del_camper)):
            print("Selección de ruta inválida.")
            pause_screen()
            return
        
        ruta_matriculada_seleccionada = rutas_matriculadas_del_camper[indice_ruta]
        
        modulos_disponibles = modulos() 
        
        if not modulos_disponibles:
            print("No hay módulos disponibles para asignar notas.")
            pause_screen()
            return

        print("\nMódulos Disponibles:")
        for idx, modulo_nombre in enumerate(modulos_disponibles):
            print(f"{idx + 1}. {modulo_nombre}")
        
        seleccion_modulo = input("Seleccione el módulo para registrar/editar nota (número): ").strip()
        try:
            indice_modulo = int(seleccion_modulo) - 1
            if not (0 <= indice_modulo < len(modulos_disponibles)):
                print("Selección de módulo inválida.")
                pause_screen()
                return
            
            modulo_seleccionado_nombre = modulos_disponibles[indice_modulo]
            
            if 'modulos_notas' not in ruta_matriculada_seleccionada:
                ruta_matriculada_seleccionada['modulos_notas'] = {} 

            if modulo_seleccionado_nombre not in ruta_matriculada_seleccionada['modulos_notas']:
                ruta_matriculada_seleccionada['modulos_notas'][modulo_seleccionado_nombre] = {"nota": 0, "aprobado": False}

            nota_actual = ruta_matriculada_seleccionada['modulos_notas'][modulo_seleccionado_nombre].get('nota', 0)
            
            try:
                nota_input = input(f"Ingrese la nota para el módulo '{modulo_seleccionado_nombre}' (0-100, actual: {nota_actual}): ").strip()
                if nota_input == "":
                    print("No se ingresó ninguna nota. La nota no fue modificada.")
                    pause_screen()
                    return

                nota = float(nota_input)
                if not (0 <= nota <= 100):
                    print("Nota fuera del rango (0-100). No se guardará.")
                    pause_screen()
                    return

                ruta_matriculada_seleccionada['modulos_notas'][modulo_seleccionado_nombre]['nota'] = nota
                ruta_matriculada_seleccionada['modulos_notas'][modulo_seleccionado_nombre]['aprobado'] = nota >= 60 
                
                print(f"Nota actualizada para el módulo '{modulo_seleccionado_nombre}'.")
                all_campers[camper_index] = found_camper 
                write_json('campers', all_campers)
                print("Cambios guardados exitosamente.")
                pause_screen()
                return

            except ValueError:
                print("Entrada inválida para la nota. Por favor, ingrese un número.")
                pause_screen()
                return

        except ValueError:
            print("Entrada de módulo inválida. Por favor, ingrese un número.")
            pause_screen()
            return

    except ValueError:
        print("Entrada de ruta inválida. Por favor, ingrese un número.")
        pause_screen()
        return
        




        
def asignar_trainer_y_salon_a_ruta():
    clear_screen()
    print("\n--- Asignar Trainer y Salón a Ruta ---")
    rutas = read_json('rutas')
    if not rutas:
        print("No hay rutas de entrenamiento disponibles.")
        pause_screen()
        return
    print("\nRutas Disponibles:")
    for ruta in rutas:
        print(f"ID: {ruta['id']}, Nombre: {ruta['nombre']}")
    id_ruta = input("Ingrese el ID de la ruta para asignar trainer y salón: ")
    for ruta in rutas:
        if ruta['id'] == id_ruta:
            trainers = read_json('trainers')
            if not trainers:
                print("No hay trainers disponibles.")
                pause_screen()
                return
            print("\nTrainers Disponibles:")
            for trainer in trainers:
                print(f"ID: {trainer['id']}, Nombre: {trainer['nombres']} {trainer['apellidos']}, Especialidad: {trainer['especialidad']}")
            id_trainer = input("Ingrese el ID del trainer a asignar: ")
            for trainer in trainers:
                if trainer['id'] == id_trainer:
                    salon = input("Salón de Entrenamiento: ")
                    if 'trainer_asignado' not in ruta:
                        ruta['trainer_asignado'] = {}
                    ruta['trainer_asignado']['id'] = id_trainer
                    ruta['trainer_asignado']['salon'] = salon
                    write_json('rutas', rutas)
                    print(f"Trainer ID: {id_trainer} asignado exitosamente a la ruta ID: {id_ruta} en el salón: {salon}")
                    pause_screen()
                    return
            print("Trainer no encontrado.")
            pause_screen()
            return
    print("Ruta no encontrada.")
    pause_screen()





