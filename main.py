from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return '<h1>Hola mundo!</h1>'


if __name__ == '__main__':
    app.run(debug=1)
