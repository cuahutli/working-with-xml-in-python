from xml.dom import minidom

xmldoc = minidom.parse('sample.xml')
items = xmldoc.getElementsByTagName('item')

print("numero de items")
print(len(items))

print("Atributo del Item # 2")
print(items[1].attributes['name'].value)

print("Todos los atributos")
for elem in items:
    print(elem.attributes['name'].value)


print("Datos del item 2")
print(items[1].firstChild.data)
print(items[1].childNodes[0].data)


print("todos los datos de los items")
for elem in items:
    print(elem.firstChild.data)