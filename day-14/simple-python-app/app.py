from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! I am Mona'

if __name__ == '__main__':
    app.run()

