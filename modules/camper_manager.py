from modules.utils import read_json, clear_screen, pause_screen # Correcto

def ver_informacion_personal(id_camper):
    clear_screen()
    campers = read_json('campers')
    for camper in campers:
        if camper['id'] == id_camper:
            print("\n--- Información Personal del Camper ---")
            print(f"ID: {camper['id']}")
            print(f"Nombres: {camper['nombres']}")
            print(f"Apellidos: {camper['apellidos']}")
            print(f"Dirección: {camper['direccion']}")
            print(f"Acudiente: {camper['acudiente']}")
            print(f"Teléfonos: Celular - {camper['telefonos']['celular']}, Fijo - {camper['telefonos']['fijo']}")
            print(f"Estado: {camper['estado']}")
            print(f"Riesgo: {camper['riesgo']}")
            pause_screen()
            return
    print("Camper no encontrado.")
    pause_screen()

def ver_notas(id_camper):
    clear_screen()
    campers = read_json('campers')
    for camper in campers:
        if camper['id'] == id_camper:
            print("\n--- Notas del Camper ---")
            print("--- Examen Inicial ---")
            print(f"Nota Teórica: {camper['notas_inicial']['teorica']}")
            print(f"Nota Práctica: {camper['notas_inicial']['practica']}")
            print(f"Aprobado Examen Inicial: {camper['notas_inicial']['aprobado']}")

            print("\n--- Notas por Módulo ---")
            if not camper['modulos_notas']:
                print("No hay notas de módulos registradas.")
            else:
                for nota_modulo in camper['modulos_notas']:
                    print(f"\nMódulo: {nota_modulo['modulo']}")
                    print(f"  Nota Teórica: {nota_modulo['nota_teorica']}")
                    print(f"  Nota Práctica: {nota_modulo['nota_practica']}")
                    print(f"  Quices/Trabajos: {nota_modulo['quices_trabajos']}")
                    print(f"  Nota Final: {nota_modulo['nota_final']}")
                    print(f"  Aprobado Módulo: {nota_modulo['aprobado']}")
            pause_screen()
            return
    print("Camper no encontrado.")
    pause_screen()

def menu_camper(id_camper):
    while True:
        clear_screen()
        print("\n--- Menú Camper ---")
        print("1. Ver Información Personal")
        print("2. Ver Notas")
        print("3. Cerrar Sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ver_informacion_personal(id_camper)
        elif opcion == '2':
            ver_notas(id_camper)
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            pause_screen()