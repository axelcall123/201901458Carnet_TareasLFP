import csv
import os
import json
import xml.etree.ElementTree as ET

with open(os.path.abspath("TAREA2/names.csv")) as file:
    csvss = csv.reader(file)
    #print(file)
    for reg in csvss:
        print(reg[0], reg[1], reg[2], reg[3])
print("tipo: ", type(csvss))

print("------------------------------")
def readJson():
    file=open(os.path.abspath("TAREA2/dat.json"))
    data=json.load(file)
    file.close()
    print(data)
    print(type(data))
    return(data)

dict=readJson()
for i in dict:
    print(i)

print("------------------------------")
xml= ET.parse(os.path.abspath("TAREA2/dat.xml"))
archivo=xml.getroot()

for a in archivo:
    print(a.tag)
    for b in a:
        print(" ", b.tag, b.text)
print(type(archivo))


