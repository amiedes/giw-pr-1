# -*- coding: utf-8 -*-
"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""
from __future__ import division
import json
import os
import re

#from semaphore import Semaphore

def findFrecuency():
    os.chdir('..')
    json_file = open('semaforos.json')
    
    data = json.load(json_file)
    semaphores_array = data['features']
    
    semaphores_dictionary = {}
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
    
        
    with open('SemaforosFrecuencia.json', 'w') as json_file:
        json.dump(semaphores_dictionary, json_file)
    json_file.close()
    
def main():
     while True:
       print "Elige una Tarea:"
       print "1.- Encontrar la frecuencia de cada semaforo "
       print "2.- Encontrar los 10 semáforos que aparecen con mayor frecuencia "
       opt=raw_input("INTRODUCE EL NUMERO DE TAREA  (para salir presiona 'q+Enter'):")
       if(opt=="1"):
            findFrecuency()
            print "\n"+"FICHERO CREADO CORRECTAMENTE (en path: '../SemaforosFrecuencia.json')"
            break
       elif(opt=="2"):
            
            break
       elif(opt=="q"):
            break
main()