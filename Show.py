from Video import Release

class Show(Release):
    episodes = None
    def __init__(self, name, director, runtime, episodes):
        Release.__init__(self, name, director)
        self.runtime = runtime
        self.episodes = episodes

    def export(self):
        ret = Release.export(self)
        if(self.episodes != None):
            ret["episodes"] = self.episodes
        if(self.runtime != None):
            ret["ep_length"] = self.runtime
        return ret