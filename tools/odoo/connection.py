import requests
from backend.config import *

def authenticate():

    payload = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
            "service": "common",
            "method": "login",
            "args": [
                ODOO_DB,
                ODOO_USERNAME,
                ODOO_PASSWORD
            ]
        }
    }

    response = requests.post(
        f"{ODOO_URL}/jsonrpc",
        json=payload
    )

    return response.json()["result"]
