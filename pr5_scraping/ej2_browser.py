# -*- coding: utf-8 -*-
"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes

"""

import urllib
from BeautifulSoup import *


#-------------------- Utils --------------------

def found_phrase(url,phrase):
    html=urllib.urlopen(url)
    soup=BeautifulSoup(html)
    body=soup.body.text
    phrase=phrase.strip()
    phrase=phrase.decode('utf8')
    if phrase in body:
        return True
    else:
        return False
        
def browse(url,phrase):
    results=list()
    html=urllib.urlopen(url)
    soup=BeautifulSoup(html)          
    blog_entries=soup.findAll('a',{'class':'post-count-link' \
                         ,'href':True})
    i=1   
    print     ' ---------------------------' \
        +'\n'+'| Loading.....Please Wait.. |' \
        +'\n'+' ---------------------------'  
    for tag in blog_entries:         
        if(found_phrase(tag['href'],phrase)
            and('201' not in tag.text)):
            results.append(tag['href'])
        else:
            continue

    print '--- RESULTS: ---'
    if(len(results)<1):
        print '----- No Results Found- Good Bye!! -----'
        return
        
    for res in results:
        print str(i)+') \n',res,'\n\n'
        i=i+1
    return    