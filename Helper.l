%option noyywrap
%{
	#include<stdio.h>
	#include "Tema.tab.h"
%}
letter [a-z]
digit [0-9]
double [0-9]*\.[0-9]+
int [0-9]*
id [a-z]([a-z])*

%%
"#include"|"iostream"|"using"|"namespace"|"std"|"main"|"for"|"while"|"if"|"struct" {printf("Keyword : %s \n",yytext); return(KEYWORD);}

"repeta" {printf("Repeta : %s \n",yytext); return(REPETA);}

"panacand" {printf("Panacand : %s \n",yytext); return(PANACAND);}

"sfrepeta" {printf("Sfrepeta : %s \n",yytext); return(SFREPETA);}

"return" {printf("Return : %s \n",yytext); return(RETURN);}

"else" {printf("Else : %s \n",yytext); return(ELSE);}

"{"|"}"|"("|")" {printf("Paranthesis: %s \n",yytext); return(PARANTHESIS);}

"int"|"double" {printf("Data Type: %s \n",yytext); return(DATA_TYPE);}

{double} {printf("Double Constant : %s \n",yytext); return(DOUBLE_CONSTANT);}

{int} {printf("Integer Constant : %s \n",yytext); return(INTEGER_CONSTANT);}

{id} {printf("Identifier : %s \n",yytext); return(ID);}

"," {printf("Comma : %s \n",yytext); return(COMMA);}

";" {printf("Semicolon : %s \n",yytext); return(SEMICOLON);}

"=" {printf("Assignment Operator : %s \n",yytext); return(ASSIGNMENT_OPERATOR);}

"-"|"+"|"*" {printf("Arithmetic Operator : %s \n",yytext); return(ARITHMETIC_OPERATOR);}

"<"|">"|"!=" {printf("Relational Operator : %s \n", yytext); return(RELATIONAL_OPERATOR);}

"cin>>"|"cout<<" {printf("Cin_Cout : %s \n", yytext); return(CIN_COUT);}
 
[ \t\n] ;

%%