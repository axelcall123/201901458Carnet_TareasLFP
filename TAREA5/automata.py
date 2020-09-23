cadena="""(
    <
        [a_s] = 45.094545123545,
        [_cadena] = "hola mundo como le va xd",
        [atributo_booleano] = true
    >,
    <
        [atributo_numerico] = 4,
        [atributo_cadena] = "adios mundo",
        [atributo_booleano] = false
    >,
    <
        [atributo_numerico] = -56.4,
        [atributo_cadena] = "este es otro ejemplo, las cadenas pueden ser muy largas",
        [atributo_booleano] = false
    >

)"""
cadenas='(<[a_B]=3.50,[dd_dd]="acd,dkdf",[d_d]=false>,'

#( ) 040 041
#< > 060 062
#[ ] 091 093
#_ 095
#, 044
#" 034
#- 045
# a-z 097 122
# 0-9 048 057
#true 1116 1114 117 101
#false 102 097 108 115 101
def automata(palabra):
    palabra=palabra+"@$#$@"
    palabrad=''
    state=-1
    SinTabAEs=palabra.replace(" ","").split()
    nueva_cadena="".join(SinTabAEs)
    nueva_cadena=nueva_cadena.lower()

    for i in range(len(nueva_cadena)):

        if state==-1:#BIENDO EL (
            if nueva_cadena[i]=="(":
                print("|T_ParenIni|.-1", nueva_cadena[i],"")
                state=0
            else:
                print("Error:-1",nueva_cadena[i],"")
                return

        elif state==0:#BIENDO EL <
            if nueva_cadena[i]=="<":
                print("|T_<>Ini|.0",nueva_cadena[i],"")
                state=1
            else:
                print("Error:0",nueva_cadena[i],"")
                return

        elif state==1:#BIENDO EL [
            if nueva_cadena[i]=="[":
                print("|T_CorIni|.1",nueva_cadena[i],"")
                state=2
            else:
                print("Error:1",nueva_cadena[i],"")
                return
            #**********************************************************************[aaa_def][_]
        elif state==2:#BINDO abc_abc
            if ord(nueva_cadena[i])>=97 and ord(nueva_cadena[i])<=122:
                state=2
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]=="_":#ABD_>>>>>>DDD
                state=3
                palabrad=palabrad+nueva_cadena[i]
            else:
                print("Error_Atri:2",nueva_cadena[i],"")
                break

        elif state==3:#BINDO abc_abc
            if ord(nueva_cadena[i])>=97 and ord(nueva_cadena[i])<=122:#BINEDO LETRAS
                state=3
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]=="]":#[ABCD_DEF]
                print("|T_Atributo|.3",palabrad,"")
                print("|T_CorFin|.3",nueva_cadena[i],"")
                palabrad=''
                state=4
            else:
                print("Error_Atri:3",nueva_cadena[i+1],i)
                break

        elif state==4:#BIENDO=
            if nueva_cadena[i]=='=':
                print("|T_igual|.4",nueva_cadena[i],"")
                if ord(nueva_cadena[i+1])>=48 and ord(nueva_cadena[i+1])<=57:#BINEDO NUMEROS
                    state=5
                elif nueva_cadena[i+1]=='"':#BINEDO PALABRAS
                    state=6
                elif ord(nueva_cadena[i+1])>=97 and ord(nueva_cadena[i+1])<=122:#BINEDO LETRAS
                    state=10
                elif nueva_cadena[i+1]=="-" or nueva_cadena[i+1]=="+":#BIENDO SI HAY UN + o -
                    state=5
                else:
                    print("Error_Atri:4.1",nueva_cadena[i],"")
                    return
            else:
                print("Error_Atri:4.2",nueva_cadena[i],"")
                return


                #**********************************************************************[12.5][D]
        elif state==5:#BIENDO #.#
            if ord(nueva_cadena[i])>=48 and ord(nueva_cadena[i])<=57:#BINEDO NUMEROS
                state=5
                palabrad=palabrad+nueva_cadena[i]

            elif nueva_cadena[i]=="-" or nueva_cadena[i]=="+":#BIENDO +-
                state=5
                palabrad=palabrad+nueva_cadena[i]
            else:
                if nueva_cadena[i]==".":#BIENDO .
                    state=5
                    palabrad=palabrad+nueva_cadena[i]
                elif nueva_cadena[i]==",":#BIENDO ,
                    state=1
                    print("|T_Numero|.5",palabrad,"")
                    print("|T_Coma|.5",nueva_cadena[i],"")
                    palabrad=''
                else:
                    print("Error_Num:6",nueva_cadena[i],"")
                    return
        #********************************************************************[abc,def]
        elif state==6:#BIENDO AAA
            if nueva_cadena[i]=='"':#BIENDO "
                print("|T_Comillas_I|",nueva_cadena[i],"")
                state=7

        elif state==7:
            if ord(nueva_cadena[i])>=97 and ord(nueva_cadena[i])<=122:
                state=7
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]==",":#BINEDO ,
                state=8
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]=='"':#BINEDO "
                print("|T_Palabra|.7",palabrad,"")
                print("|T_Comillas|.7",nueva_cadena[i],"")
                palabrad=''
                state=9
            else:
                print("Error_Num:7",nueva_cadena[i],"")
                return

        elif state==8:
            if ord(nueva_cadena[i])>=97 and ord(nueva_cadena[i])<=122:#BINEDO LETRAS
                state=8
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]=='"':#BINEDO "FIN
                print("|T_Palabra|.8",palabrad,"")
                print("|T_Comillas_F|.8",nueva_cadena[i],"")
                palabrad=''
                state=9
            else:
                print("Error_Atri:8",nueva_cadena[i],"")
                break
        elif state==9:
            if nueva_cadena[i]==',':#BIENDO,>>>> FALSE TRUE
                print("|T_Coma|.9",nueva_cadena[i],"")
                state=1
            else:
                print("Error_Atri:9",nueva_cadena[i],"")
                return
           #****************************************************

        elif state==10:
            if ord(nueva_cadena[i])>=97 and ord(nueva_cadena[i])<=122:#BINEDO LETRAS
                state=10
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]=='>':
                if palabrad=="false" or "true":
                    print("|T_VF|.10",palabrad,"")
                    print("|T_<>Fin|.10",nueva_cadena[i],"")
                    palabrad=''
                    state=11
                else:
                    print("Error_Atri:10",nueva_cadena[i],"")

        elif state==11:
            if nueva_cadena[i]==',':
                print("|T_Coma|.11",nueva_cadena[i],"")
                state=12
                if nueva_cadena[i+1]=='<':
                    print("------------------NUEVO---------------------------")
                    print("|T_CorIni|.11",nueva_cadena[i+1],i)
                    state=0

            else:
                if nueva_cadena[i]==')':
                    print("|T_ParenFin|.11", nueva_cadena[i],"")
                    state=12
                    if nueva_cadena[i:len(nueva_cadena)]==")@$#$@":
                        print("Fin")
                        return
                    else:
                        print("Error")

            #t r u e
            #f a l s e

automata(cadena)
