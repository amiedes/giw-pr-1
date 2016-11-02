#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

import urllib
import re
import xml.etree.ElementTree as ET
from html_tag_cleaner import HtmlTagCleaner

class Monument:
    next_id = 1

    def __init__(self, name, website, x_pos, y_pos):
        self.id = Monument.next_id
        Monument.next_id += 1
        self.name = name
        self.description = None
        self.website = website
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.latitude = None
        self.longitude = None

    @property
    def id(self):
        return self.id

    @property
    def name(self):
        return self.name

    @property
    def website(self):
        return self.website

    @property
    def x_pos(self):
        return self.x_pos

    @property
    def y_pos(self):
        return self.y_pos

    @property
    def description(self):
        return self.description

    @property
    def geolocation(self):
        return self.geolocation

    def set_description(self):
        if self.description is None:
            # make API call
            web_content = urllib.urlopen(self.website)
            data = web_content.read().decode('latin-1')
            # find the description inside the response
            matches = re.search('\<h3\>Descripci.n\<\/h3\>(.|\n)*\<h3\>Enlaces\<\/h3\>', data)
            if matches == None:
                self.description = '(!!) Website description did not match standard structure'
            else:
                dirty_description = matches.group(0)
                self.description = HtmlTagCleaner.clean(dirty_description)

    def set_geolocation(self):
        if (self.latitude is None) or (self.longitude is None):
            # prepare API call
            serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
            url = serviceurl + urllib.urlencode({
                'address': self.name.encode('utf-8'),
                'components': 'country:ES|administrative_area:Zaragoza'
            })
            # make API call and retrieve data
            uh = urllib.urlopen(url)
            data = uh.read()
            # extract latitude and longitude from XML response
            root = ET.fromstring(data)
            location = root.find('result').find('geometry').find('location')
            self.latitude = location.find('lat').text
            self.longitude = location.find('lng').text

    def __str__(self):
        ret = ""
        ret += "Id: " + str(self.id) + "\n"
        ret += "Name: " + self.name + "\n"
        ret += "Description: " + self.description + "\n"
        ret += "Website: " + self.website + "\n"
        ret += "x-pos: " + self.x_pos + "\n"
        ret += "y-pos: " + self.y_pos + "\n"
        ret += "latitude: " + self.latitude + "\n"
        ret += "longitude: " + self.longitude

        return ret.encode('utf8')

    def to_printable(self):
        ret = ""
        ret += "Nombre monumento: " + self.name + "\n"
        ret += "Latitud: " + self.latitude + "  "
        ret += "Longitud: " + self.longitude + "\n"
        ret += "Web asociada: " + self.website + "\n"
        ret += "Descripcion:" + self.description

        return ret.encode('utf-8')
