import requests
import json
import re

# function that will provide directions between two locations
def get_directions(origin, destination, mode):
    # input parameters
    APIkey = "apikey" # use your own API key from Google Cloud
    origin = origin
    destination = destination
    mode = mode
    
    # remove space with "+" so it fits URL
    origin = origin.replace(" ", "+")
    destination = destination.replace(" ", "+")

    # add parameters to URL
    url = 'https://maps.googleapis.com/maps/api/directions/json?origin='+origin+'&destination='+destination+'&mode='+mode+'&key='+APIkey

    # get response and store in directions
    response = requests.get(url)
    directions = response.json()

    # get navigation info
    steps = directions['routes'][0]['legs'][0]['steps']

    # print each step in directions
    for i in range(0,len(steps)):
        # get required information
        dist = steps[i]['distance']['text'] # format as text
        inst = steps[i]['html_instructions']
        time = steps[i]['duration']['text'] # format as text

        # get rid of html tags
        clean = re.compile('<.*?>')
        inst = re.sub(clean, '', inst)

        # format steps
        sentence = 'In '+dist+', '+inst+'. This should take you '+time+".\n"
        print(sentence)


# Main
origin = input('Starting location:')
destination = input('Final location:')
mode = input('Mode of transportation. Choose from driving, walking, bicycling, or transit:')

# Test parameters
#origin = "Durham, NC"
#destination = "Raleigh"
#mode = "driving"

# run get_directions function
get_directions(origin, destination, mode)