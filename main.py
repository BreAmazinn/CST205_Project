"""
Course Name: CST 205 Multimedia Design
Project Title: Pet Adoption Website
Abstract: A website that brings awarness to all pets in shelter who are in need of a loving home.
Authors: Breanna Holloman, Jaime Placios, Sayali Badole, Richard Lieu
Date: 5/19/2022
----
Breanna Holloman:
Jaime Placios:
Sayali Badole: info.html page, styling and documentations
Richard Lieu:
--
Description of important code blocks:
> In main.py a pet adoption API is extracted and stored in a .json file. Flask is used to display our website homepage(index.html)
> The index.html (homepage) page displays various features like animals and animal types that are ready to be adopted.
> If intrested, one can read more about the available pets- once clicked on "view" it will redirect to info.html() (pet description)
> The info.html page give further description of the pet one is intreseted in like breed, age, gender, color etc.
> This page also has an URL that would redirect to another website when one can adopt the pet.
> The animalType.html page will display all the different types of pets available for adoption. Once can search pets based on a specific breed, and it redirects to another page which diplays 20 breeds available. 
"""
from bs4 import BeautifulSoup
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import random
from PIL import Image
import json
import requests
from pprint import pprint


#API Extraction
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

# API information stored in a json file
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
    return render_template('index.html', animals = r1) #homepage- displays pets for adoption

@app.route('/typePage')
def typePage():
    return render_template('animalTypes.html', type = r2) #displays types of animals available for adoption

@app.route('/breed/<variable>', methods=['GET', 'POST'])
def breedPage(variable):
    breed_url = f'https://api.petfinder.com/v2/types/{variable}/breeds'

    breedResponse = requests.get(breed_url, headers=header)
    r3 = breedResponse.json() 

    return render_template('animalBreed.html', breed = r3) #displays the 20 breeds of a specific animal type

@app.route('/infoPage/<id>', methods= ['GET','POST'])
def infoPage(id):
    id_url = f'https://api.petfinder.com/v2/animals/{id}'
    idResponse = requests.get(id_url, headers=header)
    r4 = idResponse.json()
    return render_template('info.html', id=r4 ) #gives detailed description about an animal.

# ------ Necessary for the application to open once you run the python file ------
if __name__ == "__main__":
    app.run(debug=True)
