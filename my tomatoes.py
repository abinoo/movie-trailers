import webbrowser
import fresh_tomatoes

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer)

up = Movie("Up",
           "An old man and a young boy go on an adventure",
           "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
           "https://www.youtube.com/watch?v=pkqzFUhGPJg")

the_thing = Movie("The Thing",
                  "A group of scientists in Antartica find something unexpected",
                  "https://resizing.flixster.com/QbvEDOjrtErH1m3mC3dccQdpK4A=/206x305/v1.bTsxMTE2ODg5NTtqOzE3NTg5OzEyMDA7ODAwOzEyMDA",
                  "https://www.youtube.com/watch?v=p35JDJLa9ec")

godfather = Movie("The Godfather",
                  "A man has to take over for his father's mafia business",
                  "https://images-na.ssl-images-amazon.com/images/I/61ehu0M3T%2BL._AC_UL320_SR214,320_.jpg",
                  "https://www.youtube.com/watch?v=sY1S34973zA")

movies = [up, the_thing, godfather]
fresh_tomatoes.open_movies_page(movies)
