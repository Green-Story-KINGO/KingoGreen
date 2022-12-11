
var card_name = location.href.split('?')[1];
card_name = card_name.replace('%20', ' ');


// https://juni-official.tistory.com/141
function readJSON(file, callback) {
  var rawFile = new XMLHttpRequest();
  rawFile.overrideMimeType("application/json");
  rawFile.open("GET", file, true);
  rawFile.onreadystatechange = function() {
      if (rawFile.readyState === 4 && rawFile.status == "200") {
          callback(rawFile.responseText);
      }
  }
  rawFile.send(null);
}



readJSON("static/fruits.json", function(text){
  var fruit_data = JSON.parse(text);
  
  var json_length=Object.keys(fruit_data).length;
  count=0
  let recipeBox = document.getElementById("recipes");
  for(let i=0;i<json_length;i++){
    if(Object.keys(fruit_data)[i]==card_name){
      if(fruit_data[Object.keys(fruit_data)[i]]["my_recipe"].length!=0){
        count+=1
        console.log(fruit_data[Object.keys(fruit_data)[i]]["my_recipe"]);
        
        
  
        
  
        let recipeImage = document.createElement("div")
        recipeImage.setAttribute("class", "recipeImage")
  
  
        let recipeType = document.createElement("div")
        recipeType.setAttribute("class", "recipeType")
        
        recipe_data=fruit_data[Object.keys(fruit_data)[i]]['my_recipe'];
        console.log(recipe_data[0]);
  
        for(var k=0;k<recipe_data.length;k++){
          let recipeName = document.createElement("h2")
          recipe_name=recipe_data[k]["name"]
          recipeName.innerHTML = recipe_name;
  
          let recipeInstruction = document.createElement("p")
          recipe_info=recipe_data[k]["how to make"]
          info_string = ""
          for(var j=0;j<recipe_info.length;j++){
            var order = j+1
            info_string=info_string+"<b>"+order+". "+"</b>"+ recipe_info[j] +"<br><br>";
          }
          recipeInstruction.innerHTML = info_string;
          let line = document.createElement("div")
          line.setAttribute("class", "line")
    
          recipeType.appendChild(recipeName)
          recipeType.appendChild(recipeInstruction)
    
          recipeBox.appendChild(recipeImage)
          recipeBox.appendChild(recipeType)
          recipeBox.appendChild(line)
        }
        
        
  
        
  
        
  
        
  
      }
    }
    

  }

  if(count==0){
    let recipeType = document.createElement("div")
    recipeType.setAttribute("class", "recipeType")
    let recipeName = document.createElement("h2")
    recipeName.innerHTML = "There are No Other Recipe!";
    recipeType.appendChild(recipeName)
    recipeBox.appendChild(recipeType)
  }

})


let recipeBox= document.getElementById("recipes")
let temp = document.createElement("div")
temp.setAttribute("class", "temp")

// Photo
let sidebar = document.createElement("section")
sidebar.setAttribute("class", "sidebar")

let titleWrite = document.createElement("div")
titleWrite.setAttribute("class", "titleWrite")
titleWrite.innerHTML = "Recipe Name"

let titleText = document.createElement("input")
titleText.setAttribute("type", "text")
titleText.setAttribute("class", "titleText")
titleText.setAttribute("id", "input_recipe_name")
titleText.setAttribute("placeholder", "Write a Title")

temp.appendChild(titleWrite)
temp.appendChild(titleText)

let photoTitle = document.createElement("div")
photoTitle.setAttribute("class", "photoTitle")
photoTitle.innerHTML = "Photo"

let photoInput = document.createElement("div")
photoInput.setAttribute("class", "photoInput")
photoInput.setAttribute("style", "background-image:url(static/img/banana.png)")

sidebar.appendChild(titleWrite)
sidebar.appendChild(titleText)

sidebar.appendChild(photoTitle)
sidebar.appendChild(photoInput)
temp.appendChild(sidebar)

// Text

let sidebarText = document.createElement("section")
sidebarText.setAttribute("class", "sidebar")

let inputTitle = document.createElement("div")
inputTitle.setAttribute("class", "photoTitle")
inputTitle.innerHTML = "Content"

let inputfield = document.createElement("input")
inputfield.setAttribute("type", "text")
inputfield.setAttribute("class", "contentText")
inputfield.setAttribute("id", "input_recipe_info")
inputfield.setAttribute("placeholder", "How do you make your dish?")

sidebarText.appendChild(inputTitle)
sidebarText.appendChild(inputfield)
temp.appendChild(sidebarText)

// Button place

let buttonAgain = document.createElement("section")
buttonAgain.setAttribute("class", "sidebar")
buttonAgain.setAttribute("id", "buttonPlace")


let pageFinish = document.createElement("button")
pageFinish.setAttribute("class", "finish")
pageFinish.innerHTML = "<b>Finish</b>"
buttonAgain.appendChild(pageFinish)
// pageFinish.addEventListener("click", addFunction);
pageFinish.onclick=function(){
  var recipe_name= titleText.value;
  var recipe_info= inputfield.value;
  console.log(recipe_name)
  console.log(recipe_info)
  if(typeof recipe_name!="undefined" && typeof recipe_info!="undefined" ){
    console.log("hi");
    $.ajax({
      type:'POST',
      url:'http://172.30.1.100:8080/updaterecipe',
      data:{
        "user_name": window.localStorage.getItem("curUser"),
        "fruit_name": card_name,
        "recipe_name": recipe_name,
        "recipe_info": recipe_info,
      },
      dataType: 'json',
  
      success:function(data)
      { 
        $(".recipeType").css({"display":""});
        $(".temp").css({"display":"none"});
        s=0;
        alert('Add My Recipe!');
          
      },
  
      error: function() {
          alert('error');
      }
    });
  }


  
}
temp.appendChild(buttonAgain)

recipeBox.appendChild(temp)
$(".temp").css({"display":"none"});

s =0;
function newRecipe() {
  if(s==0){
    $(".recipeType").css({"display":"none"});
    $(".temp").css({"display":""});
    s=1;
  }
  else{
    $(".recipeType").css({"display":""});
    $(".temp").css({"display":"none"});
    s=0;
  }
 
}

// function addFunction() {
//   console.log(document.getElementById("input_recipe_name"));
//   var recipe_name= document.getElementById("input_recipe_name").value;
//   var recipe_info= document.getElementById("input_recipe_info").value;
//   console.log(recipe_name)
//   console.log(recipe_info)
//   if(typeof recipe_name!="undefined" && typeof recipe_info!="undefined" ){
//     console.log("hi");
//     $.ajax({
//       type:'POST',
//       url:'http://172.30.1.100:8080/updaterecipe',
//       data:{
//         "user_name": window.localStorage.getItem("curUser"),
//         "fruit_name": card_name,
//         "recipe_name": recipe_name,
//         "recipe_info": recipe_info,
//       },
//       dataType: 'json',
  
//       success:function(data)
//       { 
//         $(".recipeType").css({"display":""});
//         $(".temp").css({"display":"none"});
//         s=0;
//         alert('Add My Recipe!');
          
//       },
  
//       error: function() {
//           alert('error');
//       }
//     });
//   }
  
// }