import json
import webbrowser
import os.path
my_path = os.path.abspath(os.path.dirname(__file__))
path_1 = os.path.join(my_path, "../Json-Reporte-html/data1.json")


with open(path_1,'r') as miarchivo:
    datos=miarchivo.read()
objeto=json.loads(datos)

atributos=[]#NOMBRE,PROEMDIO
caracteristicas=[]#AXEL,95
nombre=[]
edad=[]
activo=[]
saldo=[]

for i in objeto:
    items=i.items()
    for id_item in items:
        atributos.append(id_item[0]), caracteristicas.append(id_item[1])#OBTIENE NOMBRE:"ALEX"

#print('atributos ',atributos)
#print('caracteristicas ',caracteristicas)

def html():
    texto=''
    DiContI="""
        <div class="container">
            <div class="row">
    """
    DiCe="""</div>"""

    Di12I="""
                <div class="col-md-12" >
    """
    Di4I="""
                <div class="col-md-3" class="divs">
    """
    HR='<hr>'

    body=''
    print()
    for a in range(len(atributos)):
        if str(atributos[a])=='nombre':
            nombre.append(caracteristicas[a])
        elif str(atributos[a])=='edad':
            edad.append(caracteristicas[a])
        elif str(atributos[a])=='activo':
            activo.append(caracteristicas[a])
        elif str(atributos[a])=='saldo':
            saldo.append(caracteristicas[a])
    for ids in range(len(nombre)):
                  #DiContI       +Di12I+'REPORTE#'+str(numero+1)+DiCe    +Di4I+str(atri[0]).upper()+HR+str(carac[0])+DiCe+ Di4I+str(atri[1]).upper()+HR+str(carac[1])+DiCe+ Di4I+str(atri[2]).upper()+HR+str(carac[2])+DiCe+ Di4I+str(atri[3]).upper()+HR+str(carac[3])+DiCe+   DiCe+DiCe
        body=body+DiContI       +Di12I+'REPORTE#'+str(ids+1)+DiCe                   +Di4I+'NOMBRE'+HR+str(nombre[ids])+DiCe+ Di4I+'EDAD'+HR+str(edad[ids])+DiCe+ Di4I+'ACTIVO'+HR+str(activo[ids])+DiCe+Di4I+ 'SALDO'+HR+str(saldo[ids])+DiCe+   DiCe+DiCe
    return body

#for id in range(int(sep_palabras_coma[0])):
 #   cuerpo=cuerpo+html(id)
  #  print(id)

f = open('holamundo.html','w')#nombre documento pagina web
principal = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="css/css.css">
    <title>Document</title>
</head><body>"""
f = open('hiworld.html','w')#nombre documento pagina web
principal = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="boos/bootstrap.css">
    <link rel="stylesheet" href="css/css.css">
    <title>Document</title>
</head><body>"""
cuerpos=html()
fin= """
</body>
<script src="boos/bootstrap.js"></script>
</html>"""
f.write(principal)#inicio
f.write(cuerpos)#medio
f.write(fin)#final
f.close()#cerar
webbrowser.open_new_tab('hiworld.html')#generar