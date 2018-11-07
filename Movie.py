from Video import Release

class Movie(Release):
    ###Extend Release with movie specific information###
    
    def __init__(self, name, director, runtime):
        Release.__init__(self, name, director)
        self.runtime = runtime

    def export(self):
        ret = Release.export(self)
        ret["type"] = "movie"
        if(self.runtime != None):
            ret["length"] = self.runtime
        return ret