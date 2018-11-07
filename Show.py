from Video import Release

class Show(Release):
    ###Extend Release with TV Show specific information###
    episodes = None
    def __init__(self, name, director, runtime, episodes):
        Release.__init__(self, name, director)
        #Runtime has a different meaning for a tv series than it does a movie
        self.runtime = runtime
        self.episodes = episodes

    def export(self):
        ret = Release.export(self)
        ret["type"] = "show"
        if(self.episodes != None):
            ret["episodes"] = self.episodes
        if(self.runtime != None):
            ret["ep_length"] = self.runtime
        return ret