p_uno='__servidor1'
p_dos='3servidor'
p_tres='_____a2'
#ascii numero(1-9)=48-57
#ascii numero(a-z)=97-122
#ascii _=95
#print(ord(p_dos[0]))

def automata(palabra):
    state=0
    for i in range(len(palabra)):
        if state==0:
            if ord(palabra[i])>=97 and ord(palabra[i])<=122:#LETRAS
                state=2
                #print('Al Estado 2')
            elif ord(palabra[i])==95:#guion
                state=1
                #print('Al Estado 1')
            else:
                print('Error: 0', ';;pos: ', i)
                return
        elif state==1:
            if ord(palabra[i])==95:
                state=1
                #print('Al Estado 1')
            elif ord(palabra[i])>=97 and ord(palabra[i])<=122:
                state=3
                #print('Al Estado 3')
            else:
                print('Erro: 1', ';;pos: ', i)
                return
        elif state==2:
            if ord(palabra[i])>=97 and ord(palabra[i])<=122:
                state=2
                #print('Al Estado 2')
            elif ord(palabra[i])>=48 and ord(palabra[i])<=57:
                state=4
                print('OK, cadena correcta')
                #print('Al Estado 4')
            else:
                print('Error: 2', ';;pos: ', i)
                return
        elif state==3:
            if ord(palabra[i])>=48 and ord(palabra[i])<=57:
                state=4
                print('OK, cadena correcta')
                #print('Al Estado 4')
            else:
               print('Error: 3', ';;pos: ', i)
               return
        elif state==4:
                print("XD")
            

automata(p_uno)
automata(p_dos)
automata(p_tres)