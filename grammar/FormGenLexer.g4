lexer grammar FormGenLexer;

@header {
from antlr4.Token import CommonToken
from antlr4.CommonTokenFactory import CommonTokenFactory
from antlr4 import Token
from collections import deque
}

@lexer::members {
indent_stack = [0]
token_queue = deque()
last_token = None

def nextToken(self):
    if self.token_queue:
        return self.token_queue.popleft()

    token = super().nextToken()

    if token.type == Token.EOF:
        while len(self.indent_stack) > 1:
            self.indent_stack.pop()
            dedent = self._make_token(self.DEDENT, "<DEDENT>")
            self.token_queue.append(dedent)
        self.token_queue.append(token)
        return self.token_queue.popleft()

    self.last_token = token
    return token

def _make_token(self, ttype, text):
    factory = CommonTokenFactory.DEFAULT
    t = factory.create(
        (self, self._input),
        ttype,
        text,
        self.DEFAULT_TOKEN_CHANNEL,
        -1, -1,
        self._tokenStartLine,
        self._tokenStartColumn
    )
    return t

def handle_newline(self):
    indent = 0
    i = 1
    while True:
        c = self._input.LA(i)
        if c == ord(' '):
            indent += 1
            i += 1
        elif c == ord('\t'):
            indent += 4
            i += 1
        else:
            break

    current = self.indent_stack[-1]

    if indent > current:
        self.indent_stack.append(indent)
        self.token_queue.append(self._make_token(self.INDENT, "<INDENT>"))
    elif indent < current:
        while self.indent_stack[-1] > indent:
            self.indent_stack.pop()
            self.token_queue.append(self._make_token(self.DEDENT, "<DEDENT>"))
}

//PALABRAS CLAVE — Estructurales
FORM        : 'form' ;
SECTION     : 'section' ;
FIELD       : 'field' ;
ON_SUBMIT   : 'on_submit' ;

//PALABRAS CLAVE — Propiedades de campo
TYPE        : 'type' ;
LABEL       : 'label' ;
PLACEHOLDER : 'placeholder' ;
REQUIRED    : 'required' ;
UNIQUE      : 'unique' ;
READONLY    : 'readonly' ;
FIELD_HIDDEN : 'hidden' ;
DEFAULT     : 'default' ;
MIN_LENGTH  : 'min_length' ;
MAX_LENGTH  : 'max_length' ;
MIN         : 'min' ;
MAX         : 'max' ;
OPTIONS     : 'options' ;
ICON        : 'icon' ;

//PALABRAS CLAVE — Atributos de formulario
TITLE       : 'title' ;
THEME       : 'theme' ;
LAYOUT      : 'layout' ;
SIZE        : 'size' ;
SUBMIT      : 'submit' ;
CANCEL      : 'cancel' ;

//VALORES — Temas, layouts, tamaños
DARK        : 'dark' ;
LIGHT       : 'light' ;
PRIMARY     : 'primary' ;
MINIMAL     : 'minimal' ;
STACKED     : 'stacked' ;
INLINE      : 'inline' ;
GRID        : 'grid' ;
SM          : 'sm' ;
MD          : 'md' ;
LG          : 'lg' ;

//VALORES — Tipos de campo
T_STRING    : 'string' ;
T_EMAIL     : 'email' ;
T_PASSWORD  : 'password' ;
T_INT       : 'int' ;
T_FLOAT     : 'float' ;
T_DATE      : 'date' ;
T_BOOLEAN   : 'boolean' ;
T_SELECT    : 'select' ;
T_TEXTAREA  : 'textarea' ;

//VALORES — Íconos
ICON_PERSON   : 'person' ;
ICON_LOCK     : 'lock' ;
ICON_ENVELOPE : 'envelope' ;
ICON_PHONE    : 'phone' ;
ICON_CALENDAR : 'calendar' ;
ICON_SEARCH   : 'search' ;
ICON_EYE      : 'eye' ;

//ON_SUBMIT — Métodos HTTP y acciones
POST        : 'POST' ;
GET         : 'GET' ;
SUCCESS     : 'success' ;
ERROR       : 'error' ;
REDIRECT    : 'redirect' ;

//BOOLEANOS
TRUE        : 'true' ;
FALSE       : 'false' ;

//OPERADORES Y PUNTUACIÓN
EQUALS      : '=' ;
COLON       : ':' ;
COMMA       : ',' ;
LBRACKET    : '[' ;
RBRACKET    : ']' ;
ARROW : '\u2192' ;

//LITERALES
STRING      : '"' ( ~["\\\r\n] | '\\' . )* '"' ;
INTEGER     : [0-9]+ ;
FLOAT       : [0-9]+ '.' [0-9]+ ;
URL_PATH    : '/' [a-zA-Z0-9_\-/]* ;

//IDENTIFICADORES
IDENTIFIER  : [a-zA-Z_] [a-zA-Z0-9_]* ;

//  TOKENS DE INDENTACIÓN
INDENT  : '<INDENT>'  ;
DEDENT  : '<DEDENT>'  ;

//WHITESPACE, NEWLINES Y COMENTARIOS
NEWLINE     : ( '\r'? '\n' ) { self.handle_newline() } ;
WS          : [ \t]+ -> skip ;
COMMENT     : '#' ~[\r\n]* -> skip ;
