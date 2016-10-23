# -*- coding: utf-8 -*-

import json
import os
import re
#from semaphore import Semaphore

os.chdir('..')
json_file = open('semaforos.json')
os.chdir('ej2')

data = json.load(json_file)
semaphores_array = data['features']

print "Semaphores array has " + str(len(semaphores_array)) + " elements"

#ania: creo que deberiamos sacar informacion sobre la ubicacion de cada semaforo.. 
#pero es que cada semaforo tiene distinto ubicacion pues no hay ningun semaforo 
#con mayor frecuencia que los otros... o posiblemente no entendi bien el ejercicio
semaphores_dictionary = {}
for semaphore in semaphores_array:
        semaphoreDescription = semaphore['properties']['Description']
        ubicacion = re.search('n:</b>(.+?)<br />', semaphoreDescription) #try to find a substring with ubicacion in string with description
        if ubicacion:
            foundUbicacion = ubicacion.group(1)
        print foundUbicacion

"""alberto
for semaphore in semaphores_array:
    s = Semaphore(semaphore['geometry']['coordinates'][0], semaphore['geometry']['coordinates'][1])
    #coordinates_tuple = (semaphore['geometry']['coordinates'][0], semaphore['geometry']['coordinates'][1])
    #print coordinates_tuple
    if (s in semaphores_dictionary):
        semaphores_dictionary[s] += 1
    else:
        semaphores_dictionary[s] = 1
    #print "-"*30 + "\n"

print "\n\n" + "=" * 40 + "\n\n"

for key in semaphores_dictionary:
    print key
    print "\t" + str(semaphores_dictionary[key])

print "Semaphores dictionary has " + str(len(semaphores_dictionary.keys())) + " elements."

alberto"""
