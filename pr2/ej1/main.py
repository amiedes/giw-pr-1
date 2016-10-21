# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:29:16 2016

@author: daniel reyes, alberto, anna
"""

import csv
import os



 
"""
Ejercicio 1.1
Usando el archivo agua_eprtr_2008_030412 crea un nuevo archivo csv denominado AguaAgrupada.cvs el cual debe contener agrupadas las empresas con el tipo de contaminación que producen. Tendrá la estructura:
Contaminación, empresa
CADMIO Y SUS COMPUESTOS, BEFESA ZINC AMOREBIETA
CADMIO Y SUS COMPUESTOS, UROLA KOSTAKO UDAL ELKARTEA
"""
def aguaAgrupada():
    os.chdir('..')
    os.chdir('emisiones_fuentes_contaminantes_csv_2008')
    src=open("agua_eprtr_2008_030412.csv")
    pointer=csv.reader(src,delimiter=";")
    content=list(pointer)
    final_content=[]
    for i in range(len(content)):
        if i==1:
            print "Contaminación,Empresa"
        else:
            final_content.append(content[i][8]+","+content[i][2])
    src.close()
    os.chdir("..")
    final_content.sort()
    for n in range(len(final_content)):
        #here i'm going to create a new file (not yet)
        print final_content[n]
    return        
             
    
# Main Function to complete Exercise 1 
def main():
   while 1:
       print " ----------------------"
       print "| Gestor de Tareas CVS |"
       print " ----------------------"
       print "Elige una Tarea:"
       print "1.- Procesar Fichero Para Agrupar Por Contaminante"
       print "2.- Titulo de Ej 1.2"
       print "3.- Titulo del Ej 1.3"
       opt=raw_input("INTRODUCE EL NUMERO DE TAREA  (para salir presiona 'q+Enter'):")
       if(opt=="1"):
            aguaAgrupada()
            break
       elif(opt=="2"):
            print "llamar func. ej 1.2 here"
       elif(opt=="3"):
            print "llamar func. ej 1.3 here"
       elif(opt=="q"):
            break

main()