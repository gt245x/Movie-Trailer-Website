import webbrowser


class Video():
    """ This class provides a way to store video, movie and TvShows"""
    def __init__(self,title, duration, trailer_youtube, poster_image, artist,genre):
        self.title = title
        self.duration = duration
        self.trailer_youtube_url = trailer_youtube
        self.poster_image_url = poster_image
        self.artist = artist
        self.genre = genre

    def __repr__(self):
        """returns a string containing a printable representation of an object"""
        return "Movie name: " + self.title

    def show_trailer(self):
        """This method plays a trailer of the movie."""
        webbrowser.open(self.trailer_youtube_url)
    def show_poster(self):
        """opens the poster of the movie."""
        webbrowser.open(self.poster_image_url)






class Movie(Video):
    """ This class provides a way to store movie related information with inheritance from Video class"""


    def __init__(self,title,duration,trailer_youtube,poster_image, artist,genre, movie_storyline, release_date,rating,box_office, director):
        Video.__init__(self,title,duration,trailer_youtube,poster_image, artist,genre)
        self.storyline = movie_storyline
        self.release_date = release_date
        self.rating = rating
        self.box_office = box_office
        self.director = director


    def show_info(self):
        """This method prints info that includes video title, genre, running time, release-date and box office numbers."""
        print ("Title: " + self.title)
        print ("Genre: " + self.genre)
        print ("Running time is " + str(self.duration) + " minutes")
        print ("Release date in US was on " + self.release_date)
        print ("Box office: $" + str(self.box_office) + " million")
        print ("Directed by " + self.director)

    def __repr__(self):
        """returns a string containing a printable representation of an object"""
        return "Movie name: " + self.title

class TvShow(Video):
    """ This class provides a way to store TvShows with inheritance from Video class"""
    def __init__(self,title,duration,trailer_youtube,poster_image, artist,genre, season,tv_station,day,time):
        Video.__init__(self,title,duration,trailer_youtube,poster_image, artist, genre)
        self.season = season
        self.tv_station = tv_station
        self.day = day
        self.time = time

    def get_local_listing(self):
        """This method prints the local listing of the Tv show."""
        print ("Local listing for " + self.title + " is on " + self.tv_station + " every " + self.day + " at " + self.time)

    def __repr__(self):
        """returns a string containing a printable representation of an object"""
        return "Movie name: " + self.title

