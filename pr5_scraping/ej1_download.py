# -*- coding: utf-8 -*-
"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes

"""

import urllib
import os
import shutil
from BeautifulSoup import *


#-------------------- Utils --------------------

# This Function bulid a new directory and write
# a new file with every image found in url(blog's entry)
# into it
  
def save_images(url,num_dir):
    dir_name='Entrada_'+str(num_dir)
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html)
    image_tags=soup('a',{"imageanchor":"1"})
    num_image=1
    
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
        os.mkdir(dir_name)
    else:
        os.mkdir(dir_name)
    os.chdir(dir_name)

    for tag in image_tags:
            image_target=open(dir_name+"_" \
                              +str(num_image)+".jpg","wb")            
            image_src=urllib.urlopen(tag.get('href',None))
            while True:
                    info = image_src.read(100000)
                    if len(info) < 1 : 
                        break
                    image_target.write(info)
            image_target.close()
            num_image=num_image+1
    
    os.chdir('..')
    
    
# This Function extract all tags(href)= blog's entry 
# of year 2016 from blog, and download images calling 
# save_images function
  
def download_images(url):
    html=urllib.urlopen(url)
    soup=BeautifulSoup(html)          
    num_dir=1
    active_tags=soup.findAll('a',{'class':'post-count-link' \
                             ,'href':True})
    for tag in active_tags:
     if tag.text=='2015':
        break
     else:
        tag["my_search"]="year16" 

    year16_tags=soup.findAll('a',{'class':'post-count-link' \
                          ,'href':True,'my_search':True})
    
    for tag in year16_tags:
     if tag.text=='2016':
        continue
     else:
        save_images(tag['href'],num_dir)
        num_dir=num_dir+1
