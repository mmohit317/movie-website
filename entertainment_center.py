import fresh_tomatoes
#to import fresh_tomatoes.py which contains html code
import media
#to import media.py which consists of class Movie
#which is used below
#here six movie objects are created initialised with title,
#storyline,poster,imagelink,trailer link
firangi = media.Movie("Firangi",
                      "Firangi is a 2017 Indian Hindi period action-comedy "
                      "drama filmof about 200 years ago.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/a/af/"
                      "Firangi_-_Poster_1.jpg/220px-Firangi_-_Poster_1.jpg",
                      "https://www.youtube.com/watch?v=C3GiqcWF5QE")
#media.Movie is used to assign values to the class Movie which is in media.py
omg = media.Movie("Oh My God",
                  "The Story of a Man who is affected by Act Of God",
                  "https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/"
                  "OMG_Poster.png/220px-OMG_Poster.png",
                  "https://www.youtube.com/watch?v=8nUwpoTrWFk")
dangal = media.Movie("Dangal",
                     "The film is loosely based on the Phogat family, "
                     "telling thestory of Mahavir Singh Phogat, an "
                     "amateur wrestler, who trains his daughters Geeta"
                     "Phogat and Babita Kumari to become India's first "
                     "world-class female wrestlers.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/9/99"
                     "/Dangal_Poster.jpg/220px-Dangal_Poster.jpg",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")
tiger_zinda_hai = media.Movie("Tiger Zinda Hai",
                              "is based on the 2014 abduction of "
                              "Indian nurses by ISIL",
                              "https://upload.wikimedia.org/wikipedia/en/5/"
                              "5e/Tiger_Zinda_Hai_-_Poster.jpg",
                              "https://www.youtube.com/watch?v=ePO5M5DE01I")
zindagi_na_milegi_dobaara = media.Movie("Zindagi Na Milegi Dobaara",
                                        "This Movie is a 2011 Indian"
                                        "comedy-drama road film in which 3"
                                        "friends plan a trip to Spain. ",
                                        "https://upload.wikimedia.org/"
                                        "wikipedia/en/3/3d/Zindagin"
                                        "amilegidobara.jpg",
                                        "https://www.youtube.com/"
                                        "watch?v=bQR_bxragHk")
newton = media.Movie("Newton",
                     "The Movie is about the life of a person Newton Kumar,a"
                     "rookie government clerk sent on election duty.",
                     "https://upload.wikimedia.org/wikipedia/en/6/68/"
                     "Newton_%28film%29.png",
                     "https://www.youtube.com/watch?v=yU6zMPFd4UU")
movies = [firangi, omg, dangal, tiger_zinda_hai, zindagi_na_milegi_dobaara,
          newton]
#stores objects in alist
fresh_tomatoes.open_movies_page(movies)
#fresh_tomatoes.open_movies_page(movies) opens the movie
#website in default browser
