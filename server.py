
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
  cfpw = data['cfpw']

  json_data=None
  with open('static/user.json', 'r', encoding="utf-8")as f:
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
  with open('static/user.json', 'w', encoding="utf-8")as make_file:
    json.dump(json_data, make_file, ensure_ascii=False, indent="\t")

  
  result["success"]=1
  return result

@app.route('/updateuser', methods=['POST'])
def updateUser():
  result={}
  data = request.form.to_dict()
  user_name = data['user_name']
  pw = data['pw']
  json_data=None
  with open('static/user.json', 'r', encoding="utf-8")as f:
    json_data = json.load(f)
  
  exist = 0
  
  for i in range(len(json_data.keys())):
    key = list(json_data.keys())[i]
    print(json_data[key]['password'])
    print(type(pw))
    print(json_data[key]['user_name'])
    print(type(user_name))
    if(json_data[key]['user_name']==user_name and json_data[key]['password']== pw):
      exist=1
      break
  
  if(exist==1):
    result["success"]=1
    print(user_name)
    result["user_name"]=user_name
    return result

  result["success"]=0

  return result

@app.route('/updaterecipe', methods=['POST'])
def updateRecipe():
  result={}
  data = request.form.to_dict()
  user_name = data['user_name']
  fruit_name = data['fruit_name']
  recipe_name = data['recipe_name']
  recipe_info = data['recipe_info']
  json_data=None
  with open('static/fruits.json', 'r', encoding="utf-8")as f:
    json_data = json.load(f)
  
  
  for i in range(len(json_data.keys())):
    key = list(json_data.keys())[i]
    if(key==fruit_name):
      json_data[key]['my_recipe'].append({
        "fruit_name":fruit_name,
        "name": recipe_name,
				"how to make": recipe_info
      })
      break
  
  with open('static/fruits.json', 'w', encoding="utf-8")as make_file:
    json.dump(json_data, make_file, ensure_ascii=False, indent="\t")

  # update user json
  data = request.form.to_dict()

  user_data=None
  with open('static/user.json', 'r', encoding="utf-8")as f2:
    user_data = json.load(f2)
  
  
  for i in range(len(user_data.keys())):
    key = list(user_data.keys())[i]
    if(user_data[key]["user_name"]==user_name):
      user_data[key]['my_recipe'].append({
        "fruit_name":fruit_name,
        "name": recipe_name,
				"how to make": [recipe_info]
      })
      break
  
  with open('static/user.json', 'w', encoding="utf-8")as make_file2:
    json.dump(user_data, make_file2, ensure_ascii=False, indent="\t")

  return result

@app.route('/updatefav', methods=['POST'])
def updateFav():
  result={}
  data = request.form.to_dict()
  user_name = data['name']
  recipe_name = data['recipe_name']
  recipe_info = data['recipe_info']
  json_data=None
  with open('static/user.json', 'r', encoding="utf-8")as f:
    json_data = json.load(f)
  
  exist = 0
  
  for i in range(len(json_data.keys())):
    key = list(json_data.keys())[i]
    if(json_data[key]["user_name"]==name):
      json_data[key]['liked_recipe'].append({
        "name": recipe_name,
				"how to make": recipe_info
      })
      break
  
  with open('static/user.json', 'w', encoding="utf-8")as make_file:
    json.dump(json_data, make_file, ensure_ascii=False, indent="\t")

  return result




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)