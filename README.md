# Proyecto Grupal: Manejo de Merge en GitHub

## Información del Curso

**Asignatura:** Gestión de la Configuración del Software  
**Universidad:** Universidad de Guayaquil  
**Facultad:** Ciencias Matemáticas y Físicas  
**Carrera:** Ingeniería de Software  
**Grupo:** D

## Descripción del Proyecto

Este proyecto es un ejercicio colaborativo diseñado para que los estudiantes practiquen y comprendan el flujo de trabajo con Git y GitHub, específicamente el manejo de **merge**, **pull requests** y **resolución de conflictos**.

El equipo debe:
1. Clonar este repositorio
2. Crear ramas de desarrollo (una por integrante)
3. Realizar cambios en los archivos del proyecto
4. Hacer commits descriptivos
5. Crear pull requests en GitHub
6. Resolver cualquier conflicto de merge que surja
7. Documentar el proceso y lecciones aprendidas

### Estructura del Proyecto

- `README.md` - Este archivo
- `equipo.md` - Información del equipo y reflexiones (TODOS deben editar)
- `src/calculadora.py` - Módulo de calculadora con funciones matemáticas
- `src/test_calculadora.py` - Pruebas unitarias para la calculadora
- `.gitignore` - Archivos a ignorar en Git

## Cómo Clonar el Repositorio

```bash
git clone https://github.com/CesarAlex87/gcs-merge-demo.git
cd gcs-merge-demo
```

## Instrucciones de Trabajo

### 1. Crear tu Rama de Desarrollo

```bash
git checkout -b feature/tu-nombre
```

### 2. Hacer Cambios

Cada integrante debe:
- Editar el archivo `equipo.md` con su información
- Añadir una nueva función a `src/calculadora.py`
- Añadir pruebas correspondientes en `src/test_calculadora.py`

### 3. Hacer Commits

```bash
git add .
git commit -m "feat: descripción clara de los cambios"
```

### 4. Hacer Push de tu Rama

```bash
git push origin feature/tu-nombre
```

### 5. Crear un Pull Request

En GitHub, crea un pull request desde tu rama hacia `main` o `develop`.

### 6. Resolver Conflictos

Si hay conflictos:
1. Los resolverás localmente o en GitHub
2. Los revisarás y asegurarás que el código es correcto
3. Harás un nuevo commit con los cambios resueltos

## Equipo

Los integrantes del equipo se registran en `equipo.md`.

## Requisitos

- Python 3.8 o superior
- Git
- GitHub (cuenta activa)

## Ejecución de Pruebas

```bash
python -m pytest src/test_calculadora.py -v
```

O ejecutar la calculadora directamente:

```bash
python src/calculadora.py
```

## Objetivos de Aprendizaje

- Entender el flujo de trabajo colaborativo en Git
- Practicar la creación y gestión de ramas
- Aprender a resolver conflictos de merge
- Mejorar habilidades de comunicación en equipo
- Escribir commits descriptivos
- Revisar código de compañeros a través de pull requests

## Notas Importantes

- **Commits descriptivos:** Usa mensajes claros y específicos
- **Pequeños cambios:** Es mejor hacer varias commits pequeñas que una sola grande
- **Comunica con tu equipo:** Avisa qué archivo vas a editar para evitar conflictos
- **Resuelve conflictos con cuidado:** Verifica que la solución sea correcta

## Licencia

Este proyecto es con propósitos educativos.

---

Creado para la Universidad de Guayaquil - Gestión de la Configuración del Software
