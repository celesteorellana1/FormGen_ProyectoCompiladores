# Clases CSS de Bootstrap por tema, layout y tamaño

THEME_CLASSES = {
    "dark":    "bg-dark text-white",
    "light":   "bg-light text-dark",
    "primary": "bg-primary text-white",
    "minimal": "",
}

LAYOUT_CLASSES = {
    "stacked": "",
    "inline":  "form-inline",
    "grid":    "row col-md-6",
}

SIZE_CLASSES = {
    "sm": {"input": "form-control-sm", "btn": "btn-sm"},
    "md": {"input": "form-control",    "btn": ""},
    "lg": {"input": "form-control-lg", "btn": "btn-lg"},
}

# Mapeo de tipos DSL a atributos HTML

TYPE_TO_HTML = {
    "string":   {"tag": "input",    "type": "text"},
    "email":    {"tag": "input",    "type": "email"},
    "password": {"tag": "input",    "type": "password"},
    "int":      {"tag": "input",    "type": "number"},
    "float":    {"tag": "input",    "type": "number", "step": "0.01"},
    "date":     {"tag": "input",    "type": "date"},
    "boolean":  {"tag": "input",    "type": "checkbox"},
    "select":   {"tag": "select"},
    "textarea": {"tag": "textarea"},
}

ICON_CLASSES = {
    "person":   "bi-person",
    "lock":     "bi-lock",
    "envelope": "bi-envelope",
    "phone":    "bi-telephone",
    "calendar": "bi-calendar",
    "search":   "bi-search",
    "eye":      "bi-eye",
}
