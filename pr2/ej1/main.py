#-*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:29:16 2016

@author: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

import csv
import os 
import operator

#This function changes format "number,number" to float
def to_float(word):
    partition=word.split(',')
    new_word=word
    if word=="":
        new_word="0.0"
    if len(partition)>1:
        new_word=partition[0]+'.'+partition[1]
    my_float=float(new_word)
    return my_float

"""---------------------------------------------------
Ejercicio 1.1
Usando el archivo agua_eprtr_2008_030412 crea un nuevo
archivo csv denominado AguaAgrupada.cvs el cual debe 
contener agrupadas las empresas con el tipo de contaminación
que producen. Tendrá la estructura:
Contaminación, empresa
CADMIO Y SUS COMPUESTOS, BEFESA ZINC AMOREBIETA
CADMIO Y SUS COMPUESTOS, UROLA KOSTAKO UDAL ELKARTEA
"""
def aguaAgrupada():
    os.chdir('..')
    os.chdir('emisiones_fuentes_contaminantes_csv_2008')
    src=open("agua_eprtr_2008_030412.csv")
    
    #reading source file and capture data
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

    
"""------------------------------------------------------
Ejercicio 1.2
Usando el archivo residuos_peligrosos_eprtr_2008_040412 crea un nuevo 
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

    
"""-------------------------------------------------------
Ejercicio. 1.3
Usando el archivo aire_eprtr_2008_030412 crea un
nuevo archivo cvs denominado Contaminantes.cvs el cual
tenga la información de las 10 empresas que más contaminan.
Para ello se debe sumar la cantidad Kg/año de los residuos
emitidos por la empresa.
"""    
def contaminantes():
    #reading the source file and capture data
    os.chdir('..')
    os.chdir('emisiones_fuentes_contaminantes_csv_2008')
    src=open("aire_eprtr_2008_030412.csv") 
    pointer=csv.reader(src,delimiter=";")
    content=list(pointer)
    quantities=dict()
    
    for i in range(len(content)):
        if i>=2:
            current=content[i][2]
            if (current in quantities):
                quantities[current]+=to_float(content[i][10])
            else:
                quantities[current]=to_float(content[i][10])
        else:
            continue
    src.close()
    
    #Max to Min order the{'empresa':'Suma Kg/año'}Dictionary 
    order_quantities=sorted(quantities.items(), key=operator.itemgetter(1))    
    order_quantities.reverse()        
    
    #writing the new file
    os.chdir('..')
    output=open("Contaminantes.csv","w")
    w_pointer=csv.writer(output,lineterminator="\n")
    w_pointer.writerow(["Empresas","Residuos"])
    for n in range(10):
            new_row=[order_quantities[n][0],str(order_quantities[n][1])]
            w_pointer.writerow(new_row)
    output.close()        
    return
    
    
#---------------------------------------------------------  
# Main Function to complete Exercise 1 
def main():
   while True:
       print " ----------------------"+"\n"+"| Gestor de Tareas CSV |"+"\n"+" ----------------------"
       print "Elige una Tarea:"
       print "1.- Generar Fichero --> 'AguaAgrupada.csv' "
       print "2.- Generar Fichero --> 'Frecuencia Residuos.csv' "
       print "3.- Generar Fichero --> 'Contaminantes.csv' "
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
            contaminantes()
            print "\n"+"FICHERO CREADO CORRECTAMENTE (en path: '../Contaminantes.csv')"
            break
       elif(opt=="q"):
            break

main()