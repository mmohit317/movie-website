import webbrowser
# to import webbrowser which is used by fresh_tomatoes


class Movie():
    """It is class of movies which has object self and member functions like
       title, storyline etc."""
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
                # to construct the member function
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube
