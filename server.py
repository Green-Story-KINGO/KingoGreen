
from flask import Flask, render_template, jsonify, request, url_for
from flask_cors import CORS
import json
from collections import OrderedDict

app = Flask(__name__)
CORS(app)


# render login.html templates
@app.route('/')
def login():
    return render_template('login.html')
# render home.html templates
@app.route('/home')
def home():
    return render_template('home.html')
# render tag.html templates
@app.route('/tag')
def tag():
    return render_template('tag.html')
# render all.html templates
@app.route('/all')
def all():
    return render_template('all.html')
# render detail.html templates
@app.route('/detail')
def detail():
    return render_template('detail.html')
# render morerecipe.html templates
@app.route('/morerecipe')
def morerecipe():
    return render_template('moreRecipe.html')
# render profile.html templates
@app.route('/profile')
def profile():
    return render_template('profile.html')

# sign up function
@app.route('/makeid', methods=['POST'])
def makeId():
  result={}
  data = request.form.to_dict()
  user_name = data['username']
  email = data['email']
  pw = data['pw']
  cfpw = data['cfpw']

  json_data=None
  # read user json file
  with open('static/user.json', 'r', encoding="utf-8")as f:
    json_data = json.load(f)
  
  for i in range(len(json_data.keys())):
    key = list(json_data.keys())[i]
    # if user is already existed, return {"success":0}
    if(key==email or json_data[key]['user_name']==user_name):
      result["success"]=0
      return result
  new_user = OrderedDict()
  # append new user data to user json file
  json_data[email]={
    "user_name": user_name,
    "password": pw,
    "liked_recipe": [],
    "my_recipe": []
  }
  with open('static/user.json', 'w', encoding="utf-8")as make_file:
    json.dump(json_data, make_file, ensure_ascii=False, indent="\t")

  
  result["success"]=1
  # return {"success":0}
  return result

# login function
@app.route('/updateuser', methods=['POST'])
def updateUser():
  result={}
  data = request.form.to_dict()
  user_name = data['user_name']
  pw = data['pw']
  json_data=None
  # read user json file
  with open('static/user.json', 'r', encoding="utf-8")as f:
    json_data = json.load(f)
  
  exist = 0
  
  for i in range(len(json_data.keys())):
    key = list(json_data.keys())[i]
    if(json_data[key]['user_name']==user_name and json_data[key]['password']== pw):
      exist=1
      break
  # if user data is existed, return {"success":0, "user_name":user_name}
  if(exist==1):
    result["success"]=1
    print(user_name)
    result["user_name"]=user_name
    return result

  result["success"]=0

  return result

# update recipe
@app.route('/updaterecipe', methods=['POST'])
def updateRecipe():
  result={}
  data = request.form.to_dict()
  user_name = data['user_name']
  fruit_name = data['fruit_name']
  recipe_name = data['recipe_name']
  recipe_info = data['recipe_info']
  json_data=None
  # update fruit json file
  # read fruit json file
  with open('static/fruits.json', 'r', encoding="utf-8")as f:
    json_data = json.load(f)
  for i in range(len(json_data.keys())):
    key = list(json_data.keys())[i]
    if(key==fruit_name):
      # append my recipe data to fruit json file
      json_data[key]['my_recipe'].append({
        "fruit_name":fruit_name,
        "name": recipe_name,
				"how to make": [recipe_info]
      })
      break
  # update fruit json file
  with open('static/fruits.json', 'w', encoding="utf-8")as make_file:
    json.dump(json_data, make_file, ensure_ascii=False, indent="\t")

  # update user json
  data = request.form.to_dict()

  user_data=None
  # read fruit json file
  with open('static/user.json', 'r', encoding="utf-8")as f2:
    user_data = json.load(f2)
  
  
  for i in range(len(user_data.keys())):
    key = list(user_data.keys())[i]
    if(user_data[key]["user_name"]==user_name):
      # append my recipe data to user json file
      user_data[key]['my_recipe'].append({
        "fruit_name":fruit_name,
        "name": recipe_name,
				"how to make": [recipe_info]
      })
      break
  # update user json file
  with open('static/user.json', 'w', encoding="utf-8")as make_file2:
    json.dump(user_data, make_file2, ensure_ascii=False, indent="\t")

  return result

# update user's liked recipe
@app.route('/updatefav', methods=['POST'])
def updateFav():
  result={}
  data = request.form.to_dict()
  user_name = data['user_name']
  fruit_name = data['fruit_name']
  recipe_name = data['recipe_name']
  recipe_img = data['recipe_img']
  recipe_info = json.loads(data['recipe_info'])['recipe']
  
  json_data=None
  # read user json file
  with open('static/user.json', 'r', encoding="utf-8")as f:
    json_data = json.load(f)
  
  result['exist']=1
  for i in range(len(json_data.keys())):
    key = list(json_data.keys())[i]
    if(json_data[key]["user_name"]==user_name):
      check =0
      order = -1
      for j in range(len(json_data[key]['liked_recipe'])):
        if(json_data[key]['liked_recipe'][j]["fruit_name"]==fruit_name):
          order = j
          check=1
          result['exist']=0
      # if my recipe data is not existed
      if(check==0):
        # append my recipe data to user json file
        json_data[key]['liked_recipe'].append({
          "fruit_name":fruit_name,
          "name": recipe_name,
          "how to make": recipe_info,
          "recipe_img" : recipe_img
        })
      # if my recipe data is already existed
      else:
        # delete that my recipe data in user json file
        del json_data[key]['liked_recipe'][order]
      break
  # update user json file
  with open('static/user.json', 'w', encoding="utf-8")as make_file:
    json.dump(json_data, make_file, ensure_ascii=False, indent="\t")
  
  return result




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True, threaded=True)