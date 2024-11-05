import os
from flask import Blueprint, request

command_bp = Blueprint('command', __name__)

# Vulnerable to Command Injection
@command_bp.route('/run')
def run_command():
    command = request.args.get('command')
    os.system(command)
    return "Command executed"