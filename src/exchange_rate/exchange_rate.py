import requests
import json

# Needed for request data
API_KEY = 'ac0643efadf17681b99b8e77'

source_currency = 'USD'
target_currency = 'RUB'

url = 'https://v6.exchangerate-api.com/v6/' + API_KEY + '/latest/' + source_currency

exchange_data = requests.get(url).json()

exchange_rate = exchange_data['conversion_rates'][target_currency]

print('Курс валют: 1', source_currency, 'оценивается в', exchange_rate, target_currency)