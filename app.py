from flask import Flask

from controllers.jogos.routes import jogos_bp

app = Flask(__name__)

app.register_blueprint(jogos_bp)


@app.route('/')
def home():
    return "pagina principal"

if __name__ == "__main__":
    app.run (debug=True)
