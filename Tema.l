%option noyywrap
%{
	#include<stdio.h>
%}
letter [a-z]
digit [0-9]
double [0-9]*\.[0-9]+
int [0-9]*
id [a-z]([a-z])*

%%
"#include"|"iostream"|"using"|"namespace"|"std"|"main"|"return"|"for"|"while"|"if"|"else"|"cin>>"|"cout<<"|"cattimp"|"executa"|"sfcattimp" {printf("Keyword : %s \n",yytext);}

"{"|"}"|"("|")" {printf("Paranthesis: %s \n",yytext);}

"int"|"double" {printf("Data Type: %s \n",yytext);}

{double} {printf("Double Constant : %s \n",yytext);}

{int} {printf("Integer Constant : %s \n",yytext);}

{id} {printf("Identifier : %s \n",yytext);}

[,;] {printf("Delimiter : %s \n",yytext);}

"=" {printf("Assignment Operator : %s \n",yytext);}

"-"|"+"|"*" {printf("Arithmetic Operator : %s \n",yytext);}

"<"|">"|"!=" {printf("Relational Operator : %s \n", yytext);}

[ \t\n] ;

%%
int main()
{
	FILE *fp;
	fp=fopen("main3.cpp","r");
	yyin=fp;
	yylex();
	fclose(fp);
	return 0;
}