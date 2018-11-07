import Movie
import Show
#Mongo isn't the correct db for this, but I wanted to practice with it
#I will be adding an SQLite module eventually and am using the modules here for ease of replacement
import mongo

#Just run locally on a test instance
host = "mongodb://localhost:27017"
dbname = "releases"
col = "my_collection"
MongoCon = mongo.MongoCon(host , dbname, col)

#Test the Show and Movie classes
steinsgate = Show.Show("Steins;Gate", "Hiroshi Hamasaki", 30, 26)
boyandbeast = Movie.Movie("The Boy and the Beast", "Mamoru Hosoda" , 120)
steinsgate.setYear(2011)
steinsgate.setActors(["J. Michael Tatum", "Caitlin Glass"])
steinsgate.setActors(["Ashly Burch"])

#Test db insert
MongoCon.insert(steinsgate.export())
#Test db select
db_values = MongoCon.selectRecord('Steins;Gate')
#Test delete
MongoCon.deleteRecord(str(db_values[0]["_id"]))
