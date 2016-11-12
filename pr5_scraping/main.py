#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""
from ej1_download import download_images

def main():
 while True:
   print       " --------------" \
         +"\n"+"| Web Scraping |"\
         +"\n"+" --------------" 
   
   print "Elige una Tarea:"
   print "1.- Download 2016 Images "
   print "2.- Search"
   opt=raw_input("INTRODUCE EL NUMERO DE TAREA"  \
                 +"(para salir presiona 'q+Enter'):")
   if(opt=="1"):
        url='http://trenesytiempos.blogspot.com.es/'
        print "\n Working.... Please Wait...\n"
        download_images(url)
        print "OK-All your images ready..!!!"
        break
   elif(opt=="2"):
        print "Ejercicio2_not Yet"
        break
   elif(opt=="q"):
        break 
  
main()
