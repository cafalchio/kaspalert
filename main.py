import requests
import pyglet
import time

def get_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=kaspa&vs_currencies=usd"
    sound = pyglet.media.load('gilfoyle_alert.mp3')
    while True:
        try:
            response = requests.get(url, timeout=1)
            response.raise_for_status()
            data = response.json()
            price = data.get('kaspa', {}).get('usd')
            if response.status_code == 200 and price >= 0.2:
                sound.play()
                time.sleep(2)
                return
            else:
                time.sleep(60)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching price: {e}")



if __name__ == "__main__":
    get_price()
