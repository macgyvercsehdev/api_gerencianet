from qrcode_generator import qrcode_generator
from create_order import create_order

def create_charge(txid, payload):
    location_id = create_order(txid=txid, data=payload)
    qrcode = qrcode_generator(location_id)

    return qrcode