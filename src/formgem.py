import argparse
import os
import sys

src_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(src_dir)

sys.path.insert(0, src_dir)
sys.path.insert(0, project_root)

from analizador_semantico import analyze, print_report
from generador_js import generate as generate_js

try:
    from generador_fastapi import generate as generate_fastapi
except ImportError:
    from generador_fastapi import generate_fastapi_project as generate_fastapi

from generator.html_generator import generate_html


BANNER = """

         FormGem Compiler v1.0
   .fg -> Analisis Semantico + Generadores
"""


def _resolve_output_path(filepath: str, output: str | None, target: str) -> str:
    if output:
        return output

    base_name = os.path.splitext(os.path.basename(filepath))[0]
    out_dir = os.path.dirname(os.path.abspath(filepath))

    if target == "html":
        suffix = ".html"
    elif target == "js":
        suffix = ".js"
    else:
        suffix = "_backend.py"

    return os.path.join(out_dir, base_name + suffix)


def _write_output(out_path: str, code: str, target: str) -> bool:
    try:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(code)

    except OSError as e:
        print(f"\n No se pudo escribir el archivo de salida ({target}): {e}")
        return False

    return True


def _generar_html(result, filepath: str, out_path: str):
    form = result["form"]

    try:
        html_result = generate_html(form, out_path)

        if isinstance(html_result, str):
            _write_output(out_path, html_result, "html")

    except TypeError:
        html_result = generate_html(result, filepath)

        if isinstance(html_result, str):
            _write_output(out_path, html_result, "html")


def procesar(filepath: str, output: str | None = None, solo_validar: bool = False, target: str = "html"):
    if not os.path.isfile(filepath):
        print(f" Archivo no encontrado: {filepath}")
        return False

    print("-" * 60)
    print("  FASE 1 - Analisis Semantico")
    print("-" * 60)

    result = analyze(filepath)
    print_report(result, filepath)

    if not result["ok"]:
        print("\n Pipeline detenido: corrige los errores semanticos primero.")
        return False

    if solo_validar:
        print("\n Modo --solo-validar: analisis completado, sin generacion de codigo.")
        return True

    if target == "ambos":
        targets = ["js", "fastapi"]
    elif target == "todos":
        targets = ["html", "js", "fastapi"]
    else:
        targets = [target]

    generated_outputs = []

    for current_target in targets:
        print()
        print("-" * 60)

        if current_target == "html":
            print("  FASE 2 - Generacion de HTML")
        elif current_target == "js":
            print("  FASE 2 - Generacion de JavaScript")
        else:
            print("  FASE 2 - Generacion de Backend FastAPI")

        print("-" * 60)

        try:
            out_path = _resolve_output_path(
                filepath,
                output if len(targets) == 1 else None,
                current_target
            )

            if current_target == "html":
                _generar_html(result, filepath, out_path)
                total_lines = 0

            elif current_target == "js":
                code = generate_js(result, filepath)

                if not _write_output(out_path, code, current_target):
                    return False

                total_lines = code.count("\n")

            else:
                code = generate_fastapi(result, filepath)

                if isinstance(code, dict):
                    base_name = os.path.splitext(os.path.basename(filepath))[0]
                    out_dir = os.path.dirname(os.path.abspath(filepath))
                    api_dir = os.path.join(out_dir, base_name + "_api")

                    for rel_path, content in code.items():
                        full_path = os.path.join(api_dir, rel_path)
                        os.makedirs(os.path.dirname(full_path), exist_ok=True)

                        with open(full_path, "w", encoding="utf-8") as f:
                            f.write(content)

                    out_path = api_dir
                    total_lines = sum(content.count("\n") for content in code.values())

                else:
                    if not _write_output(out_path, code, current_target):
                        return False

                    total_lines = code.count("\n")

        except Exception as e:
            print(f"\n Error en la generacion ({current_target}): {e}")
            return False

        generated_outputs.append((current_target, out_path, total_lines))

    for current_target, out_path, total_lines in generated_outputs:
        if current_target == "html":
            print(f"\n   Archivo HTML generado    : {out_path}")
        elif current_target == "js":
            print(f"   Archivo JS generado      : {out_path}")
            print(f"   Lineas generadas         : {total_lines}")
        else:
            print(f"   Archivo FastAPI generado : {out_path}")
            print(f"   Lineas generadas         : {total_lines}")

    form = result["form"]

    if form:
        total_campos = sum(len(s.fields) for s in form.sections)

        print(f"   Formulario               : {form.name}")
        print(f"   Secciones                : {len(form.sections)}")
        print(f"   Campos totales           : {total_campos}")

    print("-" * 60)
    return True


def main():
    print(BANNER)

    parser = argparse.ArgumentParser(
        description="FormGem - Compilador de formularios",
        epilog="""
Ejemplos:
  py src/formgem.py examples/formulario_completo.fg
  py src/formgem.py examples/registro_empleado.fg --target html
  py src/formgem.py examples/registro_empleado.fg --target js
  py src/formgem.py examples/registro_empleado.fg --target fastapi
  py src/formgem.py examples/registro_empleado.fg --target ambos
  py src/formgem.py examples/registro_empleado.fg --target todos
  py src/formgem.py examples/formulario_completo.fg --solo-validar
        """,
    )

    parser.add_argument("archivos", nargs="+", help="Uno o mas archivos .fg")
    parser.add_argument("-o", "--output", help="Archivo de salida (solo con un .fg y un solo target)")

    parser.add_argument(
        "--target",
        choices=["html", "js", "fastapi", "ambos", "todos"],
        default="html",
        help="Generador a ejecutar"
    )

    parser.add_argument(
        "--solo-validar",
        action="store_true",
        help="Solo analisis semantico, sin generar codigo"
    )

    args = parser.parse_args()

    if args.output and (len(args.archivos) > 1 or args.target in ["ambos", "todos"]):
        print(" La opcion -o/--output solo puede usarse con un unico archivo .fg y un solo target.")
        sys.exit(1)

    hubo_errores = False

    for filepath in args.archivos:
        ok = procesar(
            filepath,
            output=args.output,
            solo_validar=args.solo_validar,
            target=args.target
        )

        if not ok:
            hubo_errores = True

        print()

    sys.exit(1 if hubo_errores else 0)


if __name__ == "__main__":
    main()