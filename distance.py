# Run the program with the following commands from the command line interface:
# python distance.py for Windows or python3 distance.py for Mac/Unix/Linux

import math  # import module math

from sklearn.metrics import euclidean_distances

R = 6371.0

# create a dictionary called cityCoord which contains 7 cities (latitude,longitude) coordinates
cityCoord = {
    'Hamburg': [53.55108, 9.99368],
    'AliceSprings': [-23.69748, 133.88362],
    'Vancouver': [49.24966, -123.11934],
    'Erbil': [36.19116, 44.00947],
    'Fortaleza': [-3.73045, -38.52180],
    'Ukiha': [33.34740, 130.75523],
    'Niamey': [13.52483, 2.10982]
}


# define a function call main() to calculate 3 of the following options
def main():
    print('Distance Calculator.\n')
    # print()
    print('Please select one of the following options:')
    print('1. Distance between two reference cities')
    print('2. Distance between a reference city and an arbitrary point')
    print('3. Distance between two arbitrary point')
    print('0. Exit\n')
    # print()

    '''
    alternative implemented code:
    Having users enter the option where the input might be a string or integer, we have to use try and except statement to valiadte the data types.
    we can use:
    option = int(input('Choice: '))
    in order to force users enter just integer and show error if they enter string or other data types
    '''

    # Enter the corresponded option (1, 2 , or 3)
    # could be option = input('Choice (1, 2, or 3): ') to tell the customer only enter integer instead of other data types
    option = input('Choice: ')

    # Test if the input of choice is valid or not (errors check)
    try:
        option = int(option)
    except:
        # this statement will be printed out in the console when choice is not an integer
        print('Error: Your choice must be a valid option (integer).')
        return option  # exit the option validation and return to the main program

    # Each option calculation

    # OPTION 1
    if option == 1:  # if the users type "1" in the console
        # .capitalize()  --> use this in case users enter forget to get the first letter capitalised or accidentally capitalise some of the letters
        city1 = input('Enter the name of the first city: ')
        # get the value of the corresponded city in the dictionary for city 1
        coord1 = cityCoord[city1]

        # .capitalize()  --> use this in case users enter forget to get the first letter capitalised or accidentally capitalise some of the letters
        city2 = input('Enter the name of the second city: ')
        # get the value of the corresponded city in the dictionary for city 2
        coord2 = cityCoord[city2]

        distant_method = input('''Which method would you like to use? \nEnter E for Euclidean distance method or Enter H for Haversin distance method or Enter B for both methods:\n''').capitalize(
        )  # --> use capitalize() in case users enter forget to get the first letter capitalised or accidentally capitalise some of the letters

        # latitude of corresponded city 1 in radians
        lat1 = math.radians(coord1[0])
        # longitude of corresponded city 1 in radians
        lon1 = math.radians(coord1[1])
        # latitude of corresponded city 2 in radians
        lat2 = math.radians(coord2[0])
        # longitude of corresponded city 2 in radians
        lon2 = math.radians(coord2[1])

        deltaLat = lat1-lat2
        deltaLon = lon1-lon2

        # use if statement for Euclidean (E), Haversin (H), and both (B) methods correspond to the input of users in line 66
        if distant_method == "E" or distant_method == "B":
            # Euclidean distance method
            delta_x = deltaLon*math.cos((lat1+lat2)/2)
            delta_y = deltaLat
            dist_1 = R*math.sqrt(delta_x**2 + delta_y**2)
            print("Euclidean distance is equal to: ", dist_1)

        if distant_method == "H" or distant_method == "B":
            # Haversin distance method
            temp = math.sin(deltaLat/2)**2 + (math.cos(lat1) *
                                              math.cos(lat2) * math.sin(deltaLon/2)**2)
            dist_2 = 2 * R * math.asin(math.sqrt(temp))
            print("Haversin distance is equal to: ", dist_2)

    # OPTION 2
    elif option == 2:  # if the users type "2" in the console
        # .capitalize()  --> use this in case users enter forget to get the first letter capitalised or accidentally capitalise some of the letters
        city1 = input('Enter the name of your reference city: ')
        # get the value of the corresponded city in the dictionary for city 1
        coord1 = cityCoord[city1]

        city2_lat = input('Enter the latitude of the arbitrary point: ')
        # check the validation of the input for coordinates
        try:
            city2_lat = float(city2_lat)
        except:
            print('Warning: The value entered is invalid. latitude cannot be a string')
            return city2_lat

        # check the validation of the input for coordinates
        city2_long = input('Enter the longitude of the arbitrary point: ')
        try:
            city2_long = float(city2_long)
        except:
            print('Warning: The value entered is invalid. latitude cannot be a string')
            return city2_long

        distant_method = input('''Which method would you like to use? \nEnter E for Euclidean distance method or Enter H for Haversin distance method or Enter B for both methods:\n''').capitalize(
        )  # --> use capitalize() in case users enter forget to get the first letter capitalised or accidentally capitalise some of the letters

        # latitude of corresponded city 1 in radians
        lat1 = math.radians(coord1[0])
        # longitude of corresponded city 1 in radians
        lon1 = math.radians(coord1[1])
        # lat2 = math.radians(coord2[0]) # latitude of corresponded city 2 in radians
        # lon2 = math.radians(coord2[1]) # longitude of corresponded city 2 in radians

        deltaLat = lat1-city2_lat
        deltaLon = lon1-city2_long

        # use if statement for Euclidean (E), Haversin (H), and both (B) methods correspond to the input of users in line 125
        if distant_method == "E" or distant_method == "B":
            # Euclidean distance method
            delta_x = deltaLon*math.cos((lat1+city2_lat)/2)
            delta_y = deltaLat
            dist_1 = R*math.sqrt(delta_x**2 + delta_y**2)
            print("Euclidean distance is equal to: ", dist_1)

        if distant_method == "H" or distant_method == "B":
            # Haversin distance method
            temp = math.sin(deltaLat/2)**2 + (math.cos(lat1) *
                                              math.cos(city2_lat) * math.sin(deltaLon/2)**2)
            dist_2 = 2 * R * math.asin(math.sqrt(temp))
            print("Haversin distance is equal to: ", dist_2)

    # OPTION 3
    elif option == 3:  # if the users type "3" in the console
        city1_lat = float(
            input('Enter the latitude of the first arbitrary point: '))

        city1_long = float(
            input('Enter the longitude of the first arbitrary point: '))

        city2_lat = float(
            input('Enter the latitude of the second arbitrary point: '))

        city2_long = float(
            input('Enter the longitude of the second arbitrary point: '))

        distant_method = input('''Which method would you like to use? \nEnter E for Euclidean distance method or Enter H for Haversin distance method or Enter B for both methods:\n''').capitalize(
        )  # --> use capitalize() in case users enter forget to get the first letter capitalised or accidentally capitalise some of the letters

        deltaLat = city1_lat-city2_lat
        deltaLon = city1_long-city2_long

        # use if statement for Euclidean (E), Haversin (H), and both (B) methods correspond to the input of users in line 167
        if distant_method == "E" or distant_method == "B":
            # Euclidean distance method
            delta_x = deltaLon*math.cos((city1_long+city2_lat)/2)
            delta_y = deltaLat
            dist_1 = R*math.sqrt(delta_x**2 + delta_y**2)
            print("Euclidean distance is equal to: ", dist_1)

        if distant_method == "H" or distant_method == "B":
            # Haversin distance method
            temp = math.sin(deltaLat/2)**2 + (math.cos(city1_lat)
                                              * math.cos(city2_lat) * math.sin(deltaLon/2)**2)
            dist_2 = 2 * R * math.asin(math.sqrt(temp))
            print("Haversin distance is equal to: ", dist_2)

    elif option == 0:  # if the users type "0" in the console
        print('Bye!')

    else:
        # this statement will be printed out in the console when choice is not in the provided range
        print('Error: Your choice must be a valid option (range).')

    return  # exit the function and return value


# this block of code will execute if this .py file is used as a module for other .py file
if __name__ == "__main__":
    main()
