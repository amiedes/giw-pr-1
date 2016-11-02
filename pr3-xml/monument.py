#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

import urllib
import xml.etree.ElementTree as ET

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
            print "Making API call to get monument description..."
            # TODO: make call to Zaragoza's City Council's API
            #contenido = urllib.urlopen("http://www.zaragoza.es/ciudad/vistasciudad/detalle_Monumento?id=" + str(self.id)) 
            #print contenido.encode('utf8')
            
        else:
            print "Description is already set"

    def set_geolocation(self):
        if (self.latitude is None) or (self.longitude is None):
            print "Making API call to get monument geolocation..."
            serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
            url = serviceurl + urllib.urlencode({
                'address': self.name,
                'components': 'country:ES|administrative_area:Zaragoza'
            })
            uh = urllib.urlopen(url)
            data = uh.read()
            print data
            root = ET.fromstring(data)
            location = root.find('result').find('geometry').find('location')
            self.latitude = location.find('lat').text
            self.longitude = location.find('lng').text
        else:
            print "Description is already set"

    @staticmethod
    def encode(attribute):
        if attribute:
            return attribute.encode('utf8')
        else:
            return "None"

    def __str__(self):
        ret = ""
        ret += "Id: " + str(self.id) + "\n"
        ret += "Name: " + self.encode(self.name) + "\n"
        ret += "Description: " + self.encode(self.description) + "\n"
        ret += "Website: " + self.encode(self.website) + "\n"
        ret += "x-pos: " + self.encode(self.x_pos) + "\n"
        ret += "y-pos: " + self.encode(self.y_pos) + "\n"
        ret += "latitude: " + self.encode(self.latitude) + "\n"
        ret += "longitude: " + self.encode(self.longitude)

        return ret
