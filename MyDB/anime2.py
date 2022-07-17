#import csv library for Opening and Reading from a csv file
import csv 
#we are going to use this file to execute SQL queries
from cs50 import SQL 
open("animee.db", "w").close()
tirz= SQL("sqlite:///animee.db")
tirz.execute("CREATE TABLE anime(id INTEGER, anime_title TEXT, rating INTEGER, release_year INTEGER, PRIMARY KEY(id))") 
tirz.execute("CREATE TABLE voice_actors(id INTEGER, name TEXT, dob INTEGER, age INTEGER, PRIMARY KEY(id))")
tirz.execute("CREATE TABLE characters(id INTEGER, name TEXT, c_age INTEGER, PRIMARY KEY(id))")
tirz.execute("CREATE TABLE japanese(id INTEGER PRIMARY KEY, anime_id INTEGER, characters_id INTEGER,  voice_actors_id INTEGER, FOREIGN KEY(anime_id) REFERENCES anime(id), FOREIGN KEY(characters_id) REFERENCES characters(id), FOREIGN KEY(voice_actors_id) REFERENCES voice_actors(id))")

with open("animeinfo.csv","r",encoding="UTF-8") as file:

    reader =csv.DictReader(file)

    for column in reader:

        Title = column["anime_title"]
        Year = column["release_year"]
        Rate = column["rating"]
        Actors = column["voice_actors"]
        Age = column["age"]
        Birth = column["dob"] 
        Character = column["characters"] 
        Character_age = column["c_age"] 
        

        anime = tirz.execute("INSERT INTO anime(anime_title, rating, release_year) VALUES(?, ?, ?)", Title, Rate, Year)

        voice_actors = tirz.execute("INSERT INTO voice_actors(name, dob, age) VALUES(?, ?, ?)", Actors, Birth, Age)

        characters = tirz.execute("INSERT INTO characters(name,c_age) VALUES(?,?)",Character,Character_age)

        japanese = tirz.execute("INSERT INTO japanese(anime_id,characters_id,voice_actors_id) VALUES ((SELECT id FROM anime WHERE anime_title=?),(SELECT id FROM characters WHERE name=?),(SELECT id FROM voice_actors WHERE name=?))",Title,Character,Actors)



        
        