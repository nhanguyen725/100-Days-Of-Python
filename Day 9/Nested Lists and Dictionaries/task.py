capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Marseille"],
    "Germany": ["Stuttgart", "Berlin"]
}

# Challenge: print Lille
print(travel_log["France"][1])

# Nested List in List
nested_list = ["A", "B", ["C", "D"]]
# Challenge: print "D"
print(nested_list[2][1])

# Nested Dictionary in Dictionary
travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Marseille"]
    },
    "Germany": {
        "num_times_visited": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    }
}
# Challenge: print Stuttgart
print(travel_log["Germany"]["cities_visited"][2])
