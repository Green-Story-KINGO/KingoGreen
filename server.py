
from flask import Flask, render_template, jsonify, request, url_for
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

@app.route('/morerecipe')
def morerecipe():
    return render_template('moreRecipe.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)