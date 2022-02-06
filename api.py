from requests.auth import HTTPBasicAuth
from requests import request, post
from dotenv import load_dotenv
from os import getenv

load_dotenv('.env')

def _token():
    response = post(
        url='%s/oauth/token' % getenv('URL_PROD'),
        auth=HTTPBasicAuth(
            getenv('CLIENT_ID_PROD'),
            getenv('CLIENT_SECRET_PROD')
        ),
        json={
            'grant_type': 'client_credentials'
        },
        cert=getenv('CERTIFICADO_PROD'),
    )

    return response.json()['access_token']

def api_gerencianet(method, endpoint, **kwargs):
    return request(
        method,
        '%s/%s' % (getenv('URL_PROD'), endpoint),
        headers={
            'Authorization': f"Bearer {_token()}",
        },
        cert=getenv('CERTIFICADO_PROD'), 
        **kwargs,
    )
