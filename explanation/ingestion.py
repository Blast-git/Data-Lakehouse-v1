import requests
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Retrieve Alpha Vantage API key from environment
api_key = os.getenv("API_KEY")

# Define API endpoint parameters
function = "TIME_SERIES_MONTHLY"
symbol = "IBM"

# Construct API request URL
url = (
    f"https://www.alphavantage.co/query?"
    f"function={function}&symbol={symbol}&apikey={api_key}"
)

# Send request to Alpha Vantage
r = requests.get(url)

# Convert JSON response into a Python dictionary
data = r.json()

# Extract last refresh date from metadata
# Used for naming the Bronze layer file
last_refreshed = data["Meta Data"]["3. Last Refreshed"]

# Create Bronze layer directory if it does not already exist
os.makedirs("../bronze", exist_ok=True)

# Persist raw API response exactly as received
# Bronze layer should contain unmodified source data
with open(f"../bronze/{symbol}-{last_refreshed}.json", "w") as f:
    json.dump(data, f, indent=4)


#TO BE ADDED

# from pathlib import Path

# ROOT_DIR = Path(__file__).parent.parent

# bronze_dir = ROOT_DIR / "bronze"

# bronze_dir.mkdir(exist_ok=True)

# with open(bronze_dir / f"{symbol}-{last_refreshed}.json", "w") as f:
#     json.dump(data, f, indent=4)