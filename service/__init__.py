from flask import Flask, jsonify
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Security headers
talisman = Talisman(app)
talisman.force_https = False

# CORS
CORS(app)

@app.route("/accounts", methods=["GET"])
def get_accounts():
    return jsonify({"message": "My Accounts API"}), 200