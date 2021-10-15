# f = open("fileInput1.txt", "r")
f = open("fileInput2.txt", "r")
# f = open("fileInput3.txt", "r")
text = f.readlines()

f = open("fileOutput.txt", "w")
cuvinteFiser = []
char_list = [',', ';', '(', ')', '{', '=', 'cin', '>>', '*', '#include', '<', '>', 'iostream', 'using', 'namespace',
             'std', 'int',
             'main', 'double', 'cout', 'return', '}', 'while', 'if', '-', '+', 'else']

for i in range(0, len(text)):
    cuvantNou = ''

    for j in range(0, len(text[i])):
        if text[i][j-1] != '!':
            if text[i][j].isdigit() or text[i][j].isalpha() or text[i][j] == '#':
                cuvantNou = cuvantNou + text[i][j]
            elif text[i][j] == ' ' or text[i][j] == '\n':
                if cuvantNou != '':
                    if cuvantNou in char_list:
                        if cuvantNou not in cuvinteFiser:
                            cuvinteFiser.append(cuvantNou)
                            f.write(cuvantNou)
                            f.write('\n')
                            cuvantNou = ''

                    else:
                        try:
                            an_integer = int(cuvantNou)
                            ok = 1
                        except ValueError:
                            ok = 0
                        if ok == 0:
                            cuvantNou = 'ID'
                            if cuvantNou not in cuvinteFiser:
                                f.write(cuvantNou)
                                f.write('\n')
                                cuvinteFiser.append(cuvantNou)
                            cuvantNou = ''

                        else:
                            cuvantNou = 'CONST'
                            if cuvantNou not in cuvinteFiser:
                                f.write(cuvantNou)
                                f.write('\n')
                                cuvinteFiser.append(cuvantNou)
                            cuvantNou = ''


            else:
                if cuvantNou != '':
                    if cuvantNou in char_list:
                        if cuvantNou not in cuvinteFiser:
                            cuvinteFiser.append(cuvantNou)
                            f.write(cuvantNou)
                            f.write('\n')
                            cuvantNou = ''
                    else:
                        try:
                            an_integer = int(cuvantNou)
                            ok = 1
                        except ValueError:
                            ok = 0
                        if ok == 0:
                            cuvantNou = 'ID'
                            if cuvantNou not in cuvinteFiser:
                                f.write(cuvantNou)
                                f.write('\n')
                                cuvinteFiser.append(cuvantNou)
                            cuvantNou = ''

                        else:
                            cuvantNou = 'CONST'
                            if cuvantNou not in cuvinteFiser:
                                f.write(cuvantNou)
                                f.write('\n')
                                cuvinteFiser.append(cuvantNou)
                            cuvantNou = ''

                if text[i][j] in char_list:
                    if text[i][j] == '<' and text[i][j + 1] == '<' and '<<' not in cuvinteFiser:
                        j = j + 1
                        cuvinteFiser.append('<<')
                        f.write('<<')
                        f.write('\n')
                    elif text[i][j] == '>' and text[i][j + 1] == '>' and '>>' not in cuvinteFiser:
                        j = j + 1
                        cuvinteFiser.append('>>')
                        f.write('>>')
                        f.write('\n')
                    elif text[i][j] not in cuvinteFiser:
                        cuvinteFiser.append(text[i][j])
                        f.write(text[i][j])
                        f.write('\n')

                elif text[i][j] == '!' and text[i][j + 1] == '=' and '!=' not in cuvinteFiser:
                    j = j + 1
                    cuvinteFiser.append('!=')
                    f.write('!=')
                    f.write('\n')

                elif text[i][j] == "\\":
                    f.write("' ")
                    f.write('\n')
                    f.write("\ ")
                    f.write('\n')

