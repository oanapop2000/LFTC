f = open("fileInput1.txt", "r")
# f = open("fileInput2.txt", "r")
# f = open("fileInput3.txt", "r")
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


# def scrieInAutomatId():
#     litere = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#               'v', 'w', 'x', 'y', 'z']
#     f = open("automatId.txt", "w")
#     for litera in litere:
#         f.write(litera + " ")
#     f.write('\n')
#     ok = 1
#     for i in range(250):
#         f.write('q' + str(i) + " ")
#         for j in range(len(litere)):
#             f.write('q' + str((i + 1)) + " ")
#         if ok == 1:
#             f.write('0')
#             ok = 0
#         else:
#             f.write('1')
#         f.write('\n')
#     f.write('q' + str(250) + " ")
#     for j in range(len(litere)):
#         f.write("-" + " ")
#     f.write('1')
#
#
# scrieInAutomatId()


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


# def numberOrString(cuvantNou):
#     try:
#         float(cuvantNou)
#         ok = 1
#     except ValueError:
#         ok = 0
#     return ok


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


matriceConst = [[0 for x in range(100)] for y in range(100)]
stariConst = []
tranzitiiConst = [[0 for x in range(100)] for y in range(100)]
stariFinaleConst = []
matriceId = [[0 for x in range(30)] for y in range(62500)]
stariId = []
tranzitiiId = [[0 for x in range(30)] for y in range(62500)]
stariFinaleId = []


def citireFisier():
    f = open("automatConst.txt", "r")
    g = open("automatId.txt", "r")
    linesConst = f.readlines()

    alfabetConst = linesConst[0].strip()
    alfabetConst = alfabetConst.split(" ")
    i = 0

    for caracter in alfabetConst:
        matriceConst[0][i] = caracter
        i = i + 1

    for i in range(1, len(linesConst)):
        j = 0
        linie = linesConst[i].strip()
        linie = linie.split(" ")
        for stare in linie:
            matriceConst[i][j] = stare
            j = j + 1

    nrStariConst = i

    linesId = g.readlines()

    alfabetId = linesId[0].strip()
    alfabetId = alfabetId.split(" ")
    i = 0

    for caracter in alfabetId:
        matriceId[0][i] = caracter
        i = i + 1

    for i in range(1, len(linesId)):
        j = 0
        linie = linesId[i].strip()
        linie = linie.split(" ")
        for stare in linie:
            matriceId[i][j] = stare
            j = j + 1

    nrStariId = i

    return alfabetConst, nrStariConst, alfabetId, nrStariId


def creareTranzitii(k, l, stare, stareActuala, j):
    tranzitiiConst[k][l] = stareActuala
    l = l + 1
    tranzitiiConst[k][l] = matriceConst[0][j - 1]
    l = l + 1
    tranzitiiConst[k][l] = stare
    k = k + 1
    l = 0
    return k, l

def creareTranzitiiId(k, l, stare, stareActuala, j):
    tranzitiiId[k][l] = stareActuala
    l = l + 1
    tranzitiiId[k][l] = matriceId[0][j - 1]
    l = l + 1
    tranzitiiId[k][l] = stare
    k = k + 1
    l = 0
    return k, l


def creareMatriceConst():
    k = 0
    l = 0
    okD = 1
    nrTranzitii = 0
    for i in range(1, nrStariConst + 1):
        stareActuala = matriceConst[i][0]
        stariConst.append(stareActuala)
        for j in range(1, len(alfabetConst) + 1):
            if matriceConst[i][j] != '-' and ',' not in matriceConst[i][j]:
                k, l = creareTranzitii(k, l, matriceConst[i][j], stareActuala, j)
            elif matriceConst[i][j] != '-' and ',' in matriceConst[i][j]:
                okD = 0
                listStari = str(matriceConst[i][j]).split(',')
                for a in range(len(listStari)):
                    k, l = creareTranzitii(k, l, listStari[a], stareActuala, j)
        nrTranzitii = k
        if matriceConst[i][len(alfabetConst) + 1] == '1':
            stariFinaleConst.append(stareActuala)


    return okD, nrTranzitii


def creareMatriceId():
    k = 0
    l = 0
    okD = 1
    nrTranzitii = 0
    for i in range(1, nrStariId + 1):
        stareActuala = matriceId[i][0]
        stariId.append(stareActuala)
        for j in range(1, len(alfabetId) + 1):
            if matriceId[i][j] != '-' and ',' not in matriceId[i][j]:
                k, l = creareTranzitiiId(k, l, matriceId[i][j], stareActuala, j)
            elif matriceId[i][j] != '-' and ',' in matriceId[i][j]:
                okD = 0
                listStari = str(matriceId[i][j]).split(',')
                for a in range(len(listStari)):
                    k, l = creareTranzitiiId(k, l, listStari[a], stareActuala, j)
        nrTranzitii = k
        if matriceId[i][len(alfabetId) + 1] == '1':
            stariFinaleId.append(stareActuala)

    return okD, nrTranzitii


alfabetConst, nrStariConst, alfabetId, nrStariId = citireFisier()
okDetConst, nrTranzitiiConst = creareMatriceConst()
okDetId, nrTranzitiiId = creareMatriceId()


def verifConst(secventa):
    a_list = [x for x in str(secventa)]
    stareActuala = matriceConst[1][0]
    for ch in a_list:
        ok = 0
        i = 0
        while ok == 0 and i < nrTranzitiiConst:
            if tranzitiiConst[i][0] == stareActuala and tranzitiiConst[i][1] == str(ch):
                stareActuala = tranzitiiConst[i][2]
                ok = 1
            i = i + 1
        if ok == 0:
            return "Secventa nu este acceptata de automatulConst"
    if stareActuala in stariFinaleConst:
        eroare = "Secventa este acceptata de automatulConst"
    else:
        eroare = "Secventa nu este acceptata de automatulConst"
    return eroare

def verifId(secventa):
    a_list = [x for x in str(secventa)]
    stareActuala = matriceId[1][0]
    for ch in a_list:
        ok = 0
        i = 0
        while ok == 0 and i < nrTranzitiiId:
            if tranzitiiId[i][0] == stareActuala and tranzitiiId[i][1] == str(ch):
                stareActuala = tranzitiiId[i][2]
                ok = 1
            i = i + 1
        if ok == 0:
            return "Secventa nu este acceptata de automatulId"
    if stareActuala in stariFinaleId:
        eroare = "Secventa este acceptata de automatulId"
    else:
        eroare = "Secventa nu este acceptata de automatulId"
    return eroare


for i in range(0, len(text)):
    cuvantNou = ''
    ok1 = 0
    for j in range(0, len(text[i])):
        if ok1 == 0:
            if text[i][j] in eroriLexicale:
                print('Eroare lexicala pe linia ' + str(i + 1) + ' cauzata de ' + text[i][j])
            else:
                if text[i][j - 1] != '!':
                    if text[i][j] == '.':
                        cuvantNou = cuvantNou + text[i][j]
                    elif text[i][j].isdigit() or text[i][j].isalpha() or text[i][j] == '#':
                        cuvantNou = cuvantNou + text[i][j]
                    elif text[i][j] == ' ' or text[i][j] == '\n':
                        if cuvantNou != '':
                            if cuvantNou in char_list:
                                cod, nrCuvinteFisier = appendWord(cuvantNou, cod, nrCuvinteFisier)
                                cuvantNou = ''

                            else:
                                if verifConst(cuvantNou) == "Secventa este acceptata de automatulConst":
                                    codConst, cod, codTS, nrCuvinteFisier, coduriTS = appendConst(codConst, cod,
                                                                                                  codTS,
                                                                                                  nrCuvinteFisier,
                                                                                                  coduriTS)
                                else:
                                    if verifId(cuvantNou) == "Secventa este acceptata de automatulId":
                                        cod, codTS, nrCuvinteFisier, codID, coduriTS = appendID(codID, cod, codTS,
                                                                                                nrCuvinteFisier,
                                                                                                cuvantNou,
                                                                                                coduriTS)
                                    else:
                                        print('Eroare lexicala pe linia ' + str(i + 1) + ' cauzata de ' + cuvantNou)
                                cuvantNou = ''


                    else:
                        if cuvantNou != '':
                            if cuvantNou in char_list:
                                cod, nrCuvinteFisier = appendWord(cuvantNou, cod, nrCuvinteFisier)
                                cuvantNou = ''
                            else:
                                # ok = numberOrString(cuvantNou)
                                # if ok == 0:
                                #     contains_digit = any(map(str.isdigit, cuvantNou))
                                #     if contains_digit is True:
                                #         print('Eroare lexicala pe linia ' + str(i + 1) + ' cauzata de ' + cuvantNou)
                                #     elif len(cuvantNou) > 250:
                                #         print('Eroare lexicala pe linia ' + str(i + 1) + ' cauzata de ' + cuvantNou)
                                #     else:
                                #         cod, codTS, nrCuvinteFisier, codID, coduriTS = appendID(codID, cod, codTS,
                                #                                                                 nrCuvinteFisier,
                                #                                                                 cuvantNou,
                                #                                                                 coduriTS)
                                #
                                #     cuvantNou = ''
                                #
                                # else:
                                if verifConst(cuvantNou) == "Secventa este acceptata de automatulConst":
                                    codConst, cod, codTS, nrCuvinteFisier, coduriTS = appendConst(codConst, cod,
                                                                                                  codTS,
                                                                                                  nrCuvinteFisier,
                                                                                                  coduriTS)
                                else:
                                    if verifId(cuvantNou) == "Secventa este acceptata de automatulId":
                                        cod, codTS, nrCuvinteFisier, codID, coduriTS = appendID(codID, cod, codTS,
                                                                                                nrCuvinteFisier,
                                                                                                cuvantNou,
                                                                                                coduriTS)
                                    else:
                                        print('Eroare lexicala pe linia ' + str(i + 1) + ' cauzata de ' + cuvantNou)

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
