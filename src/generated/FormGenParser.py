# Generated from grammar/FormGenParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,73,233,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,1,0,1,1,1,1,1,1,4,1,51,8,1,11,1,12,1,52,1,
        1,1,1,1,1,4,1,58,8,1,11,1,12,1,59,1,1,3,1,63,8,1,1,1,1,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,85,8,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,4,6,98,8,
        6,11,6,12,6,99,1,6,1,6,1,7,1,7,1,7,1,7,1,7,4,7,109,8,7,11,7,12,7,
        110,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,172,8,8,1,9,
        1,9,1,10,1,10,1,11,1,11,1,11,1,11,5,11,182,8,11,10,11,12,11,185,
        9,11,1,11,1,11,1,12,1,12,1,12,1,12,3,12,193,8,12,1,13,1,13,1,14,
        1,14,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,
        1,17,1,17,1,18,1,18,1,19,1,19,1,19,1,19,3,19,219,8,19,1,19,1,19,
        1,20,1,20,1,20,1,20,3,20,227,8,20,1,21,1,21,1,21,1,21,1,21,0,0,22,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,0,9,
        2,0,25,28,64,64,2,0,29,31,64,64,2,0,32,34,64,64,1,0,35,43,1,0,44,
        50,1,0,65,66,1,0,56,57,2,0,35,43,68,68,1,0,51,52,239,0,44,1,0,0,
        0,2,47,1,0,0,0,4,84,1,0,0,0,6,86,1,0,0,0,8,88,1,0,0,0,10,90,1,0,
        0,0,12,92,1,0,0,0,14,103,1,0,0,0,16,171,1,0,0,0,18,173,1,0,0,0,20,
        175,1,0,0,0,22,177,1,0,0,0,24,192,1,0,0,0,26,194,1,0,0,0,28,196,
        1,0,0,0,30,198,1,0,0,0,32,200,1,0,0,0,34,208,1,0,0,0,36,212,1,0,
        0,0,38,214,1,0,0,0,40,222,1,0,0,0,42,228,1,0,0,0,44,45,3,2,1,0,45,
        46,5,0,0,1,46,1,1,0,0,0,47,48,5,1,0,0,48,50,3,30,15,0,49,51,3,4,
        2,0,50,49,1,0,0,0,51,52,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,54,
        1,0,0,0,54,55,5,71,0,0,55,57,5,69,0,0,56,58,3,12,6,0,57,56,1,0,0,
        0,58,59,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,63,
        3,32,16,0,62,61,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,65,5,70,0,
        0,65,3,1,0,0,0,66,67,5,19,0,0,67,68,5,58,0,0,68,85,5,64,0,0,69,70,
        5,20,0,0,70,71,5,58,0,0,71,85,3,6,3,0,72,73,5,23,0,0,73,74,5,58,
        0,0,74,85,5,64,0,0,75,76,5,24,0,0,76,77,5,58,0,0,77,85,5,64,0,0,
        78,79,5,21,0,0,79,80,5,58,0,0,80,85,3,8,4,0,81,82,5,22,0,0,82,83,
        5,58,0,0,83,85,3,10,5,0,84,66,1,0,0,0,84,69,1,0,0,0,84,72,1,0,0,
        0,84,75,1,0,0,0,84,78,1,0,0,0,84,81,1,0,0,0,85,5,1,0,0,0,86,87,7,
        0,0,0,87,7,1,0,0,0,88,89,7,1,0,0,89,9,1,0,0,0,90,91,7,2,0,0,91,11,
        1,0,0,0,92,93,5,2,0,0,93,94,3,30,15,0,94,95,5,71,0,0,95,97,5,69,
        0,0,96,98,3,14,7,0,97,96,1,0,0,0,98,99,1,0,0,0,99,97,1,0,0,0,99,
        100,1,0,0,0,100,101,1,0,0,0,101,102,5,70,0,0,102,13,1,0,0,0,103,
        104,5,3,0,0,104,105,3,30,15,0,105,106,5,71,0,0,106,108,5,69,0,0,
        107,109,3,16,8,0,108,107,1,0,0,0,109,110,1,0,0,0,110,108,1,0,0,0,
        110,111,1,0,0,0,111,112,1,0,0,0,112,113,5,70,0,0,113,15,1,0,0,0,
        114,115,5,5,0,0,115,116,5,59,0,0,116,117,3,18,9,0,117,118,5,71,0,
        0,118,172,1,0,0,0,119,120,5,6,0,0,120,121,5,59,0,0,121,122,5,64,
        0,0,122,172,5,71,0,0,123,124,5,7,0,0,124,125,5,59,0,0,125,126,5,
        64,0,0,126,172,5,71,0,0,127,128,5,8,0,0,128,172,5,71,0,0,129,130,
        5,9,0,0,130,131,5,59,0,0,131,132,3,28,14,0,132,133,5,71,0,0,133,
        172,1,0,0,0,134,135,5,10,0,0,135,172,5,71,0,0,136,137,5,11,0,0,137,
        172,5,71,0,0,138,139,5,12,0,0,139,140,5,59,0,0,140,141,3,24,12,0,
        141,142,5,71,0,0,142,172,1,0,0,0,143,144,5,13,0,0,144,145,5,59,0,
        0,145,146,5,65,0,0,146,172,5,71,0,0,147,148,5,14,0,0,148,149,5,59,
        0,0,149,150,5,65,0,0,150,172,5,71,0,0,151,152,5,15,0,0,152,153,5,
        59,0,0,153,154,3,26,13,0,154,155,5,71,0,0,155,172,1,0,0,0,156,157,
        5,16,0,0,157,158,5,59,0,0,158,159,3,26,13,0,159,160,5,71,0,0,160,
        172,1,0,0,0,161,162,5,17,0,0,162,163,5,59,0,0,163,164,3,22,11,0,
        164,165,5,71,0,0,165,172,1,0,0,0,166,167,5,18,0,0,167,168,5,59,0,
        0,168,169,3,20,10,0,169,170,5,71,0,0,170,172,1,0,0,0,171,114,1,0,
        0,0,171,119,1,0,0,0,171,123,1,0,0,0,171,127,1,0,0,0,171,129,1,0,
        0,0,171,134,1,0,0,0,171,136,1,0,0,0,171,138,1,0,0,0,171,143,1,0,
        0,0,171,147,1,0,0,0,171,151,1,0,0,0,171,156,1,0,0,0,171,161,1,0,
        0,0,171,166,1,0,0,0,172,17,1,0,0,0,173,174,7,3,0,0,174,19,1,0,0,
        0,175,176,7,4,0,0,176,21,1,0,0,0,177,178,5,61,0,0,178,183,5,64,0,
        0,179,180,5,60,0,0,180,182,5,64,0,0,181,179,1,0,0,0,182,185,1,0,
        0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,186,1,0,0,0,185,183,1,0,
        0,0,186,187,5,62,0,0,187,23,1,0,0,0,188,193,5,64,0,0,189,193,5,65,
        0,0,190,193,5,66,0,0,191,193,3,28,14,0,192,188,1,0,0,0,192,189,1,
        0,0,0,192,190,1,0,0,0,192,191,1,0,0,0,193,25,1,0,0,0,194,195,7,5,
        0,0,195,27,1,0,0,0,196,197,7,6,0,0,197,29,1,0,0,0,198,199,7,7,0,
        0,199,31,1,0,0,0,200,201,5,4,0,0,201,202,5,71,0,0,202,203,5,69,0,
        0,203,204,3,34,17,0,204,205,3,38,19,0,205,206,3,40,20,0,206,207,
        5,70,0,0,207,33,1,0,0,0,208,209,3,36,18,0,209,210,5,67,0,0,210,211,
        5,71,0,0,211,35,1,0,0,0,212,213,7,8,0,0,213,37,1,0,0,0,214,215,5,
        53,0,0,215,216,5,59,0,0,216,218,5,64,0,0,217,219,3,42,21,0,218,217,
        1,0,0,0,218,219,1,0,0,0,219,220,1,0,0,0,220,221,5,71,0,0,221,39,
        1,0,0,0,222,223,5,54,0,0,223,224,5,59,0,0,224,226,5,64,0,0,225,227,
        5,71,0,0,226,225,1,0,0,0,226,227,1,0,0,0,227,41,1,0,0,0,228,229,
        5,63,0,0,229,230,5,55,0,0,230,231,5,67,0,0,231,43,1,0,0,0,11,52,
        59,62,84,99,110,171,183,192,218,226
    ]

class FormGenParser ( Parser ):

    grammarFileName = "FormGenParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'form'", "'section'", "'field'", "'on_submit'", 
                     "'type'", "'label'", "'placeholder'", "'required'", 
                     "'unique'", "'readonly'", "'hidden'", "'default'", 
                     "'min_length'", "'max_length'", "'min'", "'max'", "'options'", 
                     "'icon'", "'title'", "'theme'", "'layout'", "'size'", 
                     "'submit'", "'cancel'", "'dark'", "'light'", "'primary'", 
                     "'minimal'", "'stacked'", "'inline'", "'grid'", "'sm'", 
                     "'md'", "'lg'", "'string'", "'email'", "'password'", 
                     "'int'", "'float'", "'date'", "'boolean'", "'select'", 
                     "'textarea'", "'person'", "'lock'", "'envelope'", "'phone'", 
                     "'calendar'", "'search'", "'eye'", "'POST'", "'GET'", 
                     "'success'", "'error'", "'redirect'", "'true'", "'false'", 
                     "'='", "':'", "','", "'['", "']'", "'\\u2192'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'<INDENT>'", "'<DEDENT>'" ]

    symbolicNames = [ "<INVALID>", "FORM", "SECTION", "FIELD", "ON_SUBMIT", 
                      "TYPE", "LABEL", "PLACEHOLDER", "REQUIRED", "UNIQUE", 
                      "READONLY", "FIELD_HIDDEN", "DEFAULT", "MIN_LENGTH", 
                      "MAX_LENGTH", "MIN", "MAX", "OPTIONS", "ICON", "TITLE", 
                      "THEME", "LAYOUT", "SIZE", "SUBMIT", "CANCEL", "DARK", 
                      "LIGHT", "PRIMARY", "MINIMAL", "STACKED", "INLINE", 
                      "GRID", "SM", "MD", "LG", "T_STRING", "T_EMAIL", "T_PASSWORD", 
                      "T_INT", "T_FLOAT", "T_DATE", "T_BOOLEAN", "T_SELECT", 
                      "T_TEXTAREA", "ICON_PERSON", "ICON_LOCK", "ICON_ENVELOPE", 
                      "ICON_PHONE", "ICON_CALENDAR", "ICON_SEARCH", "ICON_EYE", 
                      "POST", "GET", "SUCCESS", "ERROR", "REDIRECT", "TRUE", 
                      "FALSE", "EQUALS", "COLON", "COMMA", "LBRACKET", "RBRACKET", 
                      "ARROW", "STRING", "INTEGER", "FLOAT", "URL_PATH", 
                      "IDENTIFIER", "INDENT", "DEDENT", "NEWLINE", "WS", 
                      "COMMENT" ]

    RULE_program = 0
    RULE_form_def = 1
    RULE_form_attr = 2
    RULE_theme_value = 3
    RULE_layout_value = 4
    RULE_size_value = 5
    RULE_section = 6
    RULE_field = 7
    RULE_field_prop = 8
    RULE_field_type = 9
    RULE_icon_value = 10
    RULE_option_list = 11
    RULE_value = 12
    RULE_number = 13
    RULE_boolean_val = 14
    RULE_identifier = 15
    RULE_on_submit = 16
    RULE_http_action = 17
    RULE_http_method = 18
    RULE_success_clause = 19
    RULE_error_clause = 20
    RULE_arrow_action = 21

    ruleNames =  [ "program", "form_def", "form_attr", "theme_value", "layout_value", 
                   "size_value", "section", "field", "field_prop", "field_type", 
                   "icon_value", "option_list", "value", "number", "boolean_val", 
                   "identifier", "on_submit", "http_action", "http_method", 
                   "success_clause", "error_clause", "arrow_action" ]

    EOF = Token.EOF
    FORM=1
    SECTION=2
    FIELD=3
    ON_SUBMIT=4
    TYPE=5
    LABEL=6
    PLACEHOLDER=7
    REQUIRED=8
    UNIQUE=9
    READONLY=10
    FIELD_HIDDEN=11
    DEFAULT=12
    MIN_LENGTH=13
    MAX_LENGTH=14
    MIN=15
    MAX=16
    OPTIONS=17
    ICON=18
    TITLE=19
    THEME=20
    LAYOUT=21
    SIZE=22
    SUBMIT=23
    CANCEL=24
    DARK=25
    LIGHT=26
    PRIMARY=27
    MINIMAL=28
    STACKED=29
    INLINE=30
    GRID=31
    SM=32
    MD=33
    LG=34
    T_STRING=35
    T_EMAIL=36
    T_PASSWORD=37
    T_INT=38
    T_FLOAT=39
    T_DATE=40
    T_BOOLEAN=41
    T_SELECT=42
    T_TEXTAREA=43
    ICON_PERSON=44
    ICON_LOCK=45
    ICON_ENVELOPE=46
    ICON_PHONE=47
    ICON_CALENDAR=48
    ICON_SEARCH=49
    ICON_EYE=50
    POST=51
    GET=52
    SUCCESS=53
    ERROR=54
    REDIRECT=55
    TRUE=56
    FALSE=57
    EQUALS=58
    COLON=59
    COMMA=60
    LBRACKET=61
    RBRACKET=62
    ARROW=63
    STRING=64
    INTEGER=65
    FLOAT=66
    URL_PATH=67
    IDENTIFIER=68
    INDENT=69
    DEDENT=70
    NEWLINE=71
    WS=72
    COMMENT=73

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def form_def(self):
            return self.getTypedRuleContext(FormGenParser.Form_defContext,0)


        def EOF(self):
            return self.getToken(FormGenParser.EOF, 0)

        def getRuleIndex(self):
            return FormGenParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = FormGenParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.form_def()
            self.state = 45
            self.match(FormGenParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Form_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FORM(self):
            return self.getToken(FormGenParser.FORM, 0)

        def identifier(self):
            return self.getTypedRuleContext(FormGenParser.IdentifierContext,0)


        def NEWLINE(self):
            return self.getToken(FormGenParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(FormGenParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(FormGenParser.DEDENT, 0)

        def form_attr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormGenParser.Form_attrContext)
            else:
                return self.getTypedRuleContext(FormGenParser.Form_attrContext,i)


        def section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormGenParser.SectionContext)
            else:
                return self.getTypedRuleContext(FormGenParser.SectionContext,i)


        def on_submit(self):
            return self.getTypedRuleContext(FormGenParser.On_submitContext,0)


        def getRuleIndex(self):
            return FormGenParser.RULE_form_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForm_def" ):
                listener.enterForm_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForm_def" ):
                listener.exitForm_def(self)




    def form_def(self):

        localctx = FormGenParser.Form_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_form_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(FormGenParser.FORM)
            self.state = 48
            self.identifier()
            self.state = 50 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 49
                self.form_attr()
                self.state = 52 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0)):
                    break

            self.state = 54
            self.match(FormGenParser.NEWLINE)
            self.state = 55
            self.match(FormGenParser.INDENT)
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 56
                self.section()
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 61
                self.on_submit()


            self.state = 64
            self.match(FormGenParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Form_attrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TITLE(self):
            return self.getToken(FormGenParser.TITLE, 0)

        def EQUALS(self):
            return self.getToken(FormGenParser.EQUALS, 0)

        def STRING(self):
            return self.getToken(FormGenParser.STRING, 0)

        def THEME(self):
            return self.getToken(FormGenParser.THEME, 0)

        def theme_value(self):
            return self.getTypedRuleContext(FormGenParser.Theme_valueContext,0)


        def SUBMIT(self):
            return self.getToken(FormGenParser.SUBMIT, 0)

        def CANCEL(self):
            return self.getToken(FormGenParser.CANCEL, 0)

        def LAYOUT(self):
            return self.getToken(FormGenParser.LAYOUT, 0)

        def layout_value(self):
            return self.getTypedRuleContext(FormGenParser.Layout_valueContext,0)


        def SIZE(self):
            return self.getToken(FormGenParser.SIZE, 0)

        def size_value(self):
            return self.getTypedRuleContext(FormGenParser.Size_valueContext,0)


        def getRuleIndex(self):
            return FormGenParser.RULE_form_attr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForm_attr" ):
                listener.enterForm_attr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForm_attr" ):
                listener.exitForm_attr(self)




    def form_attr(self):

        localctx = FormGenParser.Form_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_form_attr)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(FormGenParser.TITLE)
                self.state = 67
                self.match(FormGenParser.EQUALS)
                self.state = 68
                self.match(FormGenParser.STRING)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(FormGenParser.THEME)
                self.state = 70
                self.match(FormGenParser.EQUALS)
                self.state = 71
                self.theme_value()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.match(FormGenParser.SUBMIT)
                self.state = 73
                self.match(FormGenParser.EQUALS)
                self.state = 74
                self.match(FormGenParser.STRING)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.match(FormGenParser.CANCEL)
                self.state = 76
                self.match(FormGenParser.EQUALS)
                self.state = 77
                self.match(FormGenParser.STRING)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.match(FormGenParser.LAYOUT)
                self.state = 79
                self.match(FormGenParser.EQUALS)
                self.state = 80
                self.layout_value()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 6)
                self.state = 81
                self.match(FormGenParser.SIZE)
                self.state = 82
                self.match(FormGenParser.EQUALS)
                self.state = 83
                self.size_value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Theme_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DARK(self):
            return self.getToken(FormGenParser.DARK, 0)

        def LIGHT(self):
            return self.getToken(FormGenParser.LIGHT, 0)

        def PRIMARY(self):
            return self.getToken(FormGenParser.PRIMARY, 0)

        def MINIMAL(self):
            return self.getToken(FormGenParser.MINIMAL, 0)

        def STRING(self):
            return self.getToken(FormGenParser.STRING, 0)

        def getRuleIndex(self):
            return FormGenParser.RULE_theme_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTheme_value" ):
                listener.enterTheme_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTheme_value" ):
                listener.exitTheme_value(self)




    def theme_value(self):

        localctx = FormGenParser.Theme_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_theme_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not(((((_la - 25)) & ~0x3f) == 0 and ((1 << (_la - 25)) & 549755813903) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Layout_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STACKED(self):
            return self.getToken(FormGenParser.STACKED, 0)

        def INLINE(self):
            return self.getToken(FormGenParser.INLINE, 0)

        def GRID(self):
            return self.getToken(FormGenParser.GRID, 0)

        def STRING(self):
            return self.getToken(FormGenParser.STRING, 0)

        def getRuleIndex(self):
            return FormGenParser.RULE_layout_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLayout_value" ):
                listener.enterLayout_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLayout_value" ):
                listener.exitLayout_value(self)




    def layout_value(self):

        localctx = FormGenParser.Layout_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_layout_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not(((((_la - 29)) & ~0x3f) == 0 and ((1 << (_la - 29)) & 34359738375) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Size_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SM(self):
            return self.getToken(FormGenParser.SM, 0)

        def MD(self):
            return self.getToken(FormGenParser.MD, 0)

        def LG(self):
            return self.getToken(FormGenParser.LG, 0)

        def STRING(self):
            return self.getToken(FormGenParser.STRING, 0)

        def getRuleIndex(self):
            return FormGenParser.RULE_size_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSize_value" ):
                listener.enterSize_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSize_value" ):
                listener.exitSize_value(self)




    def size_value(self):

        localctx = FormGenParser.Size_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_size_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not(((((_la - 32)) & ~0x3f) == 0 and ((1 << (_la - 32)) & 4294967303) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SECTION(self):
            return self.getToken(FormGenParser.SECTION, 0)

        def identifier(self):
            return self.getTypedRuleContext(FormGenParser.IdentifierContext,0)


        def NEWLINE(self):
            return self.getToken(FormGenParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(FormGenParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(FormGenParser.DEDENT, 0)

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormGenParser.FieldContext)
            else:
                return self.getTypedRuleContext(FormGenParser.FieldContext,i)


        def getRuleIndex(self):
            return FormGenParser.RULE_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection" ):
                listener.enterSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection" ):
                listener.exitSection(self)




    def section(self):

        localctx = FormGenParser.SectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(FormGenParser.SECTION)
            self.state = 93
            self.identifier()
            self.state = 94
            self.match(FormGenParser.NEWLINE)
            self.state = 95
            self.match(FormGenParser.INDENT)
            self.state = 97 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 96
                self.field()
                self.state = 99 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

            self.state = 101
            self.match(FormGenParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FIELD(self):
            return self.getToken(FormGenParser.FIELD, 0)

        def identifier(self):
            return self.getTypedRuleContext(FormGenParser.IdentifierContext,0)


        def NEWLINE(self):
            return self.getToken(FormGenParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(FormGenParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(FormGenParser.DEDENT, 0)

        def field_prop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormGenParser.Field_propContext)
            else:
                return self.getTypedRuleContext(FormGenParser.Field_propContext,i)


        def getRuleIndex(self):
            return FormGenParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField" ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField" ):
                listener.exitField(self)




    def field(self):

        localctx = FormGenParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(FormGenParser.FIELD)
            self.state = 104
            self.identifier()
            self.state = 105
            self.match(FormGenParser.NEWLINE)
            self.state = 106
            self.match(FormGenParser.INDENT)
            self.state = 108 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 107
                self.field_prop()
                self.state = 110 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 524256) != 0)):
                    break

            self.state = 112
            self.match(FormGenParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_propContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(FormGenParser.TYPE, 0)

        def COLON(self):
            return self.getToken(FormGenParser.COLON, 0)

        def field_type(self):
            return self.getTypedRuleContext(FormGenParser.Field_typeContext,0)


        def NEWLINE(self):
            return self.getToken(FormGenParser.NEWLINE, 0)

        def LABEL(self):
            return self.getToken(FormGenParser.LABEL, 0)

        def STRING(self):
            return self.getToken(FormGenParser.STRING, 0)

        def PLACEHOLDER(self):
            return self.getToken(FormGenParser.PLACEHOLDER, 0)

        def REQUIRED(self):
            return self.getToken(FormGenParser.REQUIRED, 0)

        def UNIQUE(self):
            return self.getToken(FormGenParser.UNIQUE, 0)

        def boolean_val(self):
            return self.getTypedRuleContext(FormGenParser.Boolean_valContext,0)


        def READONLY(self):
            return self.getToken(FormGenParser.READONLY, 0)

        def FIELD_HIDDEN(self):
            return self.getToken(FormGenParser.FIELD_HIDDEN, 0)

        def DEFAULT(self):
            return self.getToken(FormGenParser.DEFAULT, 0)

        def value(self):
            return self.getTypedRuleContext(FormGenParser.ValueContext,0)


        def MIN_LENGTH(self):
            return self.getToken(FormGenParser.MIN_LENGTH, 0)

        def INTEGER(self):
            return self.getToken(FormGenParser.INTEGER, 0)

        def MAX_LENGTH(self):
            return self.getToken(FormGenParser.MAX_LENGTH, 0)

        def MIN(self):
            return self.getToken(FormGenParser.MIN, 0)

        def number(self):
            return self.getTypedRuleContext(FormGenParser.NumberContext,0)


        def MAX(self):
            return self.getToken(FormGenParser.MAX, 0)

        def OPTIONS(self):
            return self.getToken(FormGenParser.OPTIONS, 0)

        def option_list(self):
            return self.getTypedRuleContext(FormGenParser.Option_listContext,0)


        def ICON(self):
            return self.getToken(FormGenParser.ICON, 0)

        def icon_value(self):
            return self.getTypedRuleContext(FormGenParser.Icon_valueContext,0)


        def getRuleIndex(self):
            return FormGenParser.RULE_field_prop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_prop" ):
                listener.enterField_prop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_prop" ):
                listener.exitField_prop(self)




    def field_prop(self):

        localctx = FormGenParser.Field_propContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_field_prop)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.match(FormGenParser.TYPE)
                self.state = 115
                self.match(FormGenParser.COLON)
                self.state = 116
                self.field_type()
                self.state = 117
                self.match(FormGenParser.NEWLINE)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(FormGenParser.LABEL)
                self.state = 120
                self.match(FormGenParser.COLON)
                self.state = 121
                self.match(FormGenParser.STRING)
                self.state = 122
                self.match(FormGenParser.NEWLINE)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                self.match(FormGenParser.PLACEHOLDER)
                self.state = 124
                self.match(FormGenParser.COLON)
                self.state = 125
                self.match(FormGenParser.STRING)
                self.state = 126
                self.match(FormGenParser.NEWLINE)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.match(FormGenParser.REQUIRED)
                self.state = 128
                self.match(FormGenParser.NEWLINE)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 129
                self.match(FormGenParser.UNIQUE)
                self.state = 130
                self.match(FormGenParser.COLON)
                self.state = 131
                self.boolean_val()
                self.state = 132
                self.match(FormGenParser.NEWLINE)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 6)
                self.state = 134
                self.match(FormGenParser.READONLY)
                self.state = 135
                self.match(FormGenParser.NEWLINE)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 7)
                self.state = 136
                self.match(FormGenParser.FIELD_HIDDEN)
                self.state = 137
                self.match(FormGenParser.NEWLINE)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 8)
                self.state = 138
                self.match(FormGenParser.DEFAULT)
                self.state = 139
                self.match(FormGenParser.COLON)
                self.state = 140
                self.value()
                self.state = 141
                self.match(FormGenParser.NEWLINE)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 9)
                self.state = 143
                self.match(FormGenParser.MIN_LENGTH)
                self.state = 144
                self.match(FormGenParser.COLON)
                self.state = 145
                self.match(FormGenParser.INTEGER)
                self.state = 146
                self.match(FormGenParser.NEWLINE)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 10)
                self.state = 147
                self.match(FormGenParser.MAX_LENGTH)
                self.state = 148
                self.match(FormGenParser.COLON)
                self.state = 149
                self.match(FormGenParser.INTEGER)
                self.state = 150
                self.match(FormGenParser.NEWLINE)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 11)
                self.state = 151
                self.match(FormGenParser.MIN)
                self.state = 152
                self.match(FormGenParser.COLON)
                self.state = 153
                self.number()
                self.state = 154
                self.match(FormGenParser.NEWLINE)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 12)
                self.state = 156
                self.match(FormGenParser.MAX)
                self.state = 157
                self.match(FormGenParser.COLON)
                self.state = 158
                self.number()
                self.state = 159
                self.match(FormGenParser.NEWLINE)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 13)
                self.state = 161
                self.match(FormGenParser.OPTIONS)
                self.state = 162
                self.match(FormGenParser.COLON)
                self.state = 163
                self.option_list()
                self.state = 164
                self.match(FormGenParser.NEWLINE)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 14)
                self.state = 166
                self.match(FormGenParser.ICON)
                self.state = 167
                self.match(FormGenParser.COLON)
                self.state = 168
                self.icon_value()
                self.state = 169
                self.match(FormGenParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def T_STRING(self):
            return self.getToken(FormGenParser.T_STRING, 0)

        def T_EMAIL(self):
            return self.getToken(FormGenParser.T_EMAIL, 0)

        def T_PASSWORD(self):
            return self.getToken(FormGenParser.T_PASSWORD, 0)

        def T_INT(self):
            return self.getToken(FormGenParser.T_INT, 0)

        def T_FLOAT(self):
            return self.getToken(FormGenParser.T_FLOAT, 0)

        def T_DATE(self):
            return self.getToken(FormGenParser.T_DATE, 0)

        def T_BOOLEAN(self):
            return self.getToken(FormGenParser.T_BOOLEAN, 0)

        def T_SELECT(self):
            return self.getToken(FormGenParser.T_SELECT, 0)

        def T_TEXTAREA(self):
            return self.getToken(FormGenParser.T_TEXTAREA, 0)

        def getRuleIndex(self):
            return FormGenParser.RULE_field_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_type" ):
                listener.enterField_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_type" ):
                listener.exitField_type(self)




    def field_type(self):

        localctx = FormGenParser.Field_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_field_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17557826306048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Icon_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ICON_PERSON(self):
            return self.getToken(FormGenParser.ICON_PERSON, 0)

        def ICON_LOCK(self):
            return self.getToken(FormGenParser.ICON_LOCK, 0)

        def ICON_ENVELOPE(self):
            return self.getToken(FormGenParser.ICON_ENVELOPE, 0)

        def ICON_PHONE(self):
            return self.getToken(FormGenParser.ICON_PHONE, 0)

        def ICON_CALENDAR(self):
            return self.getToken(FormGenParser.ICON_CALENDAR, 0)

        def ICON_SEARCH(self):
            return self.getToken(FormGenParser.ICON_SEARCH, 0)

        def ICON_EYE(self):
            return self.getToken(FormGenParser.ICON_EYE, 0)

        def getRuleIndex(self):
            return FormGenParser.RULE_icon_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIcon_value" ):
                listener.enterIcon_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIcon_value" ):
                listener.exitIcon_value(self)




    def icon_value(self):

        localctx = FormGenParser.Icon_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_icon_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2234207627640832) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Option_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(FormGenParser.LBRACKET, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(FormGenParser.STRING)
            else:
                return self.getToken(FormGenParser.STRING, i)

        def RBRACKET(self):
            return self.getToken(FormGenParser.RBRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(FormGenParser.COMMA)
            else:
                return self.getToken(FormGenParser.COMMA, i)

        def getRuleIndex(self):
            return FormGenParser.RULE_option_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOption_list" ):
                listener.enterOption_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOption_list" ):
                listener.exitOption_list(self)




    def option_list(self):

        localctx = FormGenParser.Option_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_option_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(FormGenParser.LBRACKET)
            self.state = 178
            self.match(FormGenParser.STRING)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==60:
                self.state = 179
                self.match(FormGenParser.COMMA)
                self.state = 180
                self.match(FormGenParser.STRING)
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 186
            self.match(FormGenParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(FormGenParser.STRING, 0)

        def INTEGER(self):
            return self.getToken(FormGenParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(FormGenParser.FLOAT, 0)

        def boolean_val(self):
            return self.getTypedRuleContext(FormGenParser.Boolean_valContext,0)


        def getRuleIndex(self):
            return FormGenParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = FormGenParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_value)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(FormGenParser.STRING)
                pass
            elif token in [65]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(FormGenParser.INTEGER)
                pass
            elif token in [66]:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.match(FormGenParser.FLOAT)
                pass
            elif token in [56, 57]:
                self.enterOuterAlt(localctx, 4)
                self.state = 191
                self.boolean_val()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(FormGenParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(FormGenParser.FLOAT, 0)

        def getRuleIndex(self):
            return FormGenParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = FormGenParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            _la = self._input.LA(1)
            if not(_la==65 or _la==66):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(FormGenParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(FormGenParser.FALSE, 0)

        def getRuleIndex(self):
            return FormGenParser.RULE_boolean_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_val" ):
                listener.enterBoolean_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_val" ):
                listener.exitBoolean_val(self)




    def boolean_val(self):

        localctx = FormGenParser.Boolean_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_boolean_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            _la = self._input.LA(1)
            if not(_la==56 or _la==57):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(FormGenParser.IDENTIFIER, 0)

        def T_STRING(self):
            return self.getToken(FormGenParser.T_STRING, 0)

        def T_EMAIL(self):
            return self.getToken(FormGenParser.T_EMAIL, 0)

        def T_PASSWORD(self):
            return self.getToken(FormGenParser.T_PASSWORD, 0)

        def T_INT(self):
            return self.getToken(FormGenParser.T_INT, 0)

        def T_FLOAT(self):
            return self.getToken(FormGenParser.T_FLOAT, 0)

        def T_DATE(self):
            return self.getToken(FormGenParser.T_DATE, 0)

        def T_BOOLEAN(self):
            return self.getToken(FormGenParser.T_BOOLEAN, 0)

        def T_SELECT(self):
            return self.getToken(FormGenParser.T_SELECT, 0)

        def T_TEXTAREA(self):
            return self.getToken(FormGenParser.T_TEXTAREA, 0)

        def getRuleIndex(self):
            return FormGenParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = FormGenParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            _la = self._input.LA(1)
            if not(((((_la - 35)) & ~0x3f) == 0 and ((1 << (_la - 35)) & 8589935103) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class On_submitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON_SUBMIT(self):
            return self.getToken(FormGenParser.ON_SUBMIT, 0)

        def NEWLINE(self):
            return self.getToken(FormGenParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(FormGenParser.INDENT, 0)

        def http_action(self):
            return self.getTypedRuleContext(FormGenParser.Http_actionContext,0)


        def success_clause(self):
            return self.getTypedRuleContext(FormGenParser.Success_clauseContext,0)


        def error_clause(self):
            return self.getTypedRuleContext(FormGenParser.Error_clauseContext,0)


        def DEDENT(self):
            return self.getToken(FormGenParser.DEDENT, 0)

        def getRuleIndex(self):
            return FormGenParser.RULE_on_submit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOn_submit" ):
                listener.enterOn_submit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOn_submit" ):
                listener.exitOn_submit(self)




    def on_submit(self):

        localctx = FormGenParser.On_submitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_on_submit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(FormGenParser.ON_SUBMIT)
            self.state = 201
            self.match(FormGenParser.NEWLINE)
            self.state = 202
            self.match(FormGenParser.INDENT)
            self.state = 203
            self.http_action()
            self.state = 204
            self.success_clause()
            self.state = 205
            self.error_clause()
            self.state = 206
            self.match(FormGenParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Http_actionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def http_method(self):
            return self.getTypedRuleContext(FormGenParser.Http_methodContext,0)


        def URL_PATH(self):
            return self.getToken(FormGenParser.URL_PATH, 0)

        def NEWLINE(self):
            return self.getToken(FormGenParser.NEWLINE, 0)

        def getRuleIndex(self):
            return FormGenParser.RULE_http_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHttp_action" ):
                listener.enterHttp_action(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHttp_action" ):
                listener.exitHttp_action(self)




    def http_action(self):

        localctx = FormGenParser.Http_actionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_http_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.http_method()
            self.state = 209
            self.match(FormGenParser.URL_PATH)
            self.state = 210
            self.match(FormGenParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Http_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POST(self):
            return self.getToken(FormGenParser.POST, 0)

        def GET(self):
            return self.getToken(FormGenParser.GET, 0)

        def getRuleIndex(self):
            return FormGenParser.RULE_http_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHttp_method" ):
                listener.enterHttp_method(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHttp_method" ):
                listener.exitHttp_method(self)




    def http_method(self):

        localctx = FormGenParser.Http_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_http_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            _la = self._input.LA(1)
            if not(_la==51 or _la==52):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Success_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUCCESS(self):
            return self.getToken(FormGenParser.SUCCESS, 0)

        def COLON(self):
            return self.getToken(FormGenParser.COLON, 0)

        def STRING(self):
            return self.getToken(FormGenParser.STRING, 0)

        def NEWLINE(self):
            return self.getToken(FormGenParser.NEWLINE, 0)

        def arrow_action(self):
            return self.getTypedRuleContext(FormGenParser.Arrow_actionContext,0)


        def getRuleIndex(self):
            return FormGenParser.RULE_success_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuccess_clause" ):
                listener.enterSuccess_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuccess_clause" ):
                listener.exitSuccess_clause(self)




    def success_clause(self):

        localctx = FormGenParser.Success_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_success_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(FormGenParser.SUCCESS)
            self.state = 215
            self.match(FormGenParser.COLON)
            self.state = 216
            self.match(FormGenParser.STRING)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==63:
                self.state = 217
                self.arrow_action()


            self.state = 220
            self.match(FormGenParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Error_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ERROR(self):
            return self.getToken(FormGenParser.ERROR, 0)

        def COLON(self):
            return self.getToken(FormGenParser.COLON, 0)

        def STRING(self):
            return self.getToken(FormGenParser.STRING, 0)

        def NEWLINE(self):
            return self.getToken(FormGenParser.NEWLINE, 0)

        def getRuleIndex(self):
            return FormGenParser.RULE_error_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterError_clause" ):
                listener.enterError_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitError_clause" ):
                listener.exitError_clause(self)




    def error_clause(self):

        localctx = FormGenParser.Error_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_error_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(FormGenParser.ERROR)
            self.state = 223
            self.match(FormGenParser.COLON)
            self.state = 224
            self.match(FormGenParser.STRING)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==71:
                self.state = 225
                self.match(FormGenParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arrow_actionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARROW(self):
            return self.getToken(FormGenParser.ARROW, 0)

        def REDIRECT(self):
            return self.getToken(FormGenParser.REDIRECT, 0)

        def URL_PATH(self):
            return self.getToken(FormGenParser.URL_PATH, 0)

        def getRuleIndex(self):
            return FormGenParser.RULE_arrow_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrow_action" ):
                listener.enterArrow_action(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrow_action" ):
                listener.exitArrow_action(self)




    def arrow_action(self):

        localctx = FormGenParser.Arrow_actionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arrow_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(FormGenParser.ARROW)
            self.state = 229
            self.match(FormGenParser.REDIRECT)
            self.state = 230
            self.match(FormGenParser.URL_PATH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





