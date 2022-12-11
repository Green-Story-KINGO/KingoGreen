
let curname = window.localStorage.getItem("curUser");

var welcome_text = "Welcome,<br> "+curname+"!";
console.log(welcome_text);
document.getElementById("welcome_text").innerHTML=welcome_text;


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





function myRecipe() {
  
  readJSON("./static/user.json", function(text){
    var user_data = JSON.parse(text);
    
    var json_length=Object.keys(user_data).length;
    console.log(user_data);
    console.log(curname);
    $("#recipes").empty();
    $('.recipes').fadeOut(0) //
    let recipeBox = document.getElementById("recipes");
    var count =0;
    for(let i=0;i<json_length;i++){
      
      if(user_data[Object.keys(user_data)[i]]["user_name"]==curname){
        if(user_data[Object.keys(user_data)[i]]["my_recipe"].length!=0){
          count +=1;
          
  
          let recipeImage = document.createElement("div")
          recipeImage.setAttribute("class", "recipeImage")
    
    
          let recipeType = document.createElement("div")
          recipeType.setAttribute("class", "recipeType")
          
          recipe_data=user_data[Object.keys(user_data)[i]]['my_recipe'];
          console.log(recipe_data[0]);

          for(var k=0;k<recipe_data.length;k++){
            let recipeName = document.createElement("h2")
            recipe_name=recipe_data[k]["name"]
            fruit_name = recipe_data[k]["fruit_name"];
            recipe_name= "<a href="+"http://172.30.1.100:8080/detail?"+fruit_name+" style='color: black'>"+recipe_name+"</a>";
            recipeName.innerHTML = recipe_name;

            let recipeInstruction = document.createElement("p")
            recipe_info=recipe_data[k]["how to make"]
            info_string = ""
            console.log(recipe_info.length);
            for(var j=0;j<recipe_info.length;j++){
              //var order = j+1
              info_string=info_string+ recipe_info[j] +"<br><br>";
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
      recipeName.innerHTML = "There are No My Recipe!";
      recipeType.appendChild(recipeName)
      recipeBox.appendChild(recipeType)
    }
    $('.recipes').fadeIn(1000) //
  
    
  })
    

}

function favRecipe() {
    
    readJSON("./static/user.json", function(text){
      var user_data = JSON.parse(text);
      var json_length=Object.keys(user_data).length;
      console.log(user_data);
      console.log(curname);
      $("#recipes").empty();
      $('.recipes').fadeOut(0) //
      let recipeBox = document.getElementById("recipes");
      var count =0;
      for(let i=0;i<json_length;i++){
        
        if(user_data[Object.keys(user_data)[i]]["user_name"]==curname){
          if(user_data[Object.keys(user_data)[i]]["my_recipe"].length!=0){
            count+=1;
            
    
            let recipeImage = document.createElement("div")
            recipeImage.setAttribute("class", "recipeImage")
      
      
            let recipeType = document.createElement("div")
            recipeType.setAttribute("class", "recipeType")
            
            recipe_data=user_data[Object.keys(user_data)[i]]['liked_recipe'];
            console.log(recipe_data[0]);
    
            for(var k=0;k<recipe_data.length;k++){
              let recipeName = document.createElement("h2")
              recipe_name=recipe_data[k]["name"]
              fruit_name = recipe_data[k]["fruit_name"];
              recipe_name= "<a href="+"http://172.30.1.100:8080/detail?"+fruit_name+" style='color: black'>"+recipe_name+"</a>";
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
        recipeName.innerHTML = "There are No Liked Recipe!";
        recipeType.appendChild(recipeName)
        recipeBox.appendChild(recipeType)
      }
      $('.recipes').fadeIn(1000) //
      
      
    })


}



