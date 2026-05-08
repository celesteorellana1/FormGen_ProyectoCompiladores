parser grammar FormGenParser;

options {
    tokenVocab = FormGenLexer;
}

//  REGLA RAÍZ

program
    : form_def EOF
    ;

//  FORMULARIO

form_def
    : FORM identifier form_attr+ NEWLINE
      INDENT
          section+
          on_submit?
      DEDENT
    ;

form_attr
    : TITLE  EQUALS STRING
    | THEME  EQUALS theme_value
    | SUBMIT EQUALS STRING
    | CANCEL EQUALS STRING
    | LAYOUT EQUALS layout_value
    | SIZE   EQUALS size_value
    ;

theme_value
    : DARK | LIGHT | PRIMARY | MINIMAL | STRING
    ;

layout_value
    : STACKED | INLINE | GRID | STRING
    ;

size_value
    : SM | MD | LG | STRING
    ;

//  SECCIÓN

section
    : SECTION identifier NEWLINE
      INDENT
          field+
      DEDENT
    ;

//  CAMPO

field
    : FIELD identifier NEWLINE
      INDENT
          field_prop+
      DEDENT
    ;

field_prop
    : TYPE        COLON field_type  NEWLINE
    | LABEL       COLON STRING      NEWLINE
    | PLACEHOLDER COLON STRING      NEWLINE
    | REQUIRED                      NEWLINE
    | UNIQUE      COLON boolean_val NEWLINE
    | READONLY                      NEWLINE
    | FIELD_HIDDEN                  NEWLINE
    | DEFAULT     COLON value       NEWLINE
    | MIN_LENGTH  COLON INTEGER     NEWLINE
    | MAX_LENGTH  COLON INTEGER     NEWLINE
    | MIN         COLON number      NEWLINE
    | MAX         COLON number      NEWLINE
    | OPTIONS     COLON option_list NEWLINE
    | ICON        COLON icon_value  NEWLINE
    ;

//  TIPOS, ÍCONOS Y VALORES

field_type
    : T_STRING | T_EMAIL    | T_PASSWORD
    | T_INT    | T_FLOAT    | T_DATE
    | T_BOOLEAN| T_SELECT   | T_TEXTAREA
    ;

icon_value
    : ICON_PERSON | ICON_LOCK     | ICON_ENVELOPE
    | ICON_PHONE  | ICON_CALENDAR | ICON_SEARCH
    | ICON_EYE
    ;

option_list
    : LBRACKET STRING (COMMA STRING)* RBRACKET
    ;

value
    : STRING | INTEGER | FLOAT | boolean_val
    ;

number
    : INTEGER | FLOAT
    ;

boolean_val
    : TRUE | FALSE
    ;

identifier
    : IDENTIFIER
    | T_STRING | T_EMAIL    | T_PASSWORD
    | T_INT    | T_FLOAT    | T_DATE
    | T_BOOLEAN| T_SELECT   | T_TEXTAREA
    ;

//  ON_SUBMIT

on_submit
    : ON_SUBMIT NEWLINE
      INDENT
          http_action
          success_clause
          error_clause
      DEDENT
    ;

http_action
    : http_method URL_PATH NEWLINE
    ;

http_method
    : POST | GET
    ;

success_clause
    : SUCCESS COLON STRING arrow_action? NEWLINE
    ;

error_clause
    : ERROR COLON STRING NEWLINE?
    ;

arrow_action
    : ARROW REDIRECT URL_PATH
    ;