%{
	#include <stdio.h>
	#include <stdlib.h>
	#include "Tema.tab.h"

int yylex();
void yyerror(const char *s);
extern FILE *yyin;
%}
%token KEYWORD
%token PARANTHESIS
%token DATA_TYPE
%token DOUBLE_CONSTANT
%token INTEGER_CONSTANT
%token ID
%token COMMA
%token SEMICOLON
%token RETURN
%token ASSIGNMENT_OPERATOR
%token ARITHMETIC_OPERATOR
%token RELATIONAL_OPERATOR
%token CIN_COUT
%token ELSE
%token REPETA
%token PANACAND
%token SFREPETA

%%
Program : 
KEYWORD RELATIONAL_OPERATOR KEYWORD RELATIONAL_OPERATOR
KEYWORD KEYWORD KEYWORD SEMICOLON
DATA_TYPE KEYWORD PARANTHESIS PARANTHESIS PARANTHESIS
	Lista_instr
	RETURN INTEGER_CONSTANT SEMICOLON
	PARANTHESIS
		;
Lista_instr : Instr |
	      Instr Lista_instr
	      ;
Instr : Declarare |
	Atribuire |
   	Cin_Cout  |
	If |
	While |
	Repeta
	;
Declarare : Tip_Data Lista_ID
;
Tip_Data : DATA_TYPE | 
	   Tip_compus
	   ;
Tip_compus : KEYWORD ID PARANTHESIS Lista_declarari PARANTHESIS
;
Lista_declarari : Declarare SEMICOLON Lista_declarari |
		  Declarare SEMICOLON
;
Lista_ID : ID COMMA Lista_ID |
           ID SEMICOLON
;
Atribuire : ID ASSIGNMENT_OPERATOR INTEGER_CONSTANT SEMICOLON|
	    ID ASSIGNMENT_OPERATOR DOUBLE_CONSTANT SEMICOLON |
            ID ASSIGNMENT_OPERATOR INTEGER_CONSTANT ARITHMETIC_OPERATOR ID ARITHMETIC_OPERATOR ID SEMICOLON |
            ID ASSIGNMENT_OPERATOR ID ARITHMETIC_OPERATOR ID ARITHMETIC_OPERATOR ID SEMICOLON |
            ID ASSIGNMENT_OPERATOR ID ARITHMETIC_OPERATOR ID SEMICOLON |
            ID ASSIGNMENT_OPERATOR ID ARITHMETIC_OPERATOR INTEGER_CONSTANT SEMICOLON
	    ;
Cin_Cout : CIN_COUT ID SEMICOLON
	   ;
If : KEYWORD PARANTHESIS ID RELATIONAL_OPERATOR ID PARANTHESIS Lista_instr ELSE Lista_instr
;
While : KEYWORD PARANTHESIS ID RELATIONAL_OPERATOR ID PARANTHESIS Lista_instr |
	KEYWORD PARANTHESIS ID RELATIONAL_OPERATOR ID PARANTHESIS PARANTHESIS Lista_instr PARANTHESIS
	;
Repeta: REPETA Instr PANACAND PARANTHESIS ID PARANTHESIS SFREPETA
;

%%  
int main(void) {  
    FILE * pt = fopen("main3.cpp", "r" );  
    if(!pt)  
    {  
    printf("Bad Input.Noexistant file \n");  
    return -1;  
    }  
    yyin = pt;  
    do  
    {  
        yyparse();  
     }while (!feof(yyin));        
} 

void yyerror(const char *s)  
{  
   printf("Error. %s \n", s);   
   exit(-1);     
} 