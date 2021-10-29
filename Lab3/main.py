stari = []
stariFinale = []
matrice = [[0 for x in range(100)] for y in range(100)]
tranzitii = [[0 for x in range(100)] for y in range(100)]


def citireFisier():
    f = open("in.txt", "r")
    lines = f.readlines()
    alfabet = lines[0].strip()
    alfabet = alfabet.split(" ")
    i = 0

    for caracter in alfabet:
        matrice[0][i] = caracter
        i = i + 1

    for i in range(1, len(lines)):
        j = 0
        linie = lines[i].strip()
        linie = linie.split(" ")
        for stare in linie:
            matrice[i][j] = stare
            j = j + 1

    nrStari = i

    return alfabet, nrStari


def citireTastatura():
    alfabet = input()
    alfabet = alfabet.split(" ")
    i = 0

    for caracter in alfabet:
        matrice[0][i] = caracter
        i = i + 1

    linie = input()
    i = 1
    while linie != '':
        j = 0
        linie = linie.strip()
        linie = linie.split(" ")
        for stare in linie:
            matrice[i][j] = stare
            j = j + 1
        linie = input()
        i = i + 1

    nrStari = i - 1

    return alfabet, nrStari


def optiuniCitire():
    ok = 0
    print("1. Citire din fisier" + '\n' + "2. Citire de la tastatura")
    while ok == 0:
        try:
            optiune = int(input())
            if optiune == 1:
                alfabet, nrStari = citireFisier()
                ok = 1
            elif optiune == 2:
                alfabet, nrStari = citireTastatura()
                ok = 1
            else:
                print("Optiunea aleasa nu exista")

        except ValueError:
            print("Nu ati introdus o cifra!")
    return alfabet, nrStari


def creareTranzitii(k, l, stare, stareActuala, j):
    tranzitii[k][l] = stareActuala
    l = l + 1
    tranzitii[k][l] = matrice[0][j - 1]
    l = l + 1
    tranzitii[k][l] = stare
    k = k + 1
    l = 0
    return k, l

def creareMatrice():
    k = 0
    l = 0
    okD = 1
    nrTranzitii = 0
    for i in range(1, nrStari + 1):
        stareActuala = matrice[i][0]
        stari.append(stareActuala)
        for j in range(1, len(alfabet) + 1):
            if matrice[i][j] != '-' and ',' not in matrice[i][j]:
                k, l = creareTranzitii(k, l, matrice[i][j], stareActuala, j)
            elif matrice[i][j] != '-' and ',' in matrice[i][j]:
                okD = 0
                listStari = str(matrice[i][j]).split(',')
                for a in range(len(listStari)):
                    k, l = creareTranzitii(k, l, listStari[a], stareActuala, j)
        nrTranzitii = k
        if matrice[i][len(alfabet) + 1] == '1':
            stariFinale.append(stareActuala)
    return okD, nrTranzitii


alfabet, nrStari = optiuniCitire()
okD, nrTranzitii = creareMatrice()


comanda = 1

while comanda != 0:
    print(
        "1. Afiseaza multimea starilor" + '\n' + "2. Afiseaza alfabetul" + '\n' + "3. Afiseaza tranzitiile" + '\n' + "4. Afiseaza multimea starilor finale" + '\n' + "5. Verifica daca o secventa este acceptata de automat" + '\n' + "6. Determina cel mai lung prefix dintr-o secventa data")
    print("Introduceti optiunea dorita: ")
    try:
        comanda = int(input())
        if comanda == 1:
            print("Multimea starilor este: " + '\n' + "{", end="")
            for stare in stari:
                print(stare + " ", end="")
            print('}')

        elif comanda == 2:
            print("Alfabetul este: " + '\n' + "{", end="")
            for litera in alfabet:
                print(litera + " ", end="")
            print('}')

        elif comanda == 3:
            print("Tranzitiile sunt: ")
            for i in range(nrTranzitii):
                for j in range(0, 3):
                    print(str(tranzitii[i][j]) + ' ', end="")
                print("")

        elif comanda == 4:
            print("Multimea starilor finale este: " + '\n' + "{", end="")
            for stare in stariFinale:
                print(stare + " ", end="")
            print('}')

        elif comanda == 5:
            if okD == 0:
                print("Acest automat nu este determinist!")
            else:
                print("Introduceti secventa: ")
                try:
                    secventa = int(input())
                    a_list = [int(x) for x in str(secventa)]
                    stareActuala = matrice[1][0]
                    for ch in a_list:
                        ok = 0
                        i = 0
                        while ok == 0 and i < nrTranzitii:
                            if tranzitii[i][0] == stareActuala and tranzitii[i][1] == str(ch):
                                stareActuala = tranzitii[i][2]
                                ok = 1
                            i = i + 1
                    if stareActuala in stariFinale:
                        print("Secventa este acceptata de automat")
                    else:
                        print("Secventa nu este acceptata de automat")
                except ValueError:
                    print("Secventa nu este de forma int!")

        elif comanda == 6:
            if okD == 0:
                print("Acest automat nu este determinist!")
            else:
                print("Introduceti secventa: ")
                try:
                    secventa = int(input())
                    a_list = [int(x) for x in str(secventa)]
                    poz = -1
                    stareActuala = matrice[1][0]
                    j = 0
                    for j in range(len(a_list)):
                        ok = 0
                        i = 0
                        while ok == 0 and i < nrTranzitii:
                            if tranzitii[i][0] == stareActuala and tranzitii[i][1] == str(a_list[j]):
                                stareActuala = tranzitii[i][2]
                                ok = 1
                                if stareActuala in stariFinale:
                                    poz = j
                            i = i + 1

                    print("Subsecventa acceptata este: ")
                    if poz != -1:
                        for i in range(poz + 1):
                            print(a_list[i], end="")
                    else:
                        print("{}")
                    print()

                except ValueError:
                    print("Secventa nu este de forma int!")

        elif comanda not in [0, 1, 2, 3, 4, 5, 6]:
            print("Aceasta comanda nu exista")

    except ValueError:
        print("Nu ati introdus o cifra!")
