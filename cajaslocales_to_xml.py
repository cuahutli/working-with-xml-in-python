import xml.etree.ElementTree as ET
from xml.dom import minidom
import psycopg2
import psycopg2.extras

def get_data():
    query = """
select 
	so.caja_local
	, coalesce(cl.nombre, 'SIN NOMBRE') as nombre_caja
	, count(so.caja_local)  as total_socios
	, count(so.sexo_soc) filter (where so.sexo_soc = 'F') as mujeres
	, count(so.sexo_soc) filter (where so.sexo_soc = 'M') as hombres
	, count(so.clave_tper) filter (where so.clave_tper = 6 ) as morales
from 
	socio so
	inner join ctascap ct on ct.clave_suc = so.clave_suc and ct.clave_soc = so.clave_soc and ct.clave_tins = 1 and ct.sdo_total_ccap = 510
	left join cajaloc cl on cl.clave = so.caja_local
group by
	so.caja_local
	, cl.nombre
order by
	so.caja_local
    """
    con = psycopg2.connect(host ="localhost", database ="o_samao", port = "5432", user = "admon_samao", password = "cstaim")
    cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(query)
    resultado = cursor.fetchall()
    columnas = [desc[0] for desc in cursor.description]
    info = {
        'data': resultado,
        'columnas': columnas        
    }
    return info

def prettify(data): 
    raw_data = ET.tostring(data, 'utf-8')
    print(raw_data)
    reparsed = minidom.parseString(raw_data)
    return reparsed.toprettyxml(indent="    ")

def crea_xml(datos):
    root = ET.Element("caja_samao")
    for dato in datos['data']:
        caja = ET.SubElement(root, 'caja_local')
        caja.set("id", str(dato['caja_local']))
        caja.set("nombre", dato['nombre_caja'])
        caja.set("nombre_corto", dato['nombre_caja'].split('(')[0].strip())
        caja.set("nombre_con_formato", dato['nombre_caja'].split('(')[0].strip().replace(" ", "_"))
        for col in datos['columnas'][2:]:
            info = ET.SubElement(caja, col)
            info.text = str(dato[col])
    
    return root

def write_xml(xmlString):
    mydata = prettify(xmlString)
    myfile = open("info_cajas_locales.xml", "w")
    myfile.write(mydata)

if __name__ == '__main__':
    datos = get_data()
    xmlstring = crea_xml(datos)
    write_xml(xmlstring)