from flask import Flask
from pathlib import Path
import os
import requests

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
COUNT_FILE = DATA_DIR / "count.txt"

# API service address on the Docker Compose network
API_URL = os.getenv("API_URL", "http://api:5002/")  # while running locally without docker, set env API_URL to "http://localhost:5002/"


@app.route("/")
def home():
    # Create the data directory if it doesn't exist
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Read the existing visitor count
    try:
        count = int(COUNT_FILE.read_text().strip() or "0")
    except (FileNotFoundError, ValueError):
        count = 0

    # Increment and save the visitor count
    count += 1
    COUNT_FILE.write_text(str(count))

    # Communicate with the API container
    try:
        response = requests.get(API_URL, timeout=3)
        response.raise_for_status()
        api_message = response.json().get(
            "message", "No message returned"
        )
    except requests.RequestException as exc:
        api_message = f"API unavailable ({exc.__class__.__name__})"

    # Display the visitor count and API response
    return f"""
        <h1>Hello Docker!</h1>
        <p>Page visited <strong>{count}</strong> times.</p>
        <p>Message from API container:
        <strong>{api_message}</strong></p>
    """


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
