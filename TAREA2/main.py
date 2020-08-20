import csv
with open('names.csv') as file:
    csvss = csv.reader(file)
    print(file)
    for reg in csvss:
        print(reg[0], reg[1], reg[2], reg[3])
print("tipo: ", type(csvss))
#------------------------
print("")

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
#-----------------
print("")

import xml.etree.ElementTree as ET
xml = ET.parse('dat.xml')
root = xml.getroot()

print("-----OBJETO------","tipo: ", type(xml))
for a in root:
   print(a.tag)
   for d in a:
       print("      ",d.tag,":",d.text)
print("tipo de estructura: ", type(root))
