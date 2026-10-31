# Return only the dogs whose breed matches the chosen breed.
# If no breed is chosen (an empty string), return every dog.
def filter_by_breed(dogs, breed):
    # No breed chosen: show all dogs
    if breed == "":
        return dogs

    # Start with an empty list and add each dog that matches
    matching_dogs = []
    for dog in dogs:
        if dog["breed"] == breed:
            matching_dogs.append(dog)

    return matching_dogs