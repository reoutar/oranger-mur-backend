import os
import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Autorise les appels depuis ton site GitHub Pages

# Le token Kobo sera stocké dans une variable d'environnement KOBO_TOKEN
KOBO_TOKEN = os.environ.get("KOBO_TOKEN")
KOBO_URL = "https://kf.kobotoolbox.org/api/v2/assets/aQL229knhzDHyFjHkrJKax/data/"

@app.get("/api/oranger-data")
def oranger_data():
    if not KOBO_TOKEN:
        return jsonify({"error": "KOBO_TOKEN not configured"}), 500

    headers = {"Authorization": f"Token {KOBO_TOKEN}"}
    r = requests.get(KOBO_URL, headers=headers)
    r.raise_for_status()
    data = r.json()

    # On renvoie les données telles quelles (results + métadonnées)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
