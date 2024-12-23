import os

def clean_migrations(project_path):
    """
    Limpia los archivos de migraciones en un proyecto Django.
    
    Args:
        project_path (str): Ruta al proyecto Django.
    """
    # Directorio raíz de las apps dentro del proyecto
    apps_path = os.path.join(project_path)

    # Iterar por todas las carpetas en el proyecto
    for app_name in os.listdir(apps_path):
        app_path = os.path.join(apps_path, app_name)
        migrations_path = os.path.join(app_path, 'migrations')

        # Verificar si la carpeta de migrations existe
        if os.path.isdir(migrations_path):
            print(f"Procesando migraciones para la app: {app_name}")
            for file_name in os.listdir(migrations_path):
                # Ignorar el archivo __init__.py
                if file_name != '__init__.py' and file_name.endswith('.py'):
                    file_path = os.path.join(migrations_path, file_name)
                    os.remove(file_path)
                    print(f"   Archivo eliminado: {file_name}")
        else:
            print(f"No se encontró carpeta de migraciones para la app: {app_name}")

if __name__ == "__main__":
    import argparse

    # Parser para manejar argumentos desde la línea de comandos
    parser = argparse.ArgumentParser(description="Limpia los archivos de migraciones en un proyecto Django.")
    parser.add_argument(
        "project_path",
        type=str,
        nargs="?",
        default=os.getcwd(),
        help="Ruta al proyecto Django (por defecto, el directorio actual)."
    )
    args = parser.parse_args()
    clean_migrations(args.project_path)
    print("¡Limpieza de archivos de migraciones completada!")
