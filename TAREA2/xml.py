import xml.etree.ElementTree as ET
xml = ET.parse('dat.xml')
root = xml.getroot()

print("-----OBJETO------","tipo: ", type(xml))
for a in root:
   print(a.tag)
   for d in a:
       print("      ",d.tag,":",d.text)
print("tipo de estructura: ", type(root))
