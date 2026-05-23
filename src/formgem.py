import argparse
import os
import sys

src_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, src_dir)

from analizador_semantico import analyze, print_report
from generators.generador_fastapi import generate as generate_fastapi
from generators.generador_js import generate as generate_js
from generators.html_generator import generate_html

BANNER = """

         FormGem Compiler v1.0
   .fg -> Analisis Semantico + Generadores
"""

# Helpers de rutas y escritura

def _resolve_output_path(filepath: str, output: str | None, target: str) -> str:
    if output:
        return output

    base_name = os.path.splitext(os.path.basename(filepath))[0]

    # Directorio actual donde está parado el usuario
    cwd = os.getcwd()
    output_dir = os.path.join(cwd, "output")

    if target == "html":
        # Si existe carpeta output la usa, si no genera en la raiz
        if os.path.isdir(output_dir):
            return os.path.join(output_dir, base_name + ".html")
        return os.path.join(cwd, base_name + ".html")
    elif target == "js":
        if os.path.isdir(output_dir):
            return os.path.join(output_dir, base_name + ".js")
        return os.path.join(cwd, base_name + ".js")
    else:
        if os.path.isdir(output_dir):
            return os.path.join(output_dir, base_name + "_backend.py")
        return os.path.join(cwd, base_name + "_backend.py")


def _write_output(out_path: str, code: str, target: str) -> bool:
    try:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(code)
    except OSError as e:
        print(f"\n No se pudo escribir el archivo de salida ({target}): {e}")
        return False
    return True

# Pipeline principal

def procesar(filepath: str, output: str | None = None,
             solo_validar: bool = False, target: str = "html"):
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
                base_name = os.path.splitext(os.path.basename(filepath))[0]
                generate_html(
                    result["form"],
                    output_path=out_path,
                    on_submit=result.get("on_submit"),
                    js_filename=base_name + ".js",
                )
                total_lines = 0

            elif current_target == "js":
                code = generate_js(result, filepath)
                if not _write_output(out_path, code, current_target):
                    return False
                total_lines = code.count("\n")

            else:
                code = generate_fastapi(result, filepath)
                if not _write_output(out_path, code, current_target):
                    return False
                total_lines = code.count("\n")

        except ValueError as e:
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

# Entrypoint CLI

def main():
    print(BANNER)

    parser = argparse.ArgumentParser(
        description="FormGem - Compilador de formularios",
        epilog="""
Ejemplos:
  python formgem.py examples/formulario_completo.fg
  python formgem.py examples/registro_empleado.fg --target html
  python formgem.py examples/registro_empleado.fg --target js
  python formgem.py examples/registro_empleado.fg --target fastapi
  python formgem.py examples/registro_empleado.fg --target ambos
  python formgem.py examples/registro_empleado.fg --target todos
  python formgem.py examples/formulario_completo.fg --solo-validar
  python formgem.py form1.fg form2.fg form3.fg
        """,
    )

    parser.add_argument("archivos", nargs="+", help="Uno o mas archivos .fg")
    parser.add_argument("-o", "--output",
                        help="Archivo de salida (solo con un .fg y un solo target)")
    parser.add_argument(
        "--target",
        choices=["html", "js", "fastapi", "ambos", "todos"],
        default="html",
        help="Generador a ejecutar",
    )
    parser.add_argument(
        "--solo-validar",
        action="store_true",
        help="Solo analisis semantico, sin generar codigo",
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
            target=args.target,
        )
        if not ok:
            hubo_errores = True
        print()

    sys.exit(1 if hubo_errores else 0)


if __name__ == "__main__":
    main()
