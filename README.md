# Comandos utilizados

## Validar archivo

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

# Visualizar HTML generado
start examples\registro_empleado.html 
start examples\formulario_completo.html

# Limpiar archivos generados

del examples\*.html
del examples\*.js
del examples\*_backend.py
del output\*.html

# FormGen – Generador Inteligente de Formularios Web

FormGen es un compilador desarrollado como proyecto del curso de Compiladores.  
Permite definir formularios web mediante un Lenguaje Específico de Dominio (DSL) y generar automáticamente:

- HTML con Bootstrap 5
- JavaScript con validaciones
- Backend en FastAPI

El sistema implementa las fases clásicas de un compilador:
- Análisis léxico
- Análisis sintáctico
- Análisis semántico
- Optimización
- Generación de código

# Características principales

- DSL declarativo y fácil de leer
- Generación automática de formularios web
- Validaciones automáticas en frontend y backend
- Generación de código optimizado
- Arquitectura modular basada en compiladores
- CLI funcional mediante argparse
- Integración con ANTLR4

# Tecnologías utilizadas

- Python 3.11
- ANTLR4
- Jinja2
- Bootstrap 5
- FastAPI
- argparse
- HTML5
- JavaScript

# Arquitectura del Compilador

```text
Archivo .fg
    ↓
Lexer (ANTLR4)
    ↓
Parser
    ↓
AST
    ↓
Análisis Semántico
    ↓
Optimizador
    ↓
Generador de Código
    ↓
HTML + JS + FastAPI
```

# Flujo de compilación

El sistema recibe un archivo `.fg` como entrada y lo transforma automáticamente en código frontend y backend funcional.

## Ejemplo de entrada

```fg
form RegistroEmpleado title="Nuevo Empleado"

section DatosPersonales

field nombre
    type: string
    label: "Nombre completo"
    required
```

## Salida generada

- HTML responsivo con Bootstrap 5
- JavaScript con validaciones automáticas
- Backend REST con FastAPI

# Instalación

## Clonar el proyecto

```bash
git clone <repositorio>
cd FormGen
```

## Instalar dependencias

```bash
pip install -e .
```

# Fases del compilador

## 1. Análisis Léxico
Reconocimiento de tokens utilizando ANTLR4.

## 2. Análisis Sintáctico
Construcción del árbol sintáctico a partir de la gramática definida.

## 3. Análisis Semántico
Validación de:
- Tipos de datos
- Propiedades válidas
- Campos duplicados
- Themes y layouts permitidos
- Reglas obligatorias del DSL

## 4. Optimización
El compilador implementa optimizaciones como:
- Eliminación de validaciones duplicadas
- Eliminación de código JavaScript innecesario
- Minificación básica de HTML
- Reordenamiento inteligente de campos

## 5. Generación de Código
Generación automática de:
- HTML5 con Bootstrap
- JavaScript
- Backend en FastAPI

# Ejemplos incluidos

El proyecto incluye ejemplos completos en la carpeta:

```text
examples/
```

Entre ellos:
- registro_empleado.fg
- formulario_completo.fg

# División del trabajo

## Persona 1 — Gramática
- Diseño de la gramática ANTLR
- Construcción del Lexer y Parser

## Persona 2 — Análisis Semántico
- Validación de reglas del lenguaje
- Uso de estructuras internas para representar el formulario

## Persona 3 — Generador HTML
- Generación de formularios HTML con Bootstrap 5
- Uso de diccionario de mapeo (`bootstrap_map.py`)
- Uso de plantillas con Jinja2

## Persona 4 — Generador JavaScript
- Generación de validaciones en el cliente
- Optimización del código JavaScript

## Persona 5 — Generador FastAPI
- Generación del backend en Python
- Creación de endpoints
- Validaciones del lado del servidor

## Integración y CLI
- Integración de todos los módulos
- Implementación de CLI con argparse
- Configuración de instalación con pip