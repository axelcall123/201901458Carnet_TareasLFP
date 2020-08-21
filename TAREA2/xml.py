import xml.etree.ElementTree as ET
import os
xml= ET.parse(os.path.abspath("TAREA2/dat.xml"))
archivo=xml.getroot()

for a in archivo:
    print(a.tag)
    for b in a:
        print(" ", b.tag, b.text)