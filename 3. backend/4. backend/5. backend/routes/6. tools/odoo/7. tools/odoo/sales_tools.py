import requests
from tools.odoo.connection import authenticate
from backend.config import *

def top_productos_pdv():

    uid = authenticate()

    payload = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
            "service": "object",
            "method": "execute_kw",
            "args": [
                ODOO_DB,
                uid,
                ODOO_PASSWORD,
                "product.product",
                "search_read",
                [[]],
                {
                    "fields": ["name"]
                }
            ]
        }
    }

    response = requests.post(
        f"{ODOO_URL}/jsonrpc",
        json=payload
    )

    return response.json()
