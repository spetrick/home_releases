class Release:
    name = None
    director = None
    actors = None
    year = None
    publisher = None

    def __init__(self, name, director):
        self.name = name
        self.director = director

    def setActors(self, actors):
        if(self.actors != None):
            self.actors.extend(actors)
        else:
            self.actors = actors

    def setYear(self, year):
        self.year = year
    
    def getYear(self):
        return self.year

    def setPublisher(self, publisher):
        self.publisher = publisher

    def getPublisher(self):
        return self.publisher

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def __str__(self):
        ret = self.name + " by " + self.director
        if(self.year != None):
            ret = ret + " in " + str(self.year)
        return ret

    def export(self):
        # Return a dictionary of available data for consumption
        ret = {
            "title": self.name
            ,"director": self.director
        }
        if(self.year != None):
            ret["year"] = self.year
        if(self.actors != None):
            ret["actors"] = self.actors
        if(self.publisher != None):
            ret["publisher"] = self.publisher
        return ret