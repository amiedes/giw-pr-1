#-*- coding: utf-8 -*-

"""
@authors: Daniel Reyes, Ania Pietrzak, Alberto Miedes
"""

class Monument:
    def __init__(self):
        self.name = ""
        self.x_position = -1
        self.y_position = -1
        self.latitude = None
        self.longitude = None
        self.website = ""
        self.description = None

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
