from flask import Flask, render_template

from controllers.jogos.routes import jogos_bp
from controllers.desenvolvedoras.routes import desenvolvedora_bp

app = Flask(__name__)

app.register_blueprint(jogos_bp)
app.register_blueprint(desenvolvedora_bp)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run (debug=True)
