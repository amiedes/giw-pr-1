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

    def parse_description(self, description):
        new_data=description.split("<p>")
        to_print=""
        for i in range(len(new_data)):
            if(i==0 or "<a" in new_data[i] or "<span" in new_data[i]):
                continue
            elif("<h3>" in new_data[i] or "div>" in new_data[i] or "<strong>" in new_data[i]):
               new_data[i]=new_data[i].replace("<h3>","")
               new_data[i]=new_data[i].replace("</h3>",":")
               new_data[i]=new_data[i].replace("<div>","")
               new_data[i]=new_data[i].replace("</div>","\n\n")
               new_data[i]=new_data[i].replace("<strong>","")
               new_data[i]=new_data[i].replace("</strong>","")
               to_print=to_print+new_data[i]+"\n"
            else:
               to_print=to_print+new_data[i]+"\n"
        return to_print

    def set_description(self):
        if self.description is None:
            web_content = urllib.urlopen(self.website)
            data = web_content.read()
            initial_pos = data.find("<h3>Descripc")
            final_pos = data.find("<h3>Enlaces</h3>")
            description = data[initial_pos:final_pos]
            description = description.replace("</p>","")
            description = description.decode('latin-1')
            final_description = self.parse_description(description)
            self.description = final_description
        else:
            print "Description is already set"

    def set_geolocation(self):
        if (self.latitude is None) or (self.longitude is None):
            print "Making API call to get monument geolocation..."
            serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
            url = serviceurl + urllib.urlencode({
                'address': self.name.encode('utf-8'),
                'components': 'country:ES|administrative_area:Zaragoza'
            })
            uh = urllib.urlopen(url)
            data = uh.read()
            root = ET.fromstring(data)
            location = root.find('result').find('geometry').find('location')
            self.latitude = location.find('lat').text
            self.longitude = location.find('lng').text
        else:
            print "Description is already set"

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
