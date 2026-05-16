# FormGen – Generador Inteligente de Formularios Web

FormGen es un compilador desarrollado como proyecto del curso de Compiladores.  
Permite definir formularios web mediante un Lenguaje Específico de Dominio (DSL) y generar automáticamente:

- HTML con Bootstrap 5 (frontend)
- JavaScript con validaciones (cliente)
- Backend en FastAPI (servidor)

El sistema implementa las fases clásicas de un compilador:
- Análisis léxico
- Análisis sintáctico
- Análisis semántico
- Generación de código

## Tecnologías utilizadas

- Python 3.11
- ANTLR4
- Jinja2
- Bootstrap 5
- argparse (CLI)
- FastAPI

## Funcionamiento del sistema

El sistema recibe un archivo `.fg` como entrada, por ejemplo:

form RegistroEmpleado title="Nuevo Empleado"
section DatosPersonales
field nombre
type: string
label: "Nombre completo"
required


Y lo transforma automáticamente en:

- HTML con Bootstrap
- JavaScript con validaciones
- Backend en FastAPI

## División del trabajo

El proyecto fue dividido en módulos:

### Persona 1 — Gramática
- Diseño de la gramática ANTLR
- Construcción del Lexer y Parser

### Persona 2 — Análisis Semántico
- Validación de reglas del lenguaje
- Uso de estructuras internas para representar el formulario

### Persona 3 — Generador HTML
- Generación de formularios HTML con Bootstrap 5
- Uso de diccionario de mapeo (`bootstrap_map.py`)
- Uso de plantillas con Jinja2

### Persona 4 — Generador JavaScript
- Generación de validaciones en el cliente
- Optimización del código JavaScript

### Persona 5 — Generador FastAPI
- Generación del backend en Python
- Creación de endpoints
- Validaciones del lado del servidor

### Persona 6 — CLI + README + Integración
- Integración de todos los módulos
- Implementación de CLI con argparse
- Configuración de instalación con pip

## Comandos utilizados
py src/formgem.py examples/registro_empleado.fg --solo-validar
py src/formgem.py examples/formulario_completo.fg --solo-validar

py src/formgem.py examples/registro_empleado.fg --target html
py src/formgem.py examples/formulario_completo.fg --target html

py src/formgem.py examples/registro_empleado.fg --target js
py src/formgem.py examples/formulario_completo.fg --target js

py src/formgem.py examples/registro_empleado.fg --target fastapi
py src/formgem.py examples/formulario_completo.fg --target fastapi

py src/formgem.py examples/registro_empleado.fg --target todos  
py src/formgem.py examples/formulario_completo.fg --target todos 

## visualizar html generado
start examples\registro_empleado.html
start examples\formulario_completo.html

## para borrar
del examples\*.html
del examples\*.js
del examples\*_backend.py
del output\*.html