# -*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes

Todos los Outputs se generan el el Dir que contiene 
las carpetas ej1 y ej2
"""

from __future__ import division
import json
import os
import re
import operator

#This function is necesary because we have spanish 
#characters in "ubicacion"
def encode(text):
    return text.encode('utf-8')
    
#this function build a dictionary like {ubicacion:frecuencia}
# where frecuencia= NumSemaforos(en ubicacion)/NumTotal 
def findDictionary():
    os.chdir('..')
    json_file = open('semaforos.txt')
    
    data = json.load(json_file)
    semaphores_array = data['features']
    
    semaphores_dictionary = dict()
    totalSemaphoreNumber = 0
    for semaphore in semaphores_array:
        
        semaphoreDescription = semaphore['properties']['Description']
        ubicacion = re.search('n:</b> (.+?)<br />', semaphoreDescription) #try to find a substring with ubicacion in string with description
        if ubicacion:
            foundUbicacion = ubicacion.group(1)
            
        num_semaforos = re.search('foros:</b> (.+?)<br />', semaphoreDescription) #try to find a substring with number of semaphores in string with description
        if num_semaforos:
            found_num_semaforos = num_semaforos.group(1)
        semaphores_dictionary[foundUbicacion]=found_num_semaforos #dictionary with ubicacion as key and corresponding number of semaphores as value
    
        totalSemaphoreNumber = totalSemaphoreNumber + int(found_num_semaforos)
    
    #change number of semaphores as value into frecuency
    for ubicacion, numOfSemaphores in semaphores_dictionary.items():
        frecuency = int(numOfSemaphores) / float(totalSemaphoreNumber)
        semaphores_dictionary[ubicacion] = frecuency
    
    return semaphores_dictionary

    
#This function Solve Exercise 2.1    
def findFrecuency():
    semaphores_dictionary = dict()
    semaphores_dictionary = findDictionary()
    with open('SemaforosFrecuencia.json', 'w') as json_file:
        json.dump(semaphores_dictionary, json_file)
    json_file.close()
    print "\n"+"FICHERO CREADO CORRECTAMENTE (en path: '../SemaforosFrecuencia.json')"


#This function Solve Exercise 2.2        
def find10Frecuencies():
    semaphores_dictionary = dict()
    semaphores_dictionary = findDictionary()
    for ubicacion, frecuencia in semaphores_dictionary.items():
        semaphores_dictionary[ubicacion] = frecuencia
    orderedDict = sorted(semaphores_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    
    with open('FrecuenciaOrdenada.txt', 'w') as f:
        for n in range(10):              
            f.write('%s:%s\n' % (orderedDict[n][0].encode('utf8') , orderedDict[n][1]))                        
    print "\n"+"FICHERO CREADO CORRECTAMENTE (en path: '../FrecuenciaOrdenada.txt')"    
        

#-------------------------------------------------------
# Main Function to complete Exercise 2 
def main():

    while True:
       print " ----------------------"+"\n"+"| Gestor de Tareas JSON |"+"\n"+" ----------------------"
       print "Elige una Tarea:"
       print "1.- Encontrar la frecuencia de cada semaforo "
       print "2.- Encontrar los 10 semáforos que aparecen con mayor frecuencia "
       opt=raw_input("INTRODUCE EL NUMERO DE TAREA  (para salir presiona 'q+Enter'):")
       if(opt=="1"):
            findFrecuency()
            break
       elif(opt=="2"):
            find10Frecuencies()
            break
       elif(opt=="q"):
            break
main()