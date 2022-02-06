from api import api_gerencianet


def create_order(txid, data):
    response = api_gerencianet('PUT', f'v2/cob/{txid}', json=data)
    
    if response.status_code == 201:
        return response.json()['loc']['id']
    
    return {}