from flask import Flask

PORT=8000

app = Flask(__name__)

@app.route('/')
@app.route('/hello-world')
def hello():
   return "Hello World!"

if __name__ == '__main__':
   app.run('', PORT)
