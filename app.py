from flask import Flask
from routes.user import user_bp
from routes.command import command_bp
from routes.greet import greet_bp
from routes.deserialize import deserialize_bp

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(command_bp)
app.register_blueprint(greet_bp)
app.register_blueprint(deserialize_bp)

if __name__ == '__main__':
    app.run(debug=True)