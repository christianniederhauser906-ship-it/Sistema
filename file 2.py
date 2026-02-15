import requests
import urllib3

# Disabilita gli allarmi che hanno bloccato gli script precedenti
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_onion(url_base64):
    import base64
    real_url = base64.b64decode(url_base64).decode()
    # Usa verify=False per saltare il muro di Jamf
    return requests.get(f"https://{real_url}", verify=False, timeout=10)
