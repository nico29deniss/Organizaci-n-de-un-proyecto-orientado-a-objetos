import os


def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print(f"El archivo {ruta_script} no se encontró en {ruta_script_absoluta}.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo {ruta_script}: {e}")


def mostrar_menu_opciones(opciones):
    for key in opciones:
        print(f"{key} - {os.path.basename(opciones[key])}")


def mostrar_menu():
    ruta_base = os.path.dirname(os.path.abspath(__file__))

    opciones = {
        '1': {
            '1': {
                'Submenú': '1.2 Técnicas de Programación',
                '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py'
            },
            '2': {
                'Submenú': '2.1 Programación Tradicional frente a POO',
                '1': 'Unidad 1/2.1. Programacion tradicional frente a Poo/2.1-1. Ejemplo Programacion tradicional frente a POO.py',
                '2': 'Unidad 1/2.1. Programacion tradicional frente a Poo/2.1-2. Ejemplo No. 02 - POO.py',
                '3': 'Unidad 1/2.1. Programacion tradicional frente a Poo/2.1-3. Ejemplo No. 02 - Programacion Tradicional.py',
                '4': 'Unidad 1/2.1. Programacion tradicional frente a Poo/2.1-4. Tarea Programacion Tradicional.py',
                '5': 'Unidad 1/2.1. Programacion tradicional frente a Poo/2.1-5. Tarea Programacion POO.py'
            },
            '3': {
                'Submenú': '2.2 Características de la POO',
                '1': 'Unidad 1/2.2. Caracteristicas de la POO/2.2-1. Ejemplo - Carro y Acciones.py',
                '2': 'Unidad 1/2.2. Caracteristicas de la POO/2.2-2. Ejemplo - Carro Relacion Persona.py',
                '3': 'Unidad 1/2.2. Caracteristicas de la POO/2.2-3. Ejemplo - Print Atributos Clase.py',
                '4': 'Unidad 1/2.2. Caracteristicas de la POO/2.2-4. Ejemplo - Libro, Bibliotecario y Usuario.py',
                '5': 'Unidad 1/2.2. Caracteristicas de la POO/2.2-5. Ejemplo - Libro, Persona y Rol.py'
            }
        },
        '2': {
            '1': {
                'Submenú': '1.1 Tipos de Datos e Identificadores',
                '1': 'Unidad 2/1.1. Tipos de Datos e identificadores/2.1.1-1 - Nomenclatura en Python.py',
                '2': 'Unidad 2/1.1. Tipos de Datos e identificadores/2.1.1-2 - Ejemplo Identificadores correctos (Python).py',
                '3': 'Unidad 2/1.1. Tipos de Datos e identificadores/2.1.1-3 - Ejemplo Identificadores poco claros (Python).py'
            },
            '2': {
                'Submenú': '1.2 Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo',
                '1': 'Unidad 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-1 - Ejemplo Clase y Objeto (Coche).py',
                '2': 'Unidad 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-1 - Ejemplo Clase y Objeto (Libro).py',
                '3': 'Unidad 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-2 - Ejemplo Herencia (Coche).py',
                '4': 'Unidad 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-2 - Ejemplo Herencia Extendido (Coche-Vehiculo).py',
                '5': 'Unidad 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-3 - Ejemplo Encapsulación (Cuenta Bancaria).py',
                '6': 'Unidad 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-4 - Ejemplo Polimorfismo (Sobrecarga).py',
                '7': 'Unidad 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-4 - Ejemplo Polimorfismo (Sobreescritura).py'
            },
            '3': {
                'Submenú': '2.1 Constructores y Destructores',
                '1': 'Unidad 2/2.1. Constructores y Destructores/2.2.1-1 - Uso de constructor.py',
                '2': 'Unidad 2/2.1. Constructores y Destructores/2.2.1-2 - Uso del destructor.py'
            }
        }
    }

    while True:
        print("\nMenú Principal - Dashboard")
        print("1 - Unidad 1")
        print("2 - Unidad 2")
        print("0 - Salir")

        eleccion = input("Elige una unidad o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            while True:
                unidad = opciones[eleccion]
                for key in unidad:
                    if key != 'Submenú':
                        print(f"{key} - {unidad[key]['Submenú']}")
                print("0 - Volver al menú principal")

                subeleccion = input("Elige una sección o '0' para volver al menú principal: ")
                if subeleccion == '0':
                    break
                elif subeleccion in unidad:
                    subunidad = unidad[subeleccion]
                    print(f"\n{subunidad['Submenú']}")
                    mostrar_menu_opciones(subunidad)
                    script_elegido = input("Elige un script para ver su código: ")
                    if script_elegido in subunidad:
                        ruta_script = os.path.join(ruta_base, subunidad[script_elegido])
                        mostrar_codigo(ruta_script)
                    else:
                        print("Opción no válida. Por favor, intenta de nuevo.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    mostrar_menu()
