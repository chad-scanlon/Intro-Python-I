# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
# python3 15_classes.py
# YOUR CODE HERE
class LatLon:
    lat = ''
    lon = ''
    def __init__(self, place_lat, place_lon):
        self.lat = place_lat
        self.lon = place_lon        

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):

    pointName = ''
    def __init__(self, waypoint_lat, waypoint_lon, waypoint_name):
        LatLon.__init__(self, waypoint_lat, waypoint_lon)
        self.waypoint_name = pointName

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
# class Geocache: 
#     def  __init__(self, name, difficulty, size):
#         self.name = name
#         self.difficulty = difficulty
#         LatLon.__init__(self)



# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
# print(geocache)
