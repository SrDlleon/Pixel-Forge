from flask import Flask, render_template
import os

from controllers.jogos.routes import jogos_bp
from controllers.desenvolvedoras.routes import desenvolvedora_bp
from controllers.clientes.routes import clientes_bp

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or os.urandom(24)

app.register_blueprint(jogos_bp)
app.register_blueprint(desenvolvedora_bp)
app.register_blueprint(clientes_bp)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run (debug=True)
