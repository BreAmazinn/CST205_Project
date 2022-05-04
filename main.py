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
api_url = "https://api.petfinder.com/v2/oauth2/token"

r = requests.post(api_url,data=data,auth=(client_id,client_pass))

data = r.json()

token = data['access_token']

pprint(token)

# url = 'https://api.petfinder.com/v2/animals'

# def get_new_token():
#     auth_server_url = "https://api.petfinder.com/v2/oauth2/token"
#     client_id = 'CCLQp88b1h14vSALFxMmavytjKIrqwuDQ6AmTLPUD9Q6bzvkHU'
#     client_secret = '78p93R1TiJLBQZoap48sTF3G6rUT6JGQPAku9DoI'

#     taken_req_payload = {'grant_type': 'client_credentials'}
#     auth=(client_id, client_secret))    

# token = get_new_token()


# @app.route('/')
# def home():
#     return render_template('index.html')


