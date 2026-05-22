import os
import re as _re
from jinja2 import Environment, FileSystemLoader, select_autoescape

from generators.bootstrap_map import ICON_CLASSES

# Construcción del contexto para la plantilla

def _enrich_form(form, on_submit=None, js_filename=None) -> dict:
    submit_method    = None
    submit_action    = None
    success_msg      = None
    success_redirect = None
    error_msg        = None

    if on_submit is not None:
        submit_method    = getattr(on_submit, 'method',      None)
        submit_action    = getattr(on_submit, 'url',         None)
        success_msg      = getattr(on_submit, 'success_msg', None)
        success_redirect = getattr(on_submit, 'success_url', None)
        error_msg        = getattr(on_submit, 'error_msg',   None)

    data = {
        "name":   getattr(form, "name",   "formulario"),
        "theme":  getattr(form, "theme",  "minimal") or "minimal",
        "layout": getattr(form, "layout", "stacked") or "stacked",
        "size":   getattr(form, "size",   "md")      or "md",

        "title":          getattr(form, "title",        None),
        "submit_label":   getattr(form, "submit_label", "Enviar"),
        "cancel_label":   getattr(form, "cancel_label", None),

        "submit_method":    submit_method,
        "submit_action":    submit_action,
        "success_msg":      success_msg,
        "success_redirect": success_redirect,
        "error_msg":        error_msg,

        "js_filename": js_filename,

        "sections": getattr(form, "sections", []),
    }

    for section in data["sections"]:
        for field in section.fields:
            if not hasattr(field, "icon"):
                field.icon = None

    return data

# Renderizado y escritura del HTML final

def generate_html(form, output_path="output/index.html",
                  templates_dir=None,
                  on_submit=None,
                  js_filename=None) -> str:

    if templates_dir is None:
        templates_dir = os.path.join(os.path.dirname(__file__), "..", "templates")

    templates_dir = os.path.abspath(templates_dir)

    if not os.path.isdir(templates_dir):
        raise FileNotFoundError(
            f"No se encontro el directorio de plantillas: {templates_dir}\n"
            "Asegurate de que 'src/templates/form.html' exista."
        )

    env = Environment(
        loader=FileSystemLoader(templates_dir),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=False,
    )

    env.filters["icon_class"] = lambda key: ICON_CLASSES.get(key, "")

    def _section_title(name: str) -> str:
        s = name.replace("_", " ")
        s = _re.sub(r"([a-z])([A-Z])", r"\1 \2", s)
        return s.title()
    env.filters["section_title"] = _section_title

    template = env.get_template("form.html")

    form_data = _enrich_form(form, on_submit=on_submit, js_filename=js_filename)
    html = template.render(form=type("FormDict", (), form_data)())

    output_path = os.path.abspath(output_path)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(html.strip())

    print(f"✅ HTML generado correctamente → {output_path}")
    return output_path
