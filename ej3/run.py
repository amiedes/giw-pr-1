# -*- coding: utf-8 -*-
# Implementar un programa en Python tal que tomando como entrada el nombre de un
# archivo de texto, analice el contenido y escriba otro archivo de salida que
# contenga el número de veces que aparece cada palabra.

import utils

# Pedir el nombre del fichero
filename = raw_input("Nombre del fichero: ")

# process file
utils.process_file(filename)
