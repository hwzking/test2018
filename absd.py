from flask import Flask


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index_1():
    return '12'


if __name__ == '__main__':
    app.run(debug=True, port=5003)

