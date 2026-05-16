import os
from jinja2 import Environment, FileSystemLoader
from analizador_semantico import analyze
from generator.bootstrap_map import (
    FIELD_TYPE_MAP,
    FIELD_CLASS_MAP,
    LABEL_CLASS,
    SECTION_CLASS,
    BUTTON_CLASS,
    FORM_CONTAINER_CLASS,
    CARD_CLASS,
    THEME_MAP,
    LAYOUT_MAP,
)


def enrich_form(form):
    enriched_sections = []

    for section in form.sections:
        enriched_fields = []

        for field in section.fields:
            field_type = (
                getattr(field, "type", None)
                or getattr(field, "field_type", None)
                or "string"
            )
            field_type = str(field_type).lower()

            input_type = FIELD_TYPE_MAP.get(field_type, "text")

            if input_type == "checkbox":
                input_class = FIELD_CLASS_MAP["checkbox"]
            elif input_type == "select":
                input_class = FIELD_CLASS_MAP["select"]
            elif input_type == "textarea":
                input_class = FIELD_CLASS_MAP["textarea"]
            else:
                input_class = FIELD_CLASS_MAP["default"]

            enriched_field = {
                "name": getattr(field, "name", ""),
                "type": field_type,
                "label": getattr(field, "label", None) or getattr(field, "name", ""),
                "required": getattr(field, "required", None)
                if getattr(field, "required", None) is not None
                else getattr(field, "is_required", False),
                "placeholder": getattr(field, "placeholder", "") or "",
                "min_length": getattr(field, "min_length", None),
                "max_length": getattr(field, "max_length", None),
                "min": getattr(field, "min", None)
                if getattr(field, "min", None) is not None
                else getattr(field, "min_val", None),
                "max": getattr(field, "max", None)
                if getattr(field, "max", None) is not None
                else getattr(field, "max_val", None),
                "options": getattr(field, "options", []),
                "icon": getattr(field, "icon", None),

                # Corrección: dejar editable el campo
                "readonly": False,

                "hidden": getattr(field, "is_hidden", False),
                "input_type": input_type,
                "input_class": input_class,
                "label_class": LABEL_CLASS,
                "section_class": SECTION_CLASS,
            }

            enriched_fields.append(enriched_field)

        enriched_section = {
            "name": getattr(section, "name", ""),
            "fields": enriched_fields,
        }

        enriched_sections.append(enriched_section)

    theme_value = getattr(form, "theme", "light") or "light"
    layout_value = getattr(form, "layout", "grid") or "grid"

    enriched_form = {
        "name": getattr(form, "name", "Formulario"),
        "title": getattr(form, "title", None) or getattr(form, "name", "Formulario"),
        "submit": getattr(form, "submit", None) or "Enviar",
        "theme": theme_value,
        "layout": layout_value,
        "theme_class": THEME_MAP.get(theme_value, ""),
        "layout_class": LAYOUT_MAP.get(layout_value, "row"),
        "sections": enriched_sections,
        "button_class": BUTTON_CLASS,
        "form_container_class": FORM_CONTAINER_CLASS,
        "card_class": CARD_CLASS,
    }

    return enriched_form


def generate_html(form, output_file="output/index.html"):
    form_data = enrich_form(form)

    env = Environment(loader=FileSystemLoader("src/generator/templates"))
    template = env.get_template("form.html")

    html = template.render(form=form_data)

    os.makedirs("output", exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"HTML generado correctamente en: {output_file}")


if __name__ == "__main__":
    input_file = "examples/registro_empleado.fg"
    # input_file = "examples/registro_empleado.fg"

    result = analyze(input_file)

    if result["ok"]:
        print("Formulario válido, generando HTML...")
        generate_html(result["form"])
    else:
        print("El formulario tiene errores:")
        for error in result["errors"]:
            print(error)