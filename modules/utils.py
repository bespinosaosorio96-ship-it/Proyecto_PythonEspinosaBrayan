import json
import os

def read_json(filename):
    try:
        with open(f'data/{filename}.json', 'r') as f:
            data = json.load(f)
            if not isinstance(data, list):
                return []
            return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError: 
        return []

def write_json(filename, data):
    with open(f'data/{filename}.json', 'w') as f:
        json.dump(data, f, indent=4)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause_screen():
    input("\nPresione Enter para continuar...")
def generate_matricula_id(matriculas_data):
    if not matriculas_data:
        return "M-001"
    last_id_num = 0
    for matricula in matriculas_data:
        try:
            if matricula['id_matricula'].startswith("M-"):
                num_part = int(matricula['id_matricula'].split('-')[1])
                if num_part > last_id_num:
                    last_id_num = num_part
        except (IndexError, ValueError):
            continue 
    new_num = last_id_num + 1
    return f"M-{new_num:03d}"