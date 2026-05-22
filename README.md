# FormGem – Generador Inteligente de Formularios Web

FormGem es un compilador desarrollado como proyecto del curso de Compiladores.  
Permite definir formularios web mediante un Lenguaje Específico de Dominio (DSL) y generar automáticamente:

- **HTML** con Bootstrap 5 (frontend)
- **JavaScript** con validaciones en el cliente
- **Backend** en FastAPI (servidor)

El sistema implementa las fases clásicas de un compilador:
- Análisis léxico y sintáctico (ANTLR4)
- Análisis semántico
- Generación de código

---

## Tecnologías utilizadas

- Python 3.11+
- ANTLR4
- Jinja2
- Bootstrap 5
- argparse (CLI)
- FastAPI / Pydantic

---

## Estructura del proyecto

```
FormGem/
├── antlr-4.13.1-complete.jar
├── requirements.txt
├── pyproject.toml
├── docs/
│   └── grammar.ebnf
├── examples/
│   ├── formulario_completo.fg
│   └── registro_empleado.fg
├── grammar/
│   ├── FormGenLexer.g4
│   └── FormGenParser.g4
├── output/               ← HTML generados
└── src/
    ├── formgem.py        ← CLI principal
    ├── analizador_semantico.py
    ├── test_parse.py
    ├── templates/
    │   └── form.html
    ├── generators/
    │   ├── html_generator.py
    │   ├── generador_js.py
    │   ├── generador_fastapi.py
    │   └── bootstrap_map.py
    └── generated/        ← Código generado por ANTLR (no editar)
```

---

## Instalación

```bash
pip install -r requirements.txt
```

---

## Uso

```bash
# Solo validar semántica
py src/formgem.py examples/registro_empleado.fg --solo-validar
py src/formgem.py examples/formulario_completo.fg --solo-validar

# Generar HTML (se guarda en output/)
py src/formgem.py examples/registro_empleado.fg --target html
py src/formgem.py examples/formulario_completo.fg --target html

# Generar JavaScript
py src/formgem.py examples/registro_empleado.fg --target js
py src/formgem.py examples/formulario_completo.fg --target js

# Generar backend FastAPI
py src/formgem.py examples/registro_empleado.fg --target fastapi
py src/formgem.py examples/formulario_completo.fg --target fastapi

# Generar JS + FastAPI
py src/formgem.py examples/registro_empleado.fg --target ambos

# Generar todo (HTML + JS + FastAPI)
py src/formgem.py examples/formulario_completo.fg --target todos

# Archivo de salida personalizado
py src/formgem.py examples/registro_empleado.fg --target js -o mi_form.js

# Procesar múltiples archivos
py src/formgem.py examples/registro_empleado.fg examples/formulario_completo.fg --target todos
```

---

## División del trabajo

### Persona 1 — Gramática
- Diseño de la gramática ANTLR formal
- Construcción del Lexer y Parser

### Persona 2 — Análisis Semántico
- Validación de reglas del lenguaje con diccionarios internos
- Detección de errores y advertencias semánticas

### Persona 3 — Generador HTML
- Generación de formularios HTML con Bootstrap 5
- Diccionario de mapeo de estilos (`bootstrap_map.py`)
- Plantillas Jinja2 (`src/templates/form.html`)

### Persona 4 — Generador JavaScript
- Generación de validaciones en el cliente
- Validadores compartidos (optimización) y activación en tiempo real con debounce

### Persona 5 — Generador FastAPI
- Generación del backend en Python con modelos Pydantic
- Endpoints y validaciones del lado del servidor

### Persona 6 — CLI + README + Integración
- Integración de todos los módulos
- CLI con argparse (`src/formgem.py`)
- Configuración de instalación con pip (`pyproject.toml`)

---

## Limpieza de archivos generados

```bash
# Windows
del output\*.html
del examples\*.js
del examples\*_backend.py

# Linux / Mac
rm output/*.html
rm examples/*.js
rm examples/*_backend.py
```
