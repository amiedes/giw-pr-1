#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

# parses XML file into a list of 'monument' objects
def parse_xml(filename):
    monuments = []
    print "Parsing XML file..."
    # TODO: parse XML file

    return monuments

# returns True if string is a valid monument ID, otherwise returns False
def valid_id(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def main():
    print "Booting up..."

    monuments = parse_xml("MonumentosZaragoza.xml")
    print monuments

    exit = False

    while(!exit):
        # ask for monument in the list
        monument_id = None
        while(!valid_id(monument_id)):
            monument_id = raw_input("Elige un monumento (ID):"))

        # get monument info and print
        monument = monuments[monument_id]
        monument.set_description()
        monument.set_geolocation()
        print monument

        # continue asking for monuments?
        option = None
        while (option != 's' and option != 'n'):
            option = raw_input("¿Desea buscar otro monumento? (s/n)")
            if option == 'n': exit = True

main()
