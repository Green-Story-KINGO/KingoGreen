
from flask import Flask, render_template, jsonify, request, url_for
from flask_cors import CORS
import json
from collections import OrderedDict

app = Flask(__name__)
CORS(app)



@app.route('/')
def home():
    return render_template('login.html')
@app.route('/home')
def login():
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



@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/makeid', methods=['POST'])
def makeId():
  result={}
  data = request.form.to_dict()
  user_name = data['username']
  email = data['email']
  pw = data['pw']
  json_data=None
  with open('user.json', 'r', encoding="utf-8")as f:
    json_data = json.load(f)
  
  for i in range(len(json_data.keys())):
    key = list(json_data.keys())[i]
    if(key==email or json_data[key]['user_name']==user_name):
      result["success"]=0
      return result
  new_user = OrderedDict()
  json_data[email]={
    "user_name": user_name,
    "password": pw,
    "liked_recipe": [],
    "my_recipe": []
  }
  with open('user.json', 'w', encoding="utf-8")as make_file:
    json.dump(json_data, make_file, ensure_ascii=False, indent="\t")

  
  result["success"]=1
  return result

@app.route('/updateuser', methods=['POST'])
def updateUser():
  result={}
  data = request.form.to_dict()
  email = data['email']
  pw = data['pw']
  json_data=None
  with open('user.json', 'r', encoding="utf-8")as f:
    json_data = json.load(f)
  
  exist = 0
  
  for i in range(len(json_data.keys())):
    key = list(json_data.keys())[i]
    if(key==email and json_data[key]['password']== user_name):
      exist=1
  
  if(exist==1):
    result["success"]=1
    result["user_name"]=1
    return result

  result["success"]=0

  return result



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)