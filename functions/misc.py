def locationParse(strLocation):
    # Turns raw string input (CSV) into array for location of object in 2D array
    insertLocation = strLocation.split(",")
    insertLocation = list(map(lambda x: int(x)-1, insertLocation))
    return(insertLocation)
