from api import api_gerencianet

def create_qrcode(location_id):
    response = api_gerencianet('GET', f'v2/loc/{location_id}/qrcode')

    if response.status_code == 200:
        return response.json()['qrcode']
