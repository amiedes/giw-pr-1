# -*- coding: utf-8 -*-

import json
import os
from semaphore import Semaphore

os.chdir('..')
json_file = open('semaforos.json')
os.chdir('ej2')

data = json.load(json_file)
semaphores_array = data['features']

print "Semaphores array has " + str(len(semaphores_array)) + " elements"
semaphores_dictionary = {}

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
