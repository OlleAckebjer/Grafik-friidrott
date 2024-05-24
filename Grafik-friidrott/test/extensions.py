from flask_socketio import SocketIO 


socketio = SocketIO()


email = "olle.ackebjer@gmail.com"
psw = "Friidrott18"

import requests


login_url = f"https://api.admin.rosterathletics.com/api/login"

# Skapa ett Session-objekt för att hantera cookies
session = requests.Session()


# Utför Curl-anropet för att logga in och spara cookies
login_data = {
    'username': email,
    "password": psw
}


session.post(login_url, data=login_data)
print("LOGGED IN")