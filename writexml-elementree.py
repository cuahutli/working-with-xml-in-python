import xml.etree.ElementTree as ET
from xml.dom import minidom

def prettify(data):
    raw_data = ET.tostring(data, 'utf-8')
    reparsed = minidom.parseString(raw_data)
    return reparsed.toprettyxml(indent="    ")


data = ET.Element('data')
items = ET.SubElement(data, 'items')

item1 = ET.SubElement(items, 'item')
item1.set('name', 'item1')
item1.text = 'Data del item 1'

item2 = ET.SubElement(items, 'item')
item2.set('name', 'item2')
item2.text = 'Data del item 2'


#mydata = ET.tostring(data)
mydata = prettify(data)
#myfile = open("sample2.xml", "wb")
myfile = open("sample2.xml", "w")
myfile.write(mydata)

