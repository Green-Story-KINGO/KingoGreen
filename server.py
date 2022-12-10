
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/tag')
def tag():
    return render_template('tag.html')

@app.route('/all')
def all():
    return render_template('all.html')

@app.route('/detail')
def detail():
    return render_template('detail.html')







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)