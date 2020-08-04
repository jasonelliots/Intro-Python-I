"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE

new = {
        "lat": 43,
        "lon": -122,
        "name": "a fifth place"
    }

waypoints.append(new)

# print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE

waypoints[0] =  {
        "lat": 43,
        "lon": -130,
        "name": "not a place"
    }

print(waypoints[0])

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE

for entry in waypoints:
    print(entry["lat"], entry["lon"], entry["name"])



########

# d = {}

# e  = {"foo": 12, 11: "bar"}

# print(e["foo"])
# print(e.get('foo'))
# print(e[11])
# print(e.get(11))


# for key in e: 
#     print(key, e[key])

# for key, val in e.items():
#     print(key, val)

# for key, val in e.items():
#     print(f'Key is {key} and value is {val}')