from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='templates', static_folder='static')
bootstrap = Bootstrap(app)

@app.route('/')
def main():
    return render_template('Hola.html')


if __name__ == '__main__':
    app.run(debug=1)
