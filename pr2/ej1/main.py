#-*- coding: utf-8 -*-
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
    
    #reading file
    pointer=csv.reader(src,delimiter=";")
    content=list(pointer)
    final_content=[]
 
    for i in range(len(content)):
        if i!=0:
            new_row=[]
            new_row.append(content[i][8])
            new_row.append(content[i][2])
            final_content.append(new_row)        
    src.close()
    os.chdir("..")
    
    #making groups
    final_content.sort()
    
    # writing new file    
    output=open("AguaAgrupada.csv","w")
    w_pointer=csv.writer(output,lineterminator="\n")
    for n in range(len(final_content)):
        if n == 0:
            w_pointer.writerow(["Contaminacion","empresa"])
        else:
            w_pointer.writerow (final_content[n])
    output.close()        
    return      
    
"""
2. Usando el archivo residuos_peligrosos_eprtr_2008_040412 crea un nuevo 
archivo cvs denominado FrecuenciaResiduos.cvs el cual debe contener la
frecuencia con la que aparecen las diferentes empresas.
 Tendrá la estructura:
Jugador,Frecuencia
"""
 
def frecuenciaResiduos():
    os.chdir('..')
    os.chdir('emisiones_fuentes_contaminantes_csv_2008')
    csvFileObj = open("residuos_peligrosos_eprtr_2008_040412.csv")
    lector = csv.reader(csvFileObj, delimiter=";")
    datos = list(lector)  
    empresasList = []
        
    for i in range(len(datos)):
        empresasList.append(datos[i][2])
    csvFileObj.close()
    os.chdir("..")
    empresa = ""
    claveValor = {}
    
    output=open("FrecuenciaResiduos.csv","w")
    w_pointer=csv.writer(output,lineterminator="\n")
    for k in range(len(empresasList)):
        if empresasList[k] != empresa:
            empresa = empresasList[k]
            cuantasEnLista = empresasList.count(empresa)
            claveValor[empresa] = cuantasEnLista
    i = 0
    for empresas, frecuencia in claveValor.items(): 
        if i == 0:
            w_pointer.writerow(["Empresa","frecuencia"])
        else:
            w_pointer.writerow ([empresas, str(frecuencia)])
        i = i + 1
    output.close()
    return

  
# Main Function to complete Exercise 1 
def main():
   while True:
       print " ----------------------"+"\n"+"| Gestor de Tareas CSV |"+"\n"+" ----------------------"
       print "Elige una Tarea:"
       print "1.- Generar Fichero --> 'AguaAgrupada.csv' "
       print "2.- Generar Fichero --> 'Frecuencia Residuos.csv'"
       print "3.- Titulo del Ej 1.3"
       opt=raw_input("INTRODUCE EL NUMERO DE TAREA  (para salir presiona 'q+Enter'):")
       if(opt=="1"):
            aguaAgrupada()
            print "\n"+"FICHERO CREADO CORRECTAMENTE (en path: '../AguaAgrupada.csv')"
            break
       elif(opt=="2"):
            frecuenciaResiduos()
            print "\n"+"FICHERO CREADO CORRECTAMENTE (en path: '../FrecuenciaResiduos.csv')"
            break
       elif(opt=="3"):
            print "llamar func. ej 1.3 here"
       elif(opt=="q"):
            break

main()