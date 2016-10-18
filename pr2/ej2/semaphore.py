class Semaphore:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other):
        return (self.latitude == other.latitude and self.longitude == other.longitude)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return int(self.latitude * self.longitude)
