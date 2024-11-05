import pickle
from flask import Blueprint, request

deserialize_bp = Blueprint('deserialize', __name__)

# Vulnerable to Insecure Deserialization
@deserialize_bp.route('/deserialize', methods=['POST'])
def deserialize():
    data = request.data
    obj = pickle.loads(data)
    return str(obj)