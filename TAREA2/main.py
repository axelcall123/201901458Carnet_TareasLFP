import csv
import os
import json
import xml.etree.ElementTree as ET

import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path_1 = os.path.join(my_path, "../TAREA2/names.csv")
path_2 = os.path.join(my_path, "../TAREA2/dat.json")
path_3 = os.path.join(my_path, "../TAREA2/dat.xml")

with open(path_1) as file:
    csvss = csv.reader(file)
    print(file)
    for reg in csvss:
        print(reg[0], reg[1], reg[2], reg[3])
print("tipo: ", type(csvss))

print("------------------------------")
def readJson():
    file=open(path_2)
    data=json.load(file)
    file.close()
    print(data)
    print(type(data))
    return(data)

dict=readJson()
for i in dict:
    print(i)

print("------------------------------")
xml= ET.parse(path_3)
archivo=xml.getroot()

for a in archivo:
    print(a.tag)
    for b in a:
        print(" ", b.tag, b.text)
print(type(archivo))


