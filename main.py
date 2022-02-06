from create_charge import create_charge
from pyqrcode import create

data = {
    "calendario": {
        "expiracao": 3600
    },
    "devedor": {
        "cpf": "42065260017",
        "nome": "Francisco dos Santos"
    },
    "valor": {
        "original": "1.12"
    },
    "chave": "bota a chave aqui",
    "solicitacaoPagador": "Informe o número ou identificador do pedido."
}
txid = 'kw8uknbkxxu0y6eworb8r40pv9ggst'

create_charge(payload=data, txid=txid)
