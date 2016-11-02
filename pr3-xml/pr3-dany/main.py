#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 15:37:05 2016

@author: dany
"""
import urllib
from xml.etree import ElementTree


def generateList():
    pointer=open("MonumentosZaragoza.xml","rt")
    tree=ElementTree.parse(pointer)
    i=1
    data= dict()
    for node in tree.iter("PropertyValue"):
        name=node.attrib.get("name")
        if(name=="nombre"):
            values=list()
            values.append(node.text)
        elif(name=="url"):
            values.append(node.text)
            data[i]=values
            i=i+1                 
    return data
    
def parse_description(description):
    new_data=description.split("<p>")
    to_print=""
    for i in range(len(new_data)):
        if(i==0 or "<a" in new_data[i] or "<span" in new_data[i]):
            continue
        elif("<h3>" in new_data[i] or "div>" in new_data[i] or "<strong>" in new_data[i]):
           new_data[i]=new_data[i].replace("<h3>","")
           new_data[i]=new_data[i].replace("</h3>",":")
           new_data[i]=new_data[i].replace("<div>","")
           new_data[i]=new_data[i].replace("</div>","\n\n")
           new_data[i]=new_data[i].replace("<strong>","")
           new_data[i]=new_data[i].replace("</strong>","")
           to_print=to_print+new_data[i]+"\n"
        else:
           to_print=to_print+new_data[i]+"\n"
    return to_print
    
def get_description(url):
    web_content=urllib.urlopen(url)
    data=web_content.read()
    initial_pos=data.find("<h3>Descripc")
    final_pos=data.find("<h3>Enlaces</h3>")
    description=data[initial_pos:final_pos]
    description=description.replace("</p>","")
    description=description.decode('latin-1')
    final_description= parse_description(description)
    return final_description


def get_position(name):
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
    monumento=name.encode('utf8')
    url = serviceurl + urllib.urlencode({'address': monumento,'components':'country:ES'})
    uh= urllib.urlopen(url)
    data = uh.read()
    position=dict()
    tree=ElementTree.fromstring(data)
    for node in tree.iter():
        if(node.tag == "lat"):
          position["lat"]=node.text
        elif(node.tag=="lng"):
          position["lng"]=node.text
        else:
            continue
    return position
    
    
def main():
   
   while True:
       print "\n ---------------------"+"\n"+"| Visita un Monumento |"+"\n"+" ---------------------"
       print "      Elige Uno:\n"
       
       monuments=generateList()
       for i in range(len(monuments)):
           i=i+1
           print i,":", monuments[i][0]
       size= len(monuments)
       
       opt=raw_input("Escoge El Numero de Monumento a Consultar:(para salir presiona '0+Enter'):")
       try:
           opt=int(opt)
       except:
           opt=-1
       
       if(opt<=size and opt>0):
            selected_name=monuments[opt][0]
            selected_url=monuments[opt][1]
            print "\n\nNOMBRE: ",selected_name,"\n" 
            position=get_position(selected_name)
            print "LATITUD: ",position["lat"],"         LONGITUD:",position["lng"],"\n"
            print "PAGINA WEB: \n", selected_url,"\n"
            print "DESCRIPCION:"
            description=get_description(selected_url)
            print description,"\n"
            redo=raw_input("Quieres consultar otro Monumento??(y/n):")
            if(redo=="y"):
                continue
            else:
                break
       elif(opt==0):
            break
       else:
           print "\n ERROR: Introduce un numero valido \n"
main()
