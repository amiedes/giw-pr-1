#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""
from ej1_download import download_images
from ej2_browser import browse

def main():
 url='http://trenesytiempos.blogspot.com.es/'   
 while True:
   print       " --------------" \
         +"\n"+"| Web Scraping |"\
         +"\n"+" --------------" 
   
   print "Choose A Task:"
   print "1.- Download 2016 Images "
   print "2.- Search Words"
   opt=raw_input("WRITE YOUR TASK NUMBER"  \
                 +"(To Exit press 'q+Enter'):")
   if(opt=="1"):
        print "\n Working.... Please Wait...\n"
        download_images(url)
        print "OK-All your images ready..!!!"
        break
   elif(opt=="2"):
        phrase=""
        phrase=raw_input("Words to Search ? :")
        browse(url,phrase)
        break
   elif(opt=="q"):
        break 
  
main()
