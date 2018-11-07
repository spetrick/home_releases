from Video import Release

class Movie(Release):
    def __init__(self, name, director, runtime):
        Release.__init__(self, name, director)
        self.runtime = runtime