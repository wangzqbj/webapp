from flask import Flask
app = Flask(__name__)

@app.route("/webapp")
def hello():
    return "<h1 style='color:blue'>你好不好啊!</h1>"

if __name__ == "__main__":
    app.run(host='127.0.0.1')
