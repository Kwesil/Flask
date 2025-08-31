from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/admin')
def admin_page():
    return "admin's world"

if __name__ == '__main__':
    app.debug = True
    app.run()