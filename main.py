from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import random
from PIL import Image
import json
import requests
from pprint import pprint

app = Flask(__name__)

# payload= {
#     'client_id': 'CCLQp88b1h14vSALFxMmavytjKIrqwuDQ6AmTLPUD9Q6bzvkHU',
#     'client_secret': '78p93R1TiJLBQZoap48sTF3G6rUT6JGQPAku9DoI'
# }

# endpoint = 'https://api.petfinder.com/v2/animals'

# r = requests.get(endpoint, params = payload)

client_id = "CCLQp88b1h14vSALFxMmavytjKIrqwuDQ6AmTLPUD9Q6bzvkHU"
client_pass = "78p93R1TiJLBQZoap48sTF3G6rUT6JGQPAku9DoI"
data = {"grant_type":"client_credentials"}
auth_url = "https://api.petfinder.com/v2/oauth2/token"
api_url = 'https://api.petfinder.com/v2/animals'


r = requests.post(auth_url,data=data,auth=(client_id,client_pass))
data = r.json()
access_token = data['access_token']

#pprint(access_token)

header = {
    #'Accept': 'application/json',
    'Authorization': 'Bearer ' + access_token
}

response = requests.get(api_url, headers=header)

r1 = response.json()

pprint(r1)

# @app.route('/')
# def home():
#     return render_template('index.html')


