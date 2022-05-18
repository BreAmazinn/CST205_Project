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

typeResponse = requests.get(type_url, headers=header)
r2 = typeResponse.json()

#pprint(r1)

# ------ Flask Application ------
app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html', animals = r1)

@app.route('/animalType')
def typePage():
    return render_template('animalTypes.html', type = r2)

@app.route('/breed/<variable>', methods=['GET', 'POST'])
def breedPage(variable):
    breed_url = f'https://api.petfinder.com/v2/types/{variable}/breeds'

    breedResponse = requests.get(breed_url, headers=header)
    r3 = breedResponse.json()

    return render_template('animalBreed.html', type = variable, breed = r3, animals = r1)


@app.route('/info/<variable>', methods=['GET', 'POST'])
def infoPage(variable):
    info_url = f'https://api.petfinder.com/v2/animals/{variable}'

    infoResponse = requests.get(info_url, headers=header)
    r4 = infoResponse.json()

    return render_template('info.html', pet = r4)

# ------ Necessary for the application to open once you run the python file ------
if __name__ == "__main__":
    app.run(debug=True)
