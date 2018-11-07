import Movie
import Show
import mongo

host = "mongodb://localhost:27017"
dbname = "releases"
col = "my_collection"
MongoCon = mongo.MongoCon(host , dbname, col)

steinsgate = Show.Show("Steins;Gate", "Hiroshi Hamasaki", 30, 26)
boyandbeast = Movie.Movie("The Boy and the Beast", "Mamoru Hosoda" , 120)
steinsgate.setYear(2011)
steinsgate.setActors(["J. Michael Tatum", "Caitlin Glass"])
steinsgate.setActors(["Ashly Burch"])
#MongoCon.insert(steinsgate.export())
db_values = MongoCon.selectRecord('Steins;Gate')
MongoCon.deleteRecord('5be22528b440c7078b2cc441')
for values in db_values:
    print(str(values["_id"]) + "\n")
