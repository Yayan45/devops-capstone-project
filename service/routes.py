from flask import jsonify, request
from service import app
from service.models import Account



@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"}), 200



@app.route("/accounts", methods=["POST"])
def create_accounts():
    """Creates an Account"""
    data = request.get_json()
    account = Account(None, None, None, None)
    account.deserialize(data)
    account.create()
    return jsonify(account.serialize()), 201



@app.route("/accounts", methods=["GET"])
def list_accounts():
    """Lists all Accounts"""
    accounts = Account.all()
    results = [account.serialize() for account in accounts]
    return jsonify(results), 200



@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_accounts(account_id):
    """Reads an Account"""
    account = Account.find(account_id)
    if not account:
        return jsonify({"message": "Account not found"}), 404
    return jsonify(account.serialize()), 200



@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_accounts(account_id):
    """Updates an Account"""
    account = Account.find(account_id)
    if not account:
        return jsonify({"message": "Account not found"}), 404

    data = request.get_json()
    account.deserialize(data)
    account.update()
    return jsonify(account.serialize()), 200



@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_accounts(account_id):
    """Deletes an Account"""
    account = Account.find(account_id)
    if account:
        account.delete()
    return "", 204