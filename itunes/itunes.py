# To run program "terminal" :python3 {name of file} {name of album}

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# Getting the apple api and storing it in a variable

"""
To change the number of songs displayed, change "limit".
Name of the album is at the end of the sys statment. 
"""
try:
    response = requests.get(
        "https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1]
    )
    response.raise_for_status()
except requests.HTTPError:
    print("Could not complete request!")
except ConnectionError:
    print("Please connect to the internet!!!")

songs = response.json()

"""
its importent to print out the json contents in order to understand
and what key words are used in order to get back the values.
"""

# Displays the data found in json form
"""
print(response.json())
"""

# Displays the results
for result in songs["results"]:
    print(f"> {result['trackName']}")
