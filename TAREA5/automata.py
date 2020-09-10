cadena="""(
    <
        [atributo_numerico] = 45.09,
        [atributo_cadena] = "hola mundo",
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
#( ) 040 041
#< > 060 062
#[ ] 091 093
#, 044
#" 034
#- 045
# a-z 097 122
# 0-9 048 057
#true 1116 1114 117 101
#false 102 097 108 115 101
def Estado2(Atributo):
    print(Atributo, type(Atributo))

def automata(palabra):
    state=-1
    SinTabAEs=palabra.replace(" ","").split()
    nueva_cadena="".join(SinTabAEs)
    nueva_cadena=nueva_cadena.lower()
    print(type(nueva_cadena))
    for i in range(len(nueva_cadena)):

        if state==-1:#BIENDO EL (
            if ord(nueva_cadena[i])==40:
                print("1T_ParenIni |"+ nueva_cadena[i]))
                state=0
            else:
                print("Error:-1")

        if state==0:#BIENDO EL <
            if ord(nueva_cadena[i])==60:
                print("|T_<>Ini|",nueva_cadena[i]))
                state=1
            else:
                print("Error:0")

        if state==1:#BIENDO EL [
            if ord(nueva_cadena[i])==91:
                print("|T_CorIni|",nueva_cadena[i]))
                state=2
            else:
                print("Error:1")
        if state==2:
            Estado2(nueva_cadena[i+1:len(nueva_cadena)-1])
            break
        
automata(cadena)   