import os
import json
import xml.etree.ElementTree as ET

# JSON

nom_archivo = "Franco.json"

datos_json = {
    "nombre": "Andres Franco",
    "edad": 17,
    "cumple": 2008,
    "lenguaje": "python"
}

# .dump es para convertir de python a json

with open(nom_archivo, "w") as file:
    json.dump(datos_json, file, indent=4)
with open(nom_archivo, "r") as file:
    for line in file.readlines():
        print(datos_json)

# borra el archivo JSON (igual que con .txt)

os.remove(nom_archivo)  

# XML

nom_archivo1 = "Franco.xml"

datos_xml = {
    "nombre": "Andres Franco",
    "edad": 17,
    "cumple": 2008,
    "lenguaje": "python"
}

def crear_xml():
    # Root es la etiqueta principal y child serian los "hijos"
    root = ET.Element("datos_xml")
    for key, value in datos_xml.items():
        child = ET.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                ET.SubElement(child, "item").text = str(item)
        else:
            child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(nom_archivo1, encoding="utf-8", xml_declaration=True)

crear_xml()

with open(nom_archivo1, "r", encoding="utf-8") as file:
    print(file.read())

os.remove(nom_archivo1)  
