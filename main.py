# Taking bitcoin price from API and using pyttsx3 to speak it out

# importing required libraries
import requests
import json
import pyttsx3

# Cryptocurrency price API
api = "https://blockchain.info/ticker"
response = requests.get(api)
data = json.loads(response.text)
btc_price = int(data["USD"]["last"])


# pyttsx3.speak(f"Bitcoin price is {btc_price} dollars.") # instant use

# speak using pyttsx3 engine
engine = pyttsx3.init()
engine.say(f"Bitcoin price is {btc_price} dollars.")
engine.runAndWait()


# printing the bitcoin price
print(btc_price)
