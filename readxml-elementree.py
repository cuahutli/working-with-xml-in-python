import xml.etree.ElementTree as ET

xmldoc = ET.parse('sample.xml')
root = xmldoc.getroot()

print("numero de elementos")
print(len(root[0]))

print("Atributo del Item # 2")
print(root[0][1].attrib['name'])

print("Todos los atributos")
for elem in root:
    for subelem in elem:
        print(subelem.attrib['name'])


print("Datos del item 2")
print(root[0][1].text)



print("todos los datos de los items")
for elem in root:
    for subelem in elem:
        print(subelem.text)