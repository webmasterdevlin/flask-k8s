from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return {"id": "23rhd9whf3oa", "username": "this is flask"}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
