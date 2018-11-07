import Movie
import Show
#Mongo isn't the correct db for this, but I wanted to practice with it
#I will be adding an SQLite module eventually and am using the modules here for ease of replacement
import mongo
#Kivy is a cross platform UI framework with rich support for touch input as well as keyboard/mouse
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

#Test the Show and Movie classes with test data
steinsgate = Show.Show("Steins;Gate", "Hiroshi Hamasaki", 30, 26)
boyandbeast = Movie.Movie("The Boy and the Beast", "Mamoru Hosoda" , 120)
steinsgate.setYear(2011)
steinsgate.setActors(["J. Michael Tatum", "Caitlin Glass"])
steinsgate.setActors(["Ashly Burch"])




class Library(GridLayout):
    def __init__(self, **kwargs):
        super(Library, self).__init__(**kwargs)
        #Just run locally on a test instance
        host = "mongodb://localhost:27017"
        dbname = "releases"
        col = "my_collection"
        MongoCon = mongo.MongoCon(host , dbname, col)
        records = MongoCon.selectAll()
        self.cols = 2
        release_list = []
        for release in records:
            if(release["type"] == "show"):
                ReleaseObj = Show.Show(release["title"], release["director"], release["ep_length"], release["episodes"])
            elif(release["type"] == "movie"):
                ReleaseObj = Movie.Movie(release["title"], release["director"], release["length"])
            if("actors" in release):
                ReleaseObj.setActors(release["actors"])
            if("year" in release):
                ReleaseObj.setYear(release["year"])
            if("publisher" in release):
                ReleaseObj.setPublisher(release["publisher"])
            release_list.append(ReleaseObj)

        for x in release_list:
            print(str(x))

        list_of_titles = ''
        for ReleaseObj in release_list:
            list_of_titles += ReleaseObj.getName()
        self.add_widget(Label(text = list_of_titles))

        #Test db insert
    #    MongoCon.insert(steinsgate.export())
        #Test db select
    #    db_values = MongoCon.selectRecord('Steins;Gate')
        #Test delete
    #    MongoCon.deleteRecord(str(db_values[0]["_id"]))

class LibraryApp(App):
    def build(self):
        return Library()

if __name__ == '__main__':
    LibraryApp().run()
