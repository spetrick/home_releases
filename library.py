import Movie
import Show
#Mongo isn't the correct db for this, but I wanted to practice with it
#I will be adding an SQLite module eventually and am using the modules here for ease of replacement
import mongo
#Kivy is a cross platform UI framework with rich support for touch input as well as keyboard/mouse
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

#Test the Show and Movie classes with test data
steinsgate = Show.Show("Steins;Gate", "Hiroshi Hamasaki", 30, 26)
boyandbeast = Movie.Movie("The Boy and the Beast", "Mamoru Hosoda" , 120)
steinsgate.setYear(2011)
steinsgate.setActors(["J. Michael Tatum", "Caitlin Glass"])
steinsgate.setActors(["Ashly Burch"])




class Library(BoxLayout):
    def __init__(self, **kwargs):
        super(Library, self).__init__(**kwargs)
        #class variables

        #class funtions
        def add_to_db(self):
            if(dropdown.value == "Show"):
                new_release = Show.Show(title.text, director.text, ep_length.text, ep_count.text)
            elif(dropdown.value == "Movie"):
                new_release = Movie.Movie(title.text, director.text, film_length.text)
            MongoCon.insert(new_release.export())

        main_layout = BoxLayout(padding = 10, orientation = "horizontal")
        self.add_widget(main_layout)
        list_layout = BoxLayout(padding = 5, orientation = "vertical")
        input_layout = BoxLayout(padding = 5, orientation = "vertical")
        input_layout.add_widget(Label(text = "Type"))
        #Dropdown doesn't actually select anything yet
        dropdown = DropDown()
        show_btn = Button(text = "Show", size_hint_y = None, height = 45)
        show_btn.bind(on_press = lambda show_btn: dropdown.select(show_btn.text))
        movie_btn = Button(text = "Movie", size_hint_y = None, height = 45)
        movie_btn.bind(on_press = lambda movie_btn: dropdown.select(movie_btn.text))
        dropdown.add_widget(show_btn)
        dropdown.add_widget(movie_btn)
        input_layout.add_widget(dropdown)
        input_layout.add_widget(Label(text = 'Title'))
        title = TextInput(mutliline = False)
        input_layout.add_widget(title)
        input_layout.add_widget(Label(text = "Director"))
        director = TextInput(multiline = False)
        input_layout.add_widget(director)
        input_layout.add_widget(Label(text = "Episode Length"))
        ep_length = TextInput(multiline = False)
        input_layout.add_widget(ep_length)
        input_layout.add_widget(Label(text = "Film Length"))
        film_length = TextInput(multiline = False)
        input_layout.add_widget(film_length)
        input_layout.add_widget(Label(text = "Episode Count"))
        ep_count = TextInput(multiline = False)
        input_layout.add_widget(ep_count)
        add_button = Button(text = "Add Release")
        add_button.bind(on_press = add_to_db)
        input_layout.add_widget(add_button)

        #Just run locally on a test instance
        host = "mongodb://localhost:27017"
        dbname = "releases"
        col = "my_collection"
        MongoCon = mongo.MongoCon(host , dbname, col)
        #Populate with any existing items from the db
        records = MongoCon.selectAll()
        release_list = []
        if(records):
            for release in records:
                #Records can either be of type show or movie. Certain data is required, otherwise check for it and add if present
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

        #Create a list of titles in the db to display
        list_of_titles = ''
        for ReleaseObj in release_list:
            list_of_titles += ReleaseObj.getName()
        list_layout.add_widget(Label(text = list_of_titles))
        main_layout.add_widget(list_layout)
        main_layout.add_widget(input_layout)

        
class LibraryApp(App):
    def build(self):
        return Library()

if __name__ == '__main__':
    LibraryApp().run()

        #Test db insert
    #    MongoCon.insert(steinsgate.export())
        #Test delete
    #    MongoCon.deleteRecord(str(db_values[0]["_id"]))