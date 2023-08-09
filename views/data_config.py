class User:
    def __init__(self, name, lastname, email, nickname, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.nickname = nickname
        self.password = password
        self.event_history = []
          
class Event:
    def __init__(self, venue, name, description, artist, address, latitude, longitude, start_time, end_time):
        self.venue = venue
        self.name = name
        self.description = description
        self.artist = artist
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.start_time = start_time
        self.end_time = end_time

class Review:
    def __init__(self, review_id, event_id, user_id, rating, comment, mood):
        self.review_id = review_id
        self.event_id = event_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
        self.mood = mood
        
class Ubication:
    def __init__(self, ubication_id, name, address, coordinates): #Investigar funcionamiento list
        self.ubication_id = ubication_id
        self.name = name
        self.address = address
        self.coordinates = []
        
class Route:
    def __init__(self, route_id, name, destinations): #Investigar funcionamiento list
        self.route_id = route_id
        self.name = name
        self.destinations = []
        