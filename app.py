from flask import Flask

app = Flask(__name__)


def main():
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)


if __name__ == '__main__':
    main()
