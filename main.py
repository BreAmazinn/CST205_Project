from calendar import c
from bs4 import BeautifulSoup
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import random
from PIL import Image
import json
import requests
from pprint import pprint



payload= {
    'client_id': 'hXshJldjTfflmGEr2SVfXy3kwNKDEjlcrEwnSOqI57e97nNwpJ',
    'client_secret': 'zMBePeVDixUqwvAosfrlgtnRZ7D7xj0rHaUxWNVq'
}

endpoint = 'https://api.petfinder.com/v2/animals'

r = requests.get(endpoint, params = payload)

client_id = "hXshJldjTfflmGEr2SVfXy3kwNKDEjlcrEwnSOqI57e97nNwpJ"
client_pass = "zMBePeVDixUqwvAosfrlgtnRZ7D7xj0rHaUxWNVq"
data = {"grant_type":"client_credentials"}

auth_url = "https://api.petfinder.com/v2/oauth2/token"
api_url = 'https://api.petfinder.com/v2/animals'
type_url = 'https://api.petfinder.com/v2/types'


r = requests.post(auth_url,data=data,auth=(client_id,client_pass))
data = r.json()
access_token = data['access_token']


header = {
    #'Accept': 'application/json',
    'Authorization': 'Bearer ' + access_token
}

response = requests.get(api_url, headers=header)
r1 = response.json()

unofficial_list = []
for list in r1['animals']:
    unofficial_list.append(list)


official_list = []

for data in unofficial_list:
    if data['photos'] != []:
        official_list.append(data)
    elif data['photos'] == None:
        print(" ")


# pprint(official_list[0])
for x in official_list:
    print(x['photos'])

# pprint(official_list[0]['photos'])
secondJson = requests.get(api_url, headers=header)
r2 = secondJson.json()




typeResponse = requests.get(type_url, headers=header)
r3 = typeResponse.json()

# other = []
# for list in r2['animals']:
#     other.append(list)


# secondOfficialList = []


# for x in other:
#     if x['photos'] != []:
#         official_list.append(x)


# ------ Flask Application ------
app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html', animals = official_list)

# @app.route('/animalType')
# def typePage():
#     return render_template('animalTypes.html', type = off)

# @app.route('/breed/<variable>', methods=['GET', 'POST'])
# def breedPage(variable):
#     breed_url = f'https://api.petfinder.com/v2/types/{variable}/breeds'

#     breedResponse = requests.get(breed_url, headers=header)
#     r3 = breedResponse.json()

#     return render_template('animalBreed.html', breed = r2)

@app.route('/information')
def animalInfo():
    return render_template('AnimalInfo.html', info = official_list)

# print("There are ",len(official_list), "animals with photos")
# another = []
# for x in official_list:
#     if x['name'] not in another:
#         another.append(x)


# for x in another:
#     print(x['name'])

# ------ Necessary for the application to open once you run the python file ------
# if __name__ == "__main__":
#     app.run(debug=True)
