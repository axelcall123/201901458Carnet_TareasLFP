import json
with open('dat.json','r') as miarchivo:
    datos=miarchivo.read()
objeto=json.loads(datos)
#for i in objeto['nombre']:
print("-----OBJETO------","tipo: ", type(objeto))
print(objeto)
print("")
for i in objeto:
    print("atributos:", i)
    for a in objeto[i]:
        print("     ",a)
    #print(i)
#print("------------------------------")
#def readJson():
#    file=open('dat.json')
#    data=json.load(file)
#    file.close()
#    print(data)

#dic=readJson()
#for e in dic:
#    print(e)
