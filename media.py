import webbrowser

class Movie():
	""" This class provides a way to store movie related information"""
	
	VALID_RATINGS = ["G", "PG", "PG-13", "R"] # Ratings for moviews

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_release_date, movie_main_actor):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.release_date = movie_release_date
		self.main_actor = movie_main_actor

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url) # opens the trailer url