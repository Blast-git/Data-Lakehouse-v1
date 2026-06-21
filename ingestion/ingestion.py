import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.getenv("API_KEY")
function = "TIME_SERIES_MONTHLY"
symbol = "IBM"

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}'

r = requests.get(url)

data = r.json()


last_refreshed = data["Meta Data"]["3. Last Refreshed"]

os.makedirs("../bronze", exist_ok=True)

with open(f"../bronze/{symbol}-{last_refreshed}.json",'w') as f:
    json.dump(data,f,indent=4)

