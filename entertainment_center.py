import media
import fresh_tomatoes
## Instances of Movie class to showcase my favorite movies
Princess_Mononoke = media.Movie("PrincessMononoke",
 						"A story of a princess who protects the forest from harm", 
 						"http://upload.wikimedia.org/wikipedia/en/2/24/Princess_Mononoke_Japanese_Poster_%28Movie%29.jpg", 
 						"https://www.youtube.com/watch?v=pkWWWKKA8jY",
 						"July 12, 1997",
 						"Yoji Matsuda")



Dumbanddumber = media.Movie("Dumbanddumber",
					" American road buddy comedy",
					"http://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg",
					"https://www.youtube.com/watch?v=lGXHVlEklgQ",
					"December 16, 1994",
					"Jim Carrey")

Darkknight = media.Movie("DarkKnight",
						"Batman comes back to take over gotham",
						"http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
						"https://www.youtube.com/watch?v=EXeTwQWrcwY",
						"July 14, 2008",
						"Christian Bale")

Inception = media.Movie("Inception",
						"Sci-fi heist thriller",
						"http://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
						"https://www.youtube.com/watch?v=E1iqGiX0lSg",
						"July 18, 2010",
						"Leonardo DiCaprio")

Interstellar = media.Movie("Interstellar",
						"Sci-fi space adventure",
						"http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
						"https://www.youtube.com/watch?v=0vxOhd4qlnA",
						"October 26, 2014",
						"Matthew McConaughey")

Looper = media.Movie("Looper",
					"Sci-fi time traver thriller",
					"http://upload.wikimedia.org/wikipedia/en/0/0a/Looper_poster.jpg",
					"https://www.youtube.com/watch?v=2iQuhsmtfHw",
					"September 6, 2012",
					"Bruce Willis")

movies = [Princess_Mononoke, Dumbanddumber, Darkknight, Inception, Interstellar, Looper]  #list of favorite movies
fresh_tomatoes.open_movies_page(movies)  #creates HTML file give movies list

