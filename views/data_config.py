class User:
    def __init__(self, name, lastname, email, user_id, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.user_id = user_id
        self.password = password
        self.event_history = []
          
class Event:
    def __init__(self, venue, name, description, address, latitude, longitude, date, schedule):
        self.venue = venue
        self.name = name
        self.description = description
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.date = date
        self.schedule = schedule

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
        