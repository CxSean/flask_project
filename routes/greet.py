from flask import Blueprint, request, render_template

greet_bp = Blueprint('greet', __name__)

# Vulnerable to Cross-Site Scripting (XSS)
@greet_bp.route('/greet')
def greet():
    name = request.args.get('name')
    return render_template('greet.html', name=name)