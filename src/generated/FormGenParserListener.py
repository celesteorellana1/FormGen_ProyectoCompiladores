from antlr4 import *
if "." in __name__:
    from .FormGenParser import FormGenParser
else:
    from FormGenParser import FormGenParser

class FormGenParserListener(ParseTreeListener):

    def enterProgram(self, ctx:FormGenParser.ProgramContext):
        pass

    def exitProgram(self, ctx:FormGenParser.ProgramContext):
        pass

    def enterForm_def(self, ctx:FormGenParser.Form_defContext):
        pass

    def exitForm_def(self, ctx:FormGenParser.Form_defContext):
        pass

    def enterForm_attr(self, ctx:FormGenParser.Form_attrContext):
        pass

    def exitForm_attr(self, ctx:FormGenParser.Form_attrContext):
        pass

    def enterTheme_value(self, ctx:FormGenParser.Theme_valueContext):
        pass

    def exitTheme_value(self, ctx:FormGenParser.Theme_valueContext):
        pass

    def enterLayout_value(self, ctx:FormGenParser.Layout_valueContext):
        pass

    def exitLayout_value(self, ctx:FormGenParser.Layout_valueContext):
        pass

    def enterSize_value(self, ctx:FormGenParser.Size_valueContext):
        pass

    def exitSize_value(self, ctx:FormGenParser.Size_valueContext):
        pass

    def enterSection(self, ctx:FormGenParser.SectionContext):
        pass

    def exitSection(self, ctx:FormGenParser.SectionContext):
        pass

    def enterField(self, ctx:FormGenParser.FieldContext):
        pass

    def exitField(self, ctx:FormGenParser.FieldContext):
        pass

    def enterField_prop(self, ctx:FormGenParser.Field_propContext):
        pass

    def exitField_prop(self, ctx:FormGenParser.Field_propContext):
        pass

    def enterField_type(self, ctx:FormGenParser.Field_typeContext):
        pass

    def exitField_type(self, ctx:FormGenParser.Field_typeContext):
        pass

    def enterIcon_value(self, ctx:FormGenParser.Icon_valueContext):
        pass

    def exitIcon_value(self, ctx:FormGenParser.Icon_valueContext):
        pass

    def enterOption_list(self, ctx:FormGenParser.Option_listContext):
        pass

    def exitOption_list(self, ctx:FormGenParser.Option_listContext):
        pass

    def enterValue(self, ctx:FormGenParser.ValueContext):
        pass

    def exitValue(self, ctx:FormGenParser.ValueContext):
        pass

    def enterNumber(self, ctx:FormGenParser.NumberContext):
        pass

    def exitNumber(self, ctx:FormGenParser.NumberContext):
        pass

    def enterBoolean_val(self, ctx:FormGenParser.Boolean_valContext):
        pass

    def exitBoolean_val(self, ctx:FormGenParser.Boolean_valContext):
        pass

    def enterIdentifier(self, ctx:FormGenParser.IdentifierContext):
        pass

    def exitIdentifier(self, ctx:FormGenParser.IdentifierContext):
        pass

    def enterOn_submit(self, ctx:FormGenParser.On_submitContext):
        pass

    def exitOn_submit(self, ctx:FormGenParser.On_submitContext):
        pass

    def enterHttp_action(self, ctx:FormGenParser.Http_actionContext):
        pass

    def exitHttp_action(self, ctx:FormGenParser.Http_actionContext):
        pass

    def enterHttp_method(self, ctx:FormGenParser.Http_methodContext):
        pass

    def exitHttp_method(self, ctx:FormGenParser.Http_methodContext):
        pass

    def enterSuccess_clause(self, ctx:FormGenParser.Success_clauseContext):
        pass

    def exitSuccess_clause(self, ctx:FormGenParser.Success_clauseContext):
        pass

    def enterError_clause(self, ctx:FormGenParser.Error_clauseContext):
        pass

    def exitError_clause(self, ctx:FormGenParser.Error_clauseContext):
        pass

    def enterArrow_action(self, ctx:FormGenParser.Arrow_actionContext):
        pass

    def exitArrow_action(self, ctx:FormGenParser.Arrow_actionContext):
        pass

del FormGenParser
