# clean_migrations

`clean_migrations` es una herramienta que elimina los archivos de migraciones generados en proyectos Django, excepto el archivo `__init__.py`.

### ¿Por qué usar `clean_migrations`?

En proyectos Django, las migraciones pueden acumularse con el tiempo, especialmente durante el desarrollo. Este script facilita la limpieza de las migraciones de todas las aplicaciones de un proyecto de manera rápida y sencilla.

## Características

- Borra todos los archivos de migraciones (`.py`) excepto `__init__.py`.
- Recorre automáticamente todas las aplicaciones en tu proyecto Django.
- Fácil de usar desde la línea de comandos o como módulo en tu código.

---

## Instalación
Instala la herramienta directamente desde PyPI con:

```bash
pip install clean_migrations
```

## Uso
Desde la línea de comandos:
- Ejecuta el siguiente comando, especificando la ruta de tu proyecto Django:

```bash
clean-migrations /ruta/a/tu/proyecto
```

- Si no se especifica la ruta, se usa el directorio actual.
Ejemplo:

```bash
clean-migrations .
```

- Desde código Python También puedes usar clean_migrations como módulo en tu código:

```python
from clean_migrations.main import clean_migrations

clean_migrations("/ruta/a/tu/proyecto")
```

# Ejemplo de Salida
```plaintext
Procesando migraciones para la app: myapp
Archivo eliminado: 0001_initial.py
Archivo eliminado: 0002_auto_20240101_1234.py
No se encontró carpeta de migraciones para la app: another_app
¡Limpieza de archivos de migraciones completada!
```
## Requisitos
- Python 3.6 o superior
- Un proyecto Django con estructuras de carpetas estándar.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar esta herramienta:

1. Haz un fork del repositorio.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Envía un pull request

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

