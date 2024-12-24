import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
# en devellopement DEVELLOPEMENT

# Charge les variables d'environnement du fichier .env
load_dotenv()
state = os.environ.get('STATE')
client_id = os.environ.get('PAYPAL_CLIENT_ID')
client_secret = os.environ.get('PAYPAL_CLIENT_SECRET')

# URL de l'API pour obtenir le token
if state == "DEVELLOPEMENT":
    url_add = "https://api-m.sandbox.paypal.com"
else:
    url_add = "https://api-m.paypal.com"



# Envoi de la requête POST avec authentification de base
def get_bearer():
    url = f"{url_add}/v1/oauth2/token"
    # Paramètres de la requête
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    res = requests.post(url, headers=headers, data=data, auth=HTTPBasicAuth(client_id, client_secret))
    res_json= res.json()
    return res_json['access_token']
