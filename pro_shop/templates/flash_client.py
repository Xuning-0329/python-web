from flask import Flask, send_file

app = Flask(__name__,static_url_path='/assets',static_folder='assets')

@app.route('/index')
def index():
    #首页
    return send_file('templates/index.html')

if __name__ == '__main__':
    app.run(debug=True)