import requests
import time


while True:
    token  = '5255695583:AAGLT4xCXy7MZdLkGWAlRyIC6kwcRk0CBuQ'
    url_base = f'https://api.telegram.org/bot{token}/getUpdates'
    resultado = requests.get(url_base)
    print(resultado.json())
    time.sleep(10)
