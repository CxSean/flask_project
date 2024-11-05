import sqlite3
from flask import Blueprint

user_bp = Blueprint('user', __name__)

# Vulnerable to SQL Injection
@user_bp.route('/user/<username>')
def get_user(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return str(user)