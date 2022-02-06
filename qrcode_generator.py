from create_qrcode import create_qrcode
from pyqrcode import create

def qrcode_generator(location_id):
    get_qrcode = create_qrcode(location_id)

    url = create(get_qrcode, error='H')
    url.svg('qrcode.svg', scale=10)