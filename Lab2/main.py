# f = open("fileInput1.txt", "r")
# f = open("fileInput2.txt", "r")
f = open("fileInput3.txt", "r")
text = f.readlines()

f = open("fileOutput.txt", "w")
cuvinteAparitii = {}
cuvinteFisier = [[0 for x in range(3)] for y in range(1000)]
char_list = [',', ';', '(', ')', '{', '=', 'cin', '>>', '*', '#include', '<', '>', 'iostream', 'using', 'namespace',
             'std', 'int',
             'main', 'double', 'cout', 'return', '}', 'while', 'if', '-', '+', 'else']
eroriLexicale = ['@', '$', '%', '^', '&', '~', '_', '[', ']', '|', ':', '"', '?']

cod = 0
codID = -1
codConst = -1
nrCuvinteFisier = 0
codTS = 0
coduriTS = []


def adaugaOrdonat(coduriTS, list):
    if len(coduriTS) == 0:
        coduriTS.append(list)
    else:
        ok = 0
        for i in range(len(coduriTS)):
            if coduriTS[i][0] > list[0]:
                coduriTS = coduriTS[:i] + [list] + coduriTS[i:]
                ok = 1
                break
        if ok == 0:
            coduriTS.append(list)
    return coduriTS


def getCod(coduriTS, cuvantNou):
    for list in coduriTS:
        if list[0] == cuvantNou:
            return list[1]


def appendWord(cuvantNou, cod, nrCuvinteFisier):
    if cuvantNou not in cuvinteAparitii:
        cuvinteAparitii[cuvantNou] = cod
        cod = cod + 1
    cuvinteFisier[nrCuvinteFisier][0] = cuvantNou
    cuvinteFisier[nrCuvinteFisier][1] = cuvinteAparitii.get(cuvantNou)
    cuvinteFisier[nrCuvinteFisier][2] = '-'
    nrCuvinteFisier = nrCuvinteFisier + 1
    return cod, nrCuvinteFisier


def numberOrString(cuvantNou):
    try:
        float(cuvantNou)
        ok = 1
    except ValueError:
        ok = 0
    return ok


def appendID(codID, cod, codTS, nrCuvinteFisier, cuvantNou, coduriTS):
    if cuvantNou not in cuvinteAparitii:
        if codID == -1:
            codID = cod
            cod = cod + 1
        list = []
        list.append(cuvantNou)
        list.append(codTS)
        coduriTS = adaugaOrdonat(coduriTS, list)
        codTS = codTS + 1
        cuvinteAparitii[cuvantNou] = codID
    cuvinteFisier[nrCuvinteFisier][0] = cuvantNou
    cuvinteFisier[nrCuvinteFisier][1] = cuvinteAparitii.get(cuvantNou)
    cuvinteFisier[nrCuvinteFisier][2] = getCod(coduriTS, cuvantNou)
    nrCuvinteFisier = nrCuvinteFisier + 1
    return cod, codTS, nrCuvinteFisier, codID, coduriTS


def appendConst(codConst, cod, codTS, nrCuvinteFisier, coduriTS):
    if cuvantNou not in cuvinteAparitii:
        if codConst == -1:
            codConst = cod
            cod = cod + 1
        list = []
        list.append(cuvantNou)
        list.append(codTS)
        coduriTS = adaugaOrdonat(coduriTS, list)
        codTS = codTS + 1
        cuvinteAparitii[cuvantNou] = codConst
    cuvinteFisier[nrCuvinteFisier][0] = cuvantNou
    cuvinteFisier[nrCuvinteFisier][1] = cuvinteAparitii.get(cuvantNou)
    cuvinteFisier[nrCuvinteFisier][2] = getCod(coduriTS, cuvantNou)
    nrCuvinteFisier = nrCuvinteFisier + 1
    return codConst, cod, codTS, nrCuvinteFisier, coduriTS


for i in range(0, len(text)):
    cuvantNou = ''
    ok1 = 0
    for j in range(0, len(text[i])):
        if ok1 == 0:
            if text[i][j] in eroriLexicale:
                print('Eroare lexicala pe linia ' + str(i + 1) + ' cauzata de ' + text[i][j])
            else:
                if text[i][j - 1] != '!':
                    if text[i][j] == '.' and cuvantNou[len(cuvantNou) - 1].isdigit():
                        cuvantNou = cuvantNou + text[i][j]
                    elif text[i][j].isdigit() or text[i][j].isalpha() or text[i][j] == '#':
                        cuvantNou = cuvantNou + text[i][j]
                    elif text[i][j] == ' ' or text[i][j] == '\n':
                        if cuvantNou != '':
                            if cuvantNou in char_list:
                                cod, nrCuvinteFisier = appendWord(cuvantNou, cod, nrCuvinteFisier)
                                cuvantNou = ''

                            else:
                                ok = numberOrString(cuvantNou)
                                if ok == 0:
                                    contains_digit = any(map(str.isdigit, cuvantNou))
                                    if contains_digit is True:
                                        print('Eroare lexicala pe linia ' + str(i + 1) + ' cauzata de ' + cuvantNou)
                                    elif len(cuvantNou) > 250:
                                        print('Eroare lexicala pe linia ' + str(i + 1) + ' cauzata de ' + cuvantNou)
                                    else:
                                        cod, codTS, nrCuvinteFisier, codID, coduriTS = appendID(codID, cod, codTS,
                                                                                      nrCuvinteFisier, cuvantNou,
                                                                                      coduriTS)

                                    cuvantNou = ''

                                else:
                                    codConst, cod, codTS, nrCuvinteFisier, coduriTS = appendConst(codConst, cod, codTS,
                                                                                        nrCuvinteFisier, coduriTS)
                                    cuvantNou = ''


                    else:
                        if cuvantNou != '':
                            if cuvantNou in char_list:
                                cod, nrCuvinteFisier = appendWord(cuvantNou, cod, nrCuvinteFisier)
                                cuvantNou = ''
                            else:
                                ok = numberOrString(cuvantNou)
                                if ok == 0:
                                    contains_digit = any(map(str.isdigit, cuvantNou))
                                    if contains_digit is True:
                                        print('Eroare lexicala pe linia ' + str(i + 1) + ' cauzata de ' + cuvantNou)
                                    elif len(cuvantNou) > 250:
                                        print('Eroare lexicala pe linia ' + str(i + 1) + ' cauzata de ' + cuvantNou)
                                    else:
                                        cod, codTS, nrCuvinteFisier, codID, coduriTS = appendID(codID, cod, codTS,
                                                                                      nrCuvinteFisier, cuvantNou,
                                                                                      coduriTS)

                                    cuvantNou = ''

                                else:
                                    codConst, cod, codTS, nrCuvinteFisier, coduriTS = appendConst(codConst, cod, codTS,
                                                                                        nrCuvinteFisier, coduriTS)
                                    cuvantNou = ''

                        if text[i][j] in char_list:
                            if text[i][j] != '<' and text[i][j] != '>':
                                cod, nrCuvinteFisier = appendWord(text[i][j], cod, nrCuvinteFisier)
                            else:
                                if text[i][j] == '>' and text[i][j - 1] != '>' and text[i][j + 1] != '>':
                                    cod, nrCuvinteFisier = appendWord(text[i][j], cod, nrCuvinteFisier)
                                elif text[i][j] == '<' and text[i][j - 1] != '<' and text[i][j + 1] != '<':
                                    cod, nrCuvinteFisier = appendWord(text[i][j], cod, nrCuvinteFisier)
                                elif text[i][j] == '<' and text[i][j + 1] == '<':
                                    cod, nrCuvinteFisier = appendWord('<<', cod, nrCuvinteFisier)
                                elif text[i][j] == '>' and text[i][j + 1] == '>':
                                    cod, nrCuvinteFisier = appendWord('>>', cod, nrCuvinteFisier)

                        elif text[i][j] == '!' and text[i][j + 1] == '=':
                            cod, nrCuvinteFisier = appendWord('!=', cod, nrCuvinteFisier)

                        elif text[i][j] == "\\":
                            cod, nrCuvinteFisier = appendWord("' ", cod, nrCuvinteFisier)
                            cod, nrCuvinteFisier = appendWord("\ ", cod, nrCuvinteFisier)
                            cod, codTS, nrCuvinteFisier, codID, coduriTS = appendID(codID, cod, codTS,
                                                                          nrCuvinteFisier, 'n', coduriTS)
                            cod, nrCuvinteFisier = appendWord("' ", cod, nrCuvinteFisier)
                            cod, nrCuvinteFisier = appendWord(";", cod, nrCuvinteFisier)
                            ok1 = 1

f.write('{:>12}' '{:>26}' '{:>30}'.format("Programul", "Tabela FIP", "Tabela TS") + '\n')
f.write('{:>14} {:>14} {:>14} {:>14} {:>14}'.format("Atomi lexicali", "Cod atom", "Cod TS", "Simbol", "Cod TS") + '\n')

i = 0
for list in coduriTS:
    f.write(
        '{:>14} {:>14} {:>14} {:>14} {:>14}'.format(cuvinteFisier[i][0], str(cuvinteFisier[i][1]), cuvinteFisier[i][2],
                                                    list[0], list[1]) + '\n')
    i = i + 1

for j in range(i, nrCuvinteFisier):
    f.write('{:>14} {:>14} {:>14}'.format(cuvinteFisier[j][0], str(cuvinteFisier[j][1]), cuvinteFisier[j][2]) + '\n')
