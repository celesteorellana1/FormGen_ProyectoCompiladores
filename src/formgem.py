import sys
import os
import argparse

src_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, src_dir)

from analizador_semantico import analyze, print_report
from generador_js import generate


BANNER = """

         FormGem Compiler v1.0        
   .fg → Análisis Semántico + JS      
"""


def procesar(filepath: str, output: str = None, solo_validar: bool = False):
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
  python formgem.py form1.fg form2.fg form3.fg
        """,
    )
    parser.add_argument("archivos", nargs="+", help="Uno o más archivos .fg")
    parser.add_argument("-o", "--output", help="Archivo .js de salida (solo con un .fg)")
    parser.add_argument("--solo-validar", action="store_true",
                        help="Solo análisis semántico, sin generar JS")

    args = parser.parse_args()

    if args.output and len(args.archivos) > 1:
        print(" La opción -o/--output solo puede usarse con un único archivo .fg")
        sys.exit(1)

    hubo_errores = False
    for filepath in args.archivos:
        ok = procesar(filepath, output=args.output, solo_validar=args.solo_validar)
        if not ok:
            hubo_errores = True
        print()

    sys.exit(1 if hubo_errores else 0)


if __name__ == "__main__":
    main()