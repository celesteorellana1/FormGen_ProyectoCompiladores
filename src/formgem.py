import sys
import os
import argparse

src_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, src_dir)

from analizador_semantico import analyze, print_report
from generador_js import generate
from generador_fastapi import generate_fastapi_project


BANNER = """

         FormGem Compiler v1.0        
   .fg → Análisis Semántico + JS      
"""


def procesar(
    filepath: str,
    output: str = None,
    solo_validar: bool = False,
    generar_fastapi: bool = False,
    con_modelo_db: bool = False
):
    if not os.path.isfile(filepath):
        print(f" Archivo no encontrado: {filepath}")
        return False

    print("-" * 60)
    print("  FASE 1 — Análisis Semántico")
    print("-" * 60)

    result = analyze(filepath)
    print_report(result, filepath)

    if not result['ok']:
        print("\n Pipeline detenido: corrige los errores semánticos primero.")
        return False

    if solo_validar:
        print("\n Modo --solo-validar: análisis completado, sin generación de JS.")
        return True

    print()
    print("-" * 60)
    print("  FASE 2 — Generación de JavaScript")
    print("-" * 60)

    try:
        js_code = generate(result, filepath)
    except ValueError as e:
        print(f"\n Error en la generación: {e}")
        return False

    if output:
        out_path = output
    else:
        base_name = os.path.splitext(os.path.basename(filepath))[0]
        out_dir   = os.path.dirname(os.path.abspath(filepath))
        out_path  = os.path.join(out_dir, base_name + ".js")

    try:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(js_code)
    except OSError as e:
        print(f"\n No se pudo escribir el archivo de salida: {e}")
        return False

    print(f"\n   Archivo JS generado : {out_path}")
    print(f"   Líneas generadas    : {js_code.count(chr(10))}")

    form = result['form']
    if form:
        total_campos = sum(len(s.fields) for s in form.sections)
        print(f"   Formulario          : {form.name}")
        print(f"   Secciones           : {len(form.sections)}")
        print(f"   Campos totales      : {total_campos}")

    if generar_fastapi:
        print()
        print("-" * 60)
        print("  FASE 3 — Generación de Backend FastAPI")
        print("-" * 60)
        try:
            api_files = generate_fastapi_project(result, filepath, include_db_model=con_modelo_db)
        except ValueError as e:
            print(f"\n Error en la generación FastAPI: {e}")
            return False

        if output:
            base_name = os.path.splitext(os.path.basename(output))[0]
            out_dir = os.path.dirname(os.path.abspath(output))
        else:
            base_name = os.path.splitext(os.path.basename(filepath))[0]
            out_dir   = os.path.dirname(os.path.abspath(filepath))
        api_dir = os.path.join(out_dir, base_name + "_api")

        try:
            os.makedirs(api_dir, exist_ok=True)
            for rel_path, content in api_files.items():
                full_path = os.path.join(api_dir, rel_path)
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, "w", encoding="utf-8") as f:
                    f.write(content)
        except OSError as e:
            print(f"\n No se pudo escribir el backend FastAPI: {e}")
            return False

        total_lines = sum(c.count(chr(10)) for c in api_files.values())
        print(f"\n   Carpeta API generada: {api_dir}")
        print(f"   Archivos generados  : {len(api_files)}")
        print(f"   Líneas generadas    : {total_lines}")
        print(f"   Modelo DB opcional  : {'sí' if con_modelo_db else 'no'}")

    print("-" * 60)
    return True


def main():
    print(BANNER)

    parser = argparse.ArgumentParser(
        description="FormGem — Compilador de formularios",
        epilog="""
Ejemplos:
  python formgem.py examples/formulario_completo.fg
  python formgem.py examples/registro_empleado.fg -o mi_form.js
  python formgem.py examples/formulario_completo.fg --solo-validar
  python formgem.py examples/formulario_completo.fg --generar-fastapi
  python formgem.py examples/formulario_completo.fg --generar-fastapi --con-modelo-db
  python formgem.py form1.fg form2.fg form3.fg
        """,
    )
    parser.add_argument("archivos", nargs="+", help="Uno o más archivos .fg")
    parser.add_argument("-o", "--output", help="Archivo .js de salida (solo con un .fg)")
    parser.add_argument("--solo-validar", action="store_true",
                        help="Solo análisis semántico, sin generar JS")
    parser.add_argument("--generar-fastapi", action="store_true",
                        help="Genera backend FastAPI en Python")
    parser.add_argument("--con-modelo-db", action="store_true",
                        help="Incluye modelo de base de datos (SQLAlchemy) en el backend generado")

    args = parser.parse_args()

    if args.output and len(args.archivos) > 1:
        print(" La opción -o/--output solo puede usarse con un único archivo .fg")
        sys.exit(1)

    hubo_errores = False
    for filepath in args.archivos:
        ok = procesar(
            filepath,
            output=args.output,
            solo_validar=args.solo_validar,
            generar_fastapi=args.generar_fastapi,
            con_modelo_db=args.con_modelo_db,
        )
        if not ok:
            hubo_errores = True
        print()

    sys.exit(1 if hubo_errores else 0)


if __name__ == "__main__":
    main()
