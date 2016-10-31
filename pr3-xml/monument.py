#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

class Monument:
    def __init__(self, name, website, x_pos, y_pos):
        self.name = name
        self.description = None
        self.website = website
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.latitude = None
        self.longitude = None

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

    def set_description():
        if description is None:
            print "Making API call to get monument description..."
            # TODO: make call to Zaragoza's City Council's API
        else:
            print "Description is already set"

    def set_geolocation():
        if (latitude is None) or (longitude is None):
            print "Making API call to get monument geolocation..."
            # TODO: make call to Google geolocation API
        else:
            print "Description is already set"

    @staticmethod
    def encode(attribute):
        if attribute:
            return attribute.encode('utf-8')
        else:
            return "None"

    def __str__(self):
        ret = ""
        ret += "Name: " + self.encode(self.name) + "\n"
        ret += "Description: " + self.encode(self.description) + "\n"
        ret += "Website: " + self.encode(self.website) + "\n"
        ret += "x-pos: " + self.encode(self.x_pos) + "\n"
        ret += "y-pos: " + self.encode(self.y_pos) + "\n"
        ret += "latitude: " + self.encode(self.latitude) + "\n"
        ret += "longitude: " + self.encode(self.longitude)

        return ret
