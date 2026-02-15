import requests
import ui

# I tuoi link RAW di GitHub (Sostituisci 'TUO_USER' con il tuo nome vero)
URL_AUTH = "https://raw.githubusercontent.com/TUO_USER/REPO/main/auth.py"
URL_DB = "https://raw.githubusercontent.com/TUO_USER/REPO/main/database.txt"
URL_ENGINE = "https://raw.githubusercontent.com/TUO_USER/REPO/main/engine.py"

def bootstrap():
    # 1. Scarica ed esegue la Password
    auth_code = requests.get(URL_AUTH).text
    exec(auth_code)
    
    # 2. Se la password passa, scarica il database e il motore
    # (Logica da attivare dopo il login)
    print("Sistema sincronizzato con GitHub.")

if __name__ == '__main__':
    bootstrap()
