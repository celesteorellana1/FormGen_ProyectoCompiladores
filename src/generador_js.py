import sys
import os
import argparse
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'generated'))


def _js_str(text):
    return text.replace('\\', '\\\\').replace('"', '\\"')


def _indent(lines, level=1):
    pad = "  " * level
    return [pad + l for l in lines]


def _collect_shared_validators(fields):
    rule_count = Counter()
    for f in fields:
        for sig in _field_rule_signatures(f):
            rule_count[sig] += 1
    shared = {}
    helper_idx = 1
    for sig, count in rule_count.items():
        if count >= 2:
            shared[sig] = f"_validar_helper_{helper_idx}"
            helper_idx += 1
    return shared


def _field_rule_signatures(f):
    sigs = []
    if f.is_required:
        sigs.append("required")
    if f.min_length is not None:
        sigs.append(f"min_length:{f.min_length}")
    if f.max_length is not None:
        sigs.append(f"max_length:{f.max_length}")
    if f.min_val is not None:
        sigs.append(f"min_val:{f.min_val}")
    if f.max_val is not None:
        sigs.append(f"max_val:{f.max_val}")
    if f.field_type == "email":
        sigs.append("email_format")
    if f.field_type == "date":
        sigs.append("date_format")
    return sigs


def _gen_shared_helpers(shared):
    if not shared:
        return []
    lines = []
    for sig, fname in shared.items():
        lines.append(f"function {fname}(value) {{")
        body = _sig_to_check(sig)
        lines.extend(_indent(body))
        lines.append("  return null;")
        lines.append("}")
        lines.append("")
    return lines


def _sig_to_check(sig):
    if sig == "required":
        return [
            'const v = (value ?? "").toString().trim();',
            'if (!v) return "Este campo es requerido";',
        ]
    if sig.startswith("min_length:"):
        n = sig.split(":")[1]
        return [f'if ((value ?? "").toString().trim().length < {n}) return "Minimo {n} caracteres";']
    if sig.startswith("max_length:"):
        n = sig.split(":")[1]
        return [f'if ((value ?? "").toString().trim().length > {n}) return "Maximo {n} caracteres";']
    if sig.startswith("min_val:"):
        n = sig.split(":")[1]
        return [f'if (Number(value) < {n}) return "El valor minimo es {n}";']
    if sig.startswith("max_val:"):
        n = sig.split(":")[1]
        return [f'if (Number(value) > {n}) return "El valor maximo es {n}";']
    if sig == "email_format":
        return [
            'const emailRx = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;',
            'if (value && !emailRx.test(value)) return "Ingresa un correo electronico valido";',
        ]
    if sig == "date_format":
        return [
            'if (value && isNaN(Date.parse(value))) return "Fecha invalida";',
        ]
    return []


def _gen_field_validator(f, shared, label):
    lines = []
    field_label = _js_str(label or f.name)
    lines.append(f"  {f.name}(value) {{")

    if f.is_hidden or f.is_readonly:
        lines.append("    return null;")
        lines.append("  },")
        lines.append("")
        return lines

    if f.is_required:
        sig_req = "required"
        if sig_req in shared:
            lines.append(f"    {{ const _e = {shared[sig_req]}(value); if (_e) return _e; }}")
        else:
            lines.append('    const _v = (value ?? "").toString().trim();')
            lines.append(f'    if (!_v) return "{_js_str(field_label)} es requerido";')

    if f.field_type == "email":
        sig = "email_format"
        if sig in shared:
            lines.append(f"    {{ const _e = {shared[sig]}(value); if (_e) return _e; }}")
        else:
            lines.append("    const _emailRx = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;")
            lines.append('    if (value && !_emailRx.test(value)) return "Ingresa un correo electronico valido";')

    if f.field_type == "date":
        sig = "date_format"
        if sig in shared:
            lines.append(f"    {{ const _e = {shared[sig]}(value); if (_e) return _e; }}")
        else:
            lines.append('    if (value && isNaN(Date.parse(value))) return "Fecha invalida";')

    if f.min_length is not None:
        sig = f"min_length:{f.min_length}"
        if sig in shared:
            lines.append(f"    {{ const _e = {shared[sig]}(value); if (_e) return _e; }}")
        else:
            lines.append(f'    if ((value ?? "").toString().trim().length < {f.min_length}) return "Minimo {f.min_length} caracteres";')

    if f.max_length is not None:
        sig = f"max_length:{f.max_length}"
        if sig in shared:
            lines.append(f"    {{ const _e = {shared[sig]}(value); if (_e) return _e; }}")
        else:
            lines.append(f'    if ((value ?? "").toString().trim().length > {f.max_length}) return "Maximo {f.max_length} caracteres";')

    if f.min_val is not None:
        sig = f"min_val:{f.min_val}"
        if sig in shared:
            lines.append(f"    {{ const _e = {shared[sig]}(value); if (_e) return _e; }}")
        else:
            lines.append(f'    if (Number(value) < {f.min_val}) return "El valor minimo es {f.min_val}";')

    if f.max_val is not None:
        sig = f"max_val:{f.max_val}"
        if sig in shared:
            lines.append(f"    {{ const _e = {shared[sig]}(value); if (_e) return _e; }}")
        else:
            lines.append(f'    if (Number(value) > {f.max_val}) return "El valor maximo es {f.max_val}";')

    if f.field_type == "select" and f.options:
        opts_js = ", ".join(f'"{_js_str(o)}"' for o in f.options)
        lines.append(f"    const _opts = [{opts_js}];")
        lines.append('    if (value && !_opts.includes(value)) return "Opcion no valida";')

    lines.append("    return null;")
    lines.append("  },")
    lines.append("")
    return lines


def _gen_submit_handler(form, on_submit_info):
    lines = []
    lines.append(f"async function enviar{form.name}(datos) {{")
    lines.append("  const errores = {};")
    lines.append("  for (const [campo, validar] of Object.entries(validaciones)) {")
    lines.append("    const error = validar(datos[campo] ?? \"\");")
    lines.append("    if (error) errores[campo] = error;")
    lines.append("  }")
    lines.append("  if (Object.keys(errores).length > 0) {")
    lines.append("    return { ok: false, errores };")
    lines.append("  }")
    lines.append("")

    if on_submit_info:
        method = on_submit_info.get("method", "POST")
        url    = on_submit_info.get("url", "/api/submit")
        s_msg  = _js_str(on_submit_info.get("success_msg", "Operacion exitosa"))
        e_msg  = _js_str(on_submit_info.get("error_msg", "Error al procesar"))
        s_url  = on_submit_info.get("success_url")

        lines.append("  try {")
        lines.append(f'    const respuesta = await fetch("{url}", {{')
        lines.append(f'      method: "{method}",')
        lines.append('      headers: { "Content-Type": "application/json" },')
        lines.append("      body: JSON.stringify(datos),")
        lines.append("    });")
        lines.append("    if (respuesta.ok) {")
        lines.append(f'      console.info("{s_msg}");')
        if s_url:
            lines.append(f'      window.location.href = "{s_url}";')
        lines.append("      return { ok: true };")
        lines.append("    } else {")
        lines.append(f'      return {{ ok: false, mensaje: "{e_msg}" }};')
        lines.append("    }")
        lines.append("  } catch (err) {")
        lines.append(f'    return {{ ok: false, mensaje: "{e_msg}: " + err.message }};')
        lines.append("  }")
    else:
        lines.append('  console.warn("No se definio bloque on_submit en el formulario.");')
        lines.append('  return { ok: false, mensaje: "Sin accion de envio configurada" };')

    lines.append("}")
    lines.append("")
    return lines


def _gen_realtime_activation(form):
    lines = []
    lines.append("function _debounce(fn, ms) {")
    lines.append("  let timer;")
    lines.append("  return (...args) => {")
    lines.append("    clearTimeout(timer);")
    lines.append("    timer = setTimeout(() => fn(...args), ms);")
    lines.append("  };")
    lines.append("}")
    lines.append("")
    lines.append(f"function activar{form.name}(formElement) {{")
    lines.append('  if (!formElement) { console.error("Elemento de formulario no encontrado"); return; }')
    lines.append("  for (const [campo, validar] of Object.entries(validaciones)) {")
    lines.append('    const input = formElement.querySelector(`[name="${campo}"]`);')
    lines.append("    if (!input) continue;")
    lines.append("    const mostrarError = _debounce((valor) => {")
    lines.append("      const error = validar(valor);")
    lines.append('      let msgEl = formElement.querySelector(`[data-error="${campo}"]`);')
    lines.append("      if (!msgEl) {")
    lines.append('        msgEl = document.createElement("span");')
    lines.append('        msgEl.dataset.error = campo;')
    lines.append('        msgEl.style.color = "red";')
    lines.append('        msgEl.style.fontSize = "0.85em";')
    lines.append("        input.insertAdjacentElement('afterend', msgEl);")
    lines.append("      }")
    lines.append('      msgEl.textContent = error ?? "";')
    lines.append("    }, 300);")
    lines.append('    input.addEventListener("input", (e) => mostrarError(e.target.value));')
    lines.append('    input.addEventListener("blur",  (e) => mostrarError(e.target.value));')
    lines.append("  }")
    lines.append('  formElement.addEventListener("submit", async (e) => {')
    lines.append("    e.preventDefault();")
    lines.append("    const datos = Object.fromEntries(new FormData(formElement));")
    lines.append(f"    const resultado = await enviar{form.name}(datos);")
    lines.append("    if (!resultado.ok && resultado.errores) {")
    lines.append("      for (const [campo, msg] of Object.entries(resultado.errores)) {")
    lines.append('        let msgEl = formElement.querySelector(`[data-error="${campo}"]`);')
    lines.append("        if (!msgEl) {")
    lines.append('          const input = formElement.querySelector(`[name="${campo}"]`);')
    lines.append("          if (!input) continue;")
    lines.append('          msgEl = document.createElement("span");')
    lines.append('          msgEl.dataset.error = campo;')
    lines.append('          msgEl.style.color = "red";')
    lines.append('          msgEl.style.fontSize = "0.85em";')
    lines.append("          input.insertAdjacentElement('afterend', msgEl);")
    lines.append("        }")
    lines.append('        msgEl.textContent = msg;')
    lines.append("      }")
    lines.append("    }")
    lines.append("  });")
    lines.append("}")
    lines.append("")
    return lines


def generate(result: dict, source_filename: str = "") -> str:
    if not result['ok']:
        raise ValueError("No se puede generar JS: el analisis semantico reporto errores.")

    form = result['form']
    if form is None:
        raise ValueError("El resultado no contiene informacion de formulario.")

    all_fields = [f for s in form.sections for f in s.fields]
    active_fields = [f for f in all_fields if not f.is_hidden and not f.is_readonly]
    shared = _collect_shared_validators(active_fields)

    label_map = {}
    for s in form.sections:
        for f in s.fields:
            label_map[f.name] = f.name.replace("_", " ").capitalize()

    on_submit_info = result.get('on_submit')

    out = []
    base = os.path.basename(source_filename) if source_filename else "formulario"
    out.append(f"// Generado por FormGem - fuente: {base}")
    out.append(f"// Formulario: {form.name}")
    out.append("")

    out.extend(_gen_shared_helpers(shared))

    out.append(f"const validaciones = {{")
    out.append("")

    for s in form.sections:
        if s.fields:
            out.append(f"  // Seccion: {s.name}")
            for f in s.fields:
                label = label_map.get(f.name, f.name)
                out.extend(_gen_field_validator(f, shared, label))

    out.append("};")
    out.append("")
    out.extend(_gen_submit_handler(form, on_submit_info))
    out.extend(_gen_realtime_activation(form))

    out.append('if (typeof module !== "undefined") {')
    out.append(f"  module.exports = {{ validaciones, enviar{form.name}, activar{form.name} }};")
    out.append("}")
    out.append("")

    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description="FormGem - Generador de JavaScript")
    parser.add_argument("archivo", help="Archivo .fg de entrada")
    parser.add_argument("-o", "--output", help="Archivo .js de salida")
    args = parser.parse_args()

    src_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, src_dir)
    from analizador_semantico import analyze, print_report

    filepath = args.archivo
    if not os.path.isfile(filepath):
        print(f"Archivo no encontrado: {filepath}")
        sys.exit(1)

    result = analyze(filepath)
    print_report(result, filepath)

    if not result['ok']:
        print("Generacion cancelada por errores semanticos.")
        sys.exit(1)

    try:
        js_code = generate(result, filepath)
    except ValueError as e:
        print(f"Error de generacion: {e}")
        sys.exit(1)

    if args.output:
        out_path = args.output
    else:
        base_name = os.path.splitext(os.path.basename(filepath))[0]
        out_dir   = os.path.dirname(os.path.abspath(filepath))
        out_path  = os.path.join(out_dir, base_name + ".js")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(js_code)

    print(f"Archivo generado: {out_path}")
    print(f"Lineas generadas: {js_code.count(chr(10))}")


if __name__ == "__main__":
    main()