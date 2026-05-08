# Generated from grammar/FormGenParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .FormGenParser import FormGenParser
else:
    from FormGenParser import FormGenParser

# This class defines a complete listener for a parse tree produced by FormGenParser.
class FormGenParserListener(ParseTreeListener):

    # Enter a parse tree produced by FormGenParser#program.
    def enterProgram(self, ctx:FormGenParser.ProgramContext):
        pass

    # Exit a parse tree produced by FormGenParser#program.
    def exitProgram(self, ctx:FormGenParser.ProgramContext):
        pass


    # Enter a parse tree produced by FormGenParser#form_def.
    def enterForm_def(self, ctx:FormGenParser.Form_defContext):
        pass

    # Exit a parse tree produced by FormGenParser#form_def.
    def exitForm_def(self, ctx:FormGenParser.Form_defContext):
        pass


    # Enter a parse tree produced by FormGenParser#form_attr.
    def enterForm_attr(self, ctx:FormGenParser.Form_attrContext):
        pass

    # Exit a parse tree produced by FormGenParser#form_attr.
    def exitForm_attr(self, ctx:FormGenParser.Form_attrContext):
        pass


    # Enter a parse tree produced by FormGenParser#theme_value.
    def enterTheme_value(self, ctx:FormGenParser.Theme_valueContext):
        pass

    # Exit a parse tree produced by FormGenParser#theme_value.
    def exitTheme_value(self, ctx:FormGenParser.Theme_valueContext):
        pass


    # Enter a parse tree produced by FormGenParser#layout_value.
    def enterLayout_value(self, ctx:FormGenParser.Layout_valueContext):
        pass

    # Exit a parse tree produced by FormGenParser#layout_value.
    def exitLayout_value(self, ctx:FormGenParser.Layout_valueContext):
        pass


    # Enter a parse tree produced by FormGenParser#size_value.
    def enterSize_value(self, ctx:FormGenParser.Size_valueContext):
        pass

    # Exit a parse tree produced by FormGenParser#size_value.
    def exitSize_value(self, ctx:FormGenParser.Size_valueContext):
        pass


    # Enter a parse tree produced by FormGenParser#section.
    def enterSection(self, ctx:FormGenParser.SectionContext):
        pass

    # Exit a parse tree produced by FormGenParser#section.
    def exitSection(self, ctx:FormGenParser.SectionContext):
        pass


    # Enter a parse tree produced by FormGenParser#field.
    def enterField(self, ctx:FormGenParser.FieldContext):
        pass

    # Exit a parse tree produced by FormGenParser#field.
    def exitField(self, ctx:FormGenParser.FieldContext):
        pass


    # Enter a parse tree produced by FormGenParser#field_prop.
    def enterField_prop(self, ctx:FormGenParser.Field_propContext):
        pass

    # Exit a parse tree produced by FormGenParser#field_prop.
    def exitField_prop(self, ctx:FormGenParser.Field_propContext):
        pass


    # Enter a parse tree produced by FormGenParser#field_type.
    def enterField_type(self, ctx:FormGenParser.Field_typeContext):
        pass

    # Exit a parse tree produced by FormGenParser#field_type.
    def exitField_type(self, ctx:FormGenParser.Field_typeContext):
        pass


    # Enter a parse tree produced by FormGenParser#icon_value.
    def enterIcon_value(self, ctx:FormGenParser.Icon_valueContext):
        pass

    # Exit a parse tree produced by FormGenParser#icon_value.
    def exitIcon_value(self, ctx:FormGenParser.Icon_valueContext):
        pass


    # Enter a parse tree produced by FormGenParser#option_list.
    def enterOption_list(self, ctx:FormGenParser.Option_listContext):
        pass

    # Exit a parse tree produced by FormGenParser#option_list.
    def exitOption_list(self, ctx:FormGenParser.Option_listContext):
        pass


    # Enter a parse tree produced by FormGenParser#value.
    def enterValue(self, ctx:FormGenParser.ValueContext):
        pass

    # Exit a parse tree produced by FormGenParser#value.
    def exitValue(self, ctx:FormGenParser.ValueContext):
        pass


    # Enter a parse tree produced by FormGenParser#number.
    def enterNumber(self, ctx:FormGenParser.NumberContext):
        pass

    # Exit a parse tree produced by FormGenParser#number.
    def exitNumber(self, ctx:FormGenParser.NumberContext):
        pass


    # Enter a parse tree produced by FormGenParser#boolean_val.
    def enterBoolean_val(self, ctx:FormGenParser.Boolean_valContext):
        pass

    # Exit a parse tree produced by FormGenParser#boolean_val.
    def exitBoolean_val(self, ctx:FormGenParser.Boolean_valContext):
        pass


    # Enter a parse tree produced by FormGenParser#identifier.
    def enterIdentifier(self, ctx:FormGenParser.IdentifierContext):
        pass

    # Exit a parse tree produced by FormGenParser#identifier.
    def exitIdentifier(self, ctx:FormGenParser.IdentifierContext):
        pass


    # Enter a parse tree produced by FormGenParser#on_submit.
    def enterOn_submit(self, ctx:FormGenParser.On_submitContext):
        pass

    # Exit a parse tree produced by FormGenParser#on_submit.
    def exitOn_submit(self, ctx:FormGenParser.On_submitContext):
        pass


    # Enter a parse tree produced by FormGenParser#http_action.
    def enterHttp_action(self, ctx:FormGenParser.Http_actionContext):
        pass

    # Exit a parse tree produced by FormGenParser#http_action.
    def exitHttp_action(self, ctx:FormGenParser.Http_actionContext):
        pass


    # Enter a parse tree produced by FormGenParser#http_method.
    def enterHttp_method(self, ctx:FormGenParser.Http_methodContext):
        pass

    # Exit a parse tree produced by FormGenParser#http_method.
    def exitHttp_method(self, ctx:FormGenParser.Http_methodContext):
        pass


    # Enter a parse tree produced by FormGenParser#success_clause.
    def enterSuccess_clause(self, ctx:FormGenParser.Success_clauseContext):
        pass

    # Exit a parse tree produced by FormGenParser#success_clause.
    def exitSuccess_clause(self, ctx:FormGenParser.Success_clauseContext):
        pass


    # Enter a parse tree produced by FormGenParser#error_clause.
    def enterError_clause(self, ctx:FormGenParser.Error_clauseContext):
        pass

    # Exit a parse tree produced by FormGenParser#error_clause.
    def exitError_clause(self, ctx:FormGenParser.Error_clauseContext):
        pass


    # Enter a parse tree produced by FormGenParser#arrow_action.
    def enterArrow_action(self, ctx:FormGenParser.Arrow_actionContext):
        pass

    # Exit a parse tree produced by FormGenParser#arrow_action.
    def exitArrow_action(self, ctx:FormGenParser.Arrow_actionContext):
        pass



del FormGenParser