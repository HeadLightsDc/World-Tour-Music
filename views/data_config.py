class User:
    def __init__(self, name, lastname, email, user_id, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.user_id = user_id
        self.password = password
        self.event_history = []
        
class Review:
    def __init__(self, review_id, event_id, user_id, rating, comment, mood):
        self.review_id = review_id
        self.event_id = event_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
        self.mood = mood
    
class Event:
    def __init__(self, event_id, name, artist, genre, id_ubication, time_start, description, imagen):
        self.event_id = event_id
        self.name = name
        self.artist = artist
        self.genre = genre
        self.id_ubication = id_ubication
        self.time_start = time_start
        self.description = description
        self.image = imagen
        
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
        