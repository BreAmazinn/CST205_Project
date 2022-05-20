"""
Course Name: CST 205 Multimedia Design
Project Title: Pet Adoption Website
Abstract: A website that brings awarness to all pets in shelter who are in need of a loving home.
Authors: Breanna Holloman, Jaime Placios, Sayali Badole, Richard Lieu
Date: 5/19/2022
Github Link: https://github.com/BreAmazinn/CST205_Project.git
----
Breanna Holloman: Finding an API, getting responses and routing. Set up animal type page
Jaime Placios: Function to only grab animals with a certain criteria, Navigation Bar, 
Sayali Badole: AnimalInfo..html page, webpage styling and documentations, AnimalInfo.html routing
Richard Lieu:
As a team: Our group worked more as a team - index.html, fixing the bugs etc was done over weekly meetings.
--
Description of important code blocks:
> In main.py a pet adoption API is extracted and stored in a .json file. Flask is used to display our website homepage(index.html)
> The index.html (homepage) page displays various features like animals and animal types that are ready to be adopted.
> If intrested, one can read more about the available pets- once clicked on "view" it will redirect to info.html() (pet description)
> The info.html page give further description of the pet one is intreseted in like breed, age, gender, color etc.
> This page also has an URL that would redirect to another website when one can adopt the pet.
> The animalType.html page will display all the different types of pets available for adoption. Once can search pets based on a specific breed, and it redirects to another page which diplays 20 breeds available. 
"""
from calendar import c
from bs4 import BeautifulSoup
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import random
from PIL import Image
import json
import requests
from pprint import pprint
#API EXTRACTION
payload= {
    'client_id': 'CCLQp88b1h14vSALFxMmavytjKIrqwuDQ6AmTLPUD9Q6bzvkHU',
    'client_secret': '78p93R1TiJLBQZoap48sTF3G6rUT6JGQPAku9DoI'
}
endpoint = 'https://api.petfinder.com/v2/animals'
r = requests.get(endpoint, params = payload)
client_id = "CCLQp88b1h14vSALFxMmavytjKIrqwuDQ6AmTLPUD9Q6bzvkHU"
client_pass = "78p93R1TiJLBQZoap48sTF3G6rUT6JGQPAku9DoI"
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
#MAIN JSON FILE WITH ALL THE DATA
r1 = response.json()
i=0
unofficial_list = []
for list in r1['animals']:
    unofficial_list.append(list)
#PREPROCESSED LIST OF PETS WITH PICTURES ON DISPLAY
official_list = []
for data in unofficial_list:
    if data['photos'] != []:
        official_list.append(data)
    elif data['photos'] == None:
        print(" ")
secondJson = requests.get(api_url, headers=header)
r2 = secondJson.json()
typeResponse = requests.get(type_url, headers=header)
r3 = typeResponse.json()

# ------ Flask Application ------
app = Flask(__name__)
# ROUTE TO THE HOMEPAGE
@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html', animals = official_list)  
#ROUTE TO THE DIFFERENT ANIMAL TYPES AVAILABLE FOR ADOPTION PAGE
@app.route('/animalType')
def typePage():
    return render_template('animalTypes.html', type = r3)

#ROUTE TO DIFFERENT TYPES OF BREEDS AVAILABLE FOR ADOPTION
@app.route('/breed/<variable>', methods=['GET', 'POST'])
def breedPage(variable):
    breed_url = f'https://api.petfinder.com/v2/types/{variable}/breeds'
    breedResponse = requests.get(breed_url, headers=header)
    r3 = breedResponse.json()
    return render_template('animalBreed.html', type = variable, breed = r3, animals = r1)

#DETAILED PET DESCRIPTION OF A PET
@app.route('/information/<variable>', methods=['GET','POST'])
def animalInfo(variable):
    info_url = f'https://api.petfinder.com/v2/animals/{variable}'
    infoResponse = requests.get(info_url, headers=header)
    r4 = infoResponse.json()
    return render_template('AnimalInfo.html', info = r4) 

# ------ Necessary for the application to open once you run the python file ------

if __name__ == "__main__":
    app.run(debug=True)
