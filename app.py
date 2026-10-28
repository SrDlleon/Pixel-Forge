from flask import Flask
from controllers.desenv_controller import desenvolvedora_bp

app = Flask(__name__)

@app.route("/login")
def login:
    request.form('nome')
    request.form('idade')


if __name__ == "__main__":
    app.run (debug=True)