#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

from xml.etree import ElementTree
from monument import Monument

# parses XML file into a list of 'monument' objects
def parse_xml():
    monuments = []
    fh = open("MonumentosZaragoza.xml", "rt")
    tree = ElementTree.parse(fh)

    for punto_interes in tree.iterfind("Feature"):

        for info in punto_interes:
            field_name = info.get("name")
            if   field_name == "nombre":
                nombre = info.text
            elif field_name == "url":
                url = info.text
            elif field_name == "posicion_x":
                posicion_x = info.text
            elif field_name == "posicion_y":
                posicion_y = info.text
        monument = Monument(nombre, url, posicion_x, posicion_y)
        monuments.append(monument)

    return monuments

# returns True if string is a valid monument ID, otherwise returns False
def valid_id(s):
    if (s == None): return False
    try:
        int(s)
        return True
    except ValueError:
        return False

def main():
    monuments = parse_xml()

    for monument in monuments:
        print str(monument.id) + ".- " + monument.name

    exit = False
    while(not exit):
        # ask for monument in the list
        monument_id = None
        while(not valid_id(monument_id)):
            monument_id = raw_input("\nElige un monumento (ID): ")

        # get monument info and print
        monument = monuments[int(monument_id)-1]
        monument.set_description()
        monument.set_geolocation()
        print monument.to_printable()

        # continue asking for monuments?
        option = None
        while (option != 's' and option != 'n'):
            option = raw_input("\n¿Desea buscar otro monumento? (s/n): ")
            if option == 'n': exit = True

main()
