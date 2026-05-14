import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'generated'))

from antlr4 import CommonTokenStream, FileStream, ParseTreeWalker
from generated.FormGenLexer import FormGenLexer
from generated.FormGenParser import FormGenParser
from generated.FormGenParserListener import FormGenParserListener


VALID_PROPS_BY_TYPE = {
    "string":   {"label", "placeholder", "required", "unique", "readonly", "hidden",
                 "default", "min_length", "max_length", "icon"},
    "email":    {"label", "placeholder", "required", "unique", "readonly", "hidden",
                 "default", "min_length", "max_length", "icon"},
    "password": {"label", "placeholder", "required", "unique", "readonly", "hidden",
                 "default", "min_length", "max_length", "icon"},
    "int":      {"label", "placeholder", "required", "unique", "readonly", "hidden",
                 "default", "min", "max", "icon"},
    "float":    {"label", "placeholder", "required", "unique", "readonly", "hidden",
                 "default", "min", "max", "icon"},
    "date":     {"label", "placeholder", "required", "unique", "readonly", "hidden",
                 "default", "icon"},
    "boolean":  {"label", "required", "hidden", "default"},
    "select":   {"label", "placeholder", "required", "unique", "readonly", "hidden",
                 "default", "options", "icon"},
    "textarea": {"label", "placeholder", "required", "readonly", "hidden",
                 "default", "min_length", "max_length"},
}

DEFAULT_VALUE_TYPE = {
    "string":   "string",
    "email":    "string",
    "password": "string",
    "int":      "integer",
    "float":    "number",
    "date":     "string",
    "boolean":  "boolean",
    "select":   "string",
    "textarea": "string",
}

REQUIRES_OPTIONS  = {"select"}
FORBIDS_OPTIONS   = {"string", "email", "password", "int", "float", "date", "boolean", "textarea"}
VALID_ICONS       = {"person", "lock", "envelope", "phone", "calendar", "search", "eye"}
VALID_FIELD_TYPES = set(VALID_PROPS_BY_TYPE.keys())
VALID_THEMES      = {"dark", "light", "primary", "minimal"}
VALID_LAYOUTS     = {"stacked", "inline", "grid"}
VALID_SIZES       = {"sm", "md", "lg"}


class FieldInfo:
    def __init__(self, name, line):
        self.name = name
        self.line = line
        self.field_type = None
        self.props_seen = set()
        self.min_length = None
        self.max_length = None
        self.min_val = None
        self.max_val = None
        self.default_val = None
        self.default_val_kind = None
        self.options = []
        self.is_hidden = False
        self.is_readonly = False
        self.is_required = False
        self.label = None
        self.placeholder = None
        self.icon = None


class FormInfo:
    def __init__(self, name, line):
        self.name = name
        self.line = line
        self.attrs_seen = set()
        self.theme = None
        self.layout = None
        self.size = None
        self.sections = []


class SectionInfo:
    def __init__(self, name, line):
        self.name = name
        self.line = line
        self.fields = []


class SemanticError:
    def __init__(self, line, message):
        self.line = line
        self.message = message

    def __str__(self):
        return f"  ❌ [Línea {self.line}] ERROR: {self.message}"


class SemanticWarning:
    def __init__(self, line, message):
        self.line = line
        self.message = message

    def __str__(self):
        return f"  ⚠️  [Línea {self.line}] ADVERTENCIA: {self.message}"


class SemanticAnalyzer(FormGenParserListener):

    def __init__(self):
        self.errors = []
        self.warnings = []
        self._form = None
        self._current_section = None
        self._current_field = None
        self._field_names_in_section = set()
        self._section_names = set()
        self.on_submit = None

    def _error(self, ctx, msg):
        line = ctx.start.line if hasattr(ctx, 'start') else 0
        self.errors.append(SemanticError(line, msg))

    def _warn(self, ctx, msg):
        line = ctx.start.line if hasattr(ctx, 'start') else 0
        self.warnings.append(SemanticWarning(line, msg))

    def _strip_quotes(self, text):
        if text and text.startswith('"') and text.endswith('"'):
            return text[1:-1]
        return text

    def enterForm_def(self, ctx: FormGenParser.Form_defContext):
        self._form = FormInfo(ctx.identifier().getText(), ctx.start.line)

    def exitForm_def(self, ctx: FormGenParser.Form_defContext):
        if 'title' not in self._form.attrs_seen:
            self._warn(ctx, f"El formulario '{self._form.name}' no tiene atributo 'title'.")

    def enterForm_attr(self, ctx: FormGenParser.Form_attrContext):
        if ctx.TITLE():
            attr = 'title'
        elif ctx.THEME():
            attr = 'theme'
        elif ctx.SUBMIT():
            attr = 'submit'
        elif ctx.CANCEL():
            attr = 'cancel'
        elif ctx.LAYOUT():
            attr = 'layout'
        elif ctx.SIZE():
            attr = 'size'
        else:
            return

        if attr in self._form.attrs_seen:
            self._error(ctx, f"Atributo de formulario '{attr}' declarado más de una vez.")
        self._form.attrs_seen.add(attr)

        if ctx.THEME() and ctx.theme_value():
            val = self._strip_quotes(ctx.theme_value().getText())
            if val not in VALID_THEMES:
                self._error(ctx, f"Tema inválido: '{val}'. Válidos: {sorted(VALID_THEMES)}.")
            self._form.theme = val

        if ctx.LAYOUT() and ctx.layout_value():
            val = self._strip_quotes(ctx.layout_value().getText())
            if val not in VALID_LAYOUTS:
                self._error(ctx, f"Layout inválido: '{val}'. Válidos: {sorted(VALID_LAYOUTS)}.")
            self._form.layout = val

        if ctx.SIZE() and ctx.size_value():
            val = self._strip_quotes(ctx.size_value().getText())
            if val not in VALID_SIZES:
                self._error(ctx, f"Tamaño inválido: '{val}'. Válidos: {sorted(VALID_SIZES)}.")
            self._form.size = val

    def enterSection(self, ctx: FormGenParser.SectionContext):
        name = ctx.identifier().getText()
        if name in self._section_names:
            self._error(ctx, f"Sección '{name}' duplicada en el formulario.")
        self._section_names.add(name)
        self._current_section = SectionInfo(name, ctx.start.line)
        self._field_names_in_section = set()
        if self._form:
            self._form.sections.append(self._current_section)

    def exitSection(self, ctx: FormGenParser.SectionContext):
        if self._current_section and not self._current_section.fields:
            self._warn(ctx, f"La sección '{self._current_section.name}' no contiene ningún campo.")

    def enterField(self, ctx: FormGenParser.FieldContext):
        name = ctx.identifier().getText()
        if name in self._field_names_in_section:
            self._error(ctx, f"Campo '{name}' duplicado en la sección '{self._current_section.name}'.")
        self._field_names_in_section.add(name)
        self._current_field = FieldInfo(name, ctx.start.line)
        if self._current_section:
            self._current_section.fields.append(self._current_field)

    def exitField(self, ctx: FormGenParser.FieldContext):
        f = self._current_field
        if not f:
            return

        if f.field_type is None:
            self._error(ctx, f"El campo '{f.name}' no tiene propiedad 'type'.")
            return

        allowed = VALID_PROPS_BY_TYPE.get(f.field_type, set())

        if f.field_type in REQUIRES_OPTIONS and "options" not in f.props_seen:
            self._error(ctx, f"El campo '{f.name}' es de tipo 'select' y le falta 'options'.")

        if f.field_type in FORBIDS_OPTIONS and "options" in f.props_seen:
            self._error(ctx, f"El campo '{f.name}' es de tipo '{f.field_type}' y no puede tener 'options'.")

        for prop in f.props_seen:
            if prop not in allowed:
                self._error(ctx, f"La propiedad '{prop}' no es válida para el tipo '{f.field_type}' (campo '{f.name}').")

        text_types = {"string", "email", "password", "textarea"}
        if ("min_length" in f.props_seen or "max_length" in f.props_seen) and f.field_type not in text_types:
            self._error(ctx, f"'min_length'/'max_length' solo aplica a tipos de texto (campo '{f.name}', tipo '{f.field_type}').")

        if f.min_length is not None and f.max_length is not None:
            if f.min_length > f.max_length:
                self._error(ctx, f"'min_length' ({f.min_length}) > 'max_length' ({f.max_length}) en el campo '{f.name}'.")

        if f.min_val is not None and f.max_val is not None:
            if f.min_val > f.max_val:
                self._error(ctx, f"'min' ({f.min_val}) > 'max' ({f.max_val}) en el campo '{f.name}'.")

        if f.default_val is not None and f.default_val_kind is not None:
            expected = DEFAULT_VALUE_TYPE.get(f.field_type)
            actual = f.default_val_kind
            ok = (expected == actual) or (expected == "number" and actual in ("integer", "float"))
            if not ok:
                self._error(ctx, f"El valor 'default' del campo '{f.name}' debería ser de tipo '{expected}' pero se encontró '{actual}'.")

        if f.is_hidden and f.is_required:
            self._warn(ctx, f"El campo '{f.name}' es 'hidden' y 'required' al mismo tiempo (los campos ocultos no pueden ser completados por el usuario).")

        if f.is_readonly and f.is_required:
            self._warn(ctx, f"El campo '{f.name}' es 'readonly' y 'required'. Un campo de solo lectura no puede ser modificado por el usuario.")

        if f.min_length == 0:
            self._warn(ctx, f"'min_length: 0' en el campo '{f.name}' no tiene efecto.")

        if f.field_type == "select" and len(f.options) < 2:
            self._warn(ctx, f"El campo 'select' '{f.name}' tiene menos de 2 opciones ({len(f.options)}); considera agregar más.")

    def enterField_prop(self, ctx: FormGenParser.Field_propContext):
        f = self._current_field
        if not f:
            return

        if ctx.TYPE():
            if ctx.field_type():
                ft = ctx.field_type().getText()
                if ft in VALID_FIELD_TYPES:
                    f.field_type = ft
                else:
                    self._error(ctx, f"Tipo de campo desconocido: '{ft}'.")
            return

        prop_map = {
            'LABEL': 'label', 'PLACEHOLDER': 'placeholder',
            'REQUIRED': 'required', 'UNIQUE': 'unique',
            'READONLY': 'readonly', 'FIELD_HIDDEN': 'hidden',
            'DEFAULT': 'default', 'MIN_LENGTH': 'min_length',
            'MAX_LENGTH': 'max_length', 'MIN': 'min',
            'MAX': 'max', 'OPTIONS': 'options', 'ICON': 'icon',
        }

        prop_name = None
        for token_attr, name in prop_map.items():
            if getattr(ctx, token_attr, lambda: None)():
                prop_name = name
                break

        if prop_name is None:
            return

        if prop_name in f.props_seen:
            self._error(ctx, f"Propiedad '{prop_name}' duplicada en el campo '{f.name}'.")
        f.props_seen.add(prop_name)

        if prop_name == 'required':
            f.is_required = True
        elif prop_name == 'hidden':
            f.is_hidden = True
        elif prop_name == 'readonly':
            f.is_readonly = True
        elif prop_name == 'min_length':
            try:
                f.min_length = int(ctx.INTEGER().getText())
            except (AttributeError, ValueError):
                pass
        elif prop_name == 'max_length':
            try:
                f.max_length = int(ctx.INTEGER().getText())
            except (AttributeError, ValueError):
                pass
        elif prop_name == 'min':
            if ctx.number():
                try:
                    f.min_val = float(ctx.number().getText())
                except ValueError:
                    pass
        elif prop_name == 'max':
            if ctx.number():
                try:
                    f.max_val = float(ctx.number().getText())
                except ValueError:
                    pass
        elif prop_name == 'default':
            if ctx.value():
                v = ctx.value()
                if v.STRING():
                    f.default_val = self._strip_quotes(v.STRING().getText())
                    f.default_val_kind = 'string'
                elif v.FLOAT():
                    f.default_val = float(v.FLOAT().getText())
                    f.default_val_kind = 'float'
                elif v.INTEGER():
                    f.default_val = int(v.INTEGER().getText())
                    f.default_val_kind = 'integer'
                elif v.boolean_val():
                    f.default_val = v.boolean_val().getText()
                    f.default_val_kind = 'boolean'
        elif prop_name == 'label':
            if ctx.STRING():
                f.label = self._strip_quotes(ctx.STRING().getText())
        elif prop_name == 'placeholder':
            if ctx.STRING():
                f.placeholder = self._strip_quotes(ctx.STRING().getText())
        elif prop_name == 'options':
            if ctx.option_list():
                strings = ctx.option_list().STRING()
                f.options = [self._strip_quotes(s.getText()) for s in strings]
                seen_opts = set()
                for opt in f.options:
                    if opt in seen_opts:
                        self._warn(ctx, f"Opción duplicada '{opt}' en el campo '{f.name}'.")
                    seen_opts.add(opt)
        elif prop_name == 'icon':
            if ctx.icon_value():
                icon = ctx.icon_value().getText()
                if icon not in VALID_ICONS:
                    self._error(ctx, f"Ícono desconocido: '{icon}' en campo '{f.name}'. Válidos: {sorted(VALID_ICONS)}.")
                else:
                    f.icon = icon

    def enterOn_submit(self, ctx: FormGenParser.On_submitContext):
        self.on_submit = {
            "method": None,
            "url": None,
            "success_msg": None,
            "error_msg": None,
            "success_action": None,
            "success_url": None,
        }

    def enterHttp_action(self, ctx: FormGenParser.Http_actionContext):
        if self.on_submit is None:
            self.on_submit = {}
        if ctx.http_method():
            self.on_submit["method"] = ctx.http_method().getText()
        if ctx.URL_PATH():
            self.on_submit["url"] = ctx.URL_PATH().getText()

    def enterSuccess_clause(self, ctx: FormGenParser.Success_clauseContext):
        if self.on_submit is None:
            self.on_submit = {}
        if ctx.STRING():
            self.on_submit["success_msg"] = self._strip_quotes(ctx.STRING().getText())
        arrow = ctx.arrow_action()
        if arrow and arrow.URL_PATH():
            self.on_submit["success_action"] = "redirect"
            self.on_submit["success_url"] = arrow.URL_PATH().getText()

    def enterError_clause(self, ctx: FormGenParser.Error_clauseContext):
        if self.on_submit is None:
            self.on_submit = {}
        if ctx.STRING():
            self.on_submit["error_msg"] = self._strip_quotes(ctx.STRING().getText())


def analyze(filepath: str) -> dict:
    input_stream = FileStream(filepath, encoding='utf-8')
    lexer = FormGenLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FormGenParser(stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        return {
            'ok': False,
            'errors': [SemanticError(0, f"{parser.getNumberOfSyntaxErrors()} error(es) sintáctico(s). Corrige la sintaxis antes del análisis semántico.")],
            'warnings': [],
            'form': None,
        }

    analyzer = SemanticAnalyzer()
    walker = ParseTreeWalker()
    walker.walk(analyzer, tree)

    return {
        'ok': len(analyzer.errors) == 0,
        'errors': analyzer.errors,
        'warnings': analyzer.warnings,
        'form': analyzer._form,
        'on_submit': analyzer.on_submit,
    }


def print_report(result: dict, filepath: str):
    print("=" * 60)
    print(f"  ANÁLISIS SEMÁNTICO — {os.path.basename(filepath)}")
    print("=" * 60)

    form = result['form']
    if form:
        print(f"\n  Formulario : {form.name}")
        print(f"  Secciones  : {len(form.sections)}")
        print(f"  Campos     : {sum(len(s.fields) for s in form.sections)}")

    print()
    if result['errors']:
        print(f"  Errores semánticos ({len(result['errors'])}):")
        for e in result['errors']:
            print(str(e))
    else:
        print("  ✅ Sin errores semánticos")

    print()
    if result['warnings']:
        print(f"  Advertencias ({len(result['warnings'])}):")
        for w in result['warnings']:
            print(str(w))
    else:
        print("  ✅ Sin advertencias")

    print()
    print(f"  Estado: {'✅ VÁLIDO' if result['ok'] else '❌ INVÁLIDO'}")
    print("=" * 60)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python semantic_analyzer.py <archivo.fg> [<archivo2.fg> ...]")
        sys.exit(1)

    any_error = False
    for path in sys.argv[1:]:
        result = analyze(path)
        print_report(result, path)
        print()
        if not result['ok']:
            any_error = True

    sys.exit(1 if any_error else 0)
