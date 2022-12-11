// get current fruit name
let curname = window.localStorage.getItem("curUser");

var welcome_text = "Welcome,<br> "+curname+"!";
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




// update my recipe space
function myRecipe() {
  // read user json file
  readJSON("static/user.json", function(text){
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
        // if user data has my recipe data
        if(user_data[Object.keys(user_data)[i]]["my_recipe"].length!=0){
          // add my recipe data to my recipe space
          count +=1;
          let recipeImage = document.createElement("div")
          recipeImage.setAttribute("class", "recipeImage")
    
          let recipeType = document.createElement("div")
          recipeType.setAttribute("class", "recipeType")
          
          recipe_data=user_data[Object.keys(user_data)[i]]['my_recipe'];

          for(var k=0;k<recipe_data.length;k++){
            let recipeName = document.createElement("h2")
            recipe_name=recipe_data[k]["name"]
            fruit_name = recipe_data[k]["fruit_name"];
            recipe_name= "<a href="+"http://127.0.0.1:8080/detail?"+fruit_name+" style='color: black'>"+recipe_name+"</a>";
            recipeName.innerHTML = recipe_name;

            let recipeInstruction = document.createElement("p")
            recipe_info=recipe_data[k]["how to make"]
            info_string = ""
            for(var j=0;j<recipe_info.length;j++){
              var order = j+1
              info_string=info_string+ recipe_info[j] +"<br><br>";
            }
            recipeInstruction.innerHTML = info_string;
            recipeType.appendChild(recipeName)
            recipeType.appendChild(recipeInstruction)
            recipeBox.appendChild(recipeType)
            let line = document.createElement("div")
            line.setAttribute("class", "line")
            recipeType.appendChild(line)
          }
        }
             
  
      }

    }
    
    // if user's my recipe data is empty
    if(count==0){
      let recipeType = document.createElement("div")
      recipeType.setAttribute("class", "recipeType")
      let recipeName = document.createElement("h2")
      // show "There are No My Recipe!" message
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
            
    

      
            let recipeType = document.createElement("div")
            recipeType.setAttribute("class", "recipeType")
            
            recipe_data=user_data[Object.keys(user_data)[i]]['liked_recipe'];
            console.log(recipe_data[0]);
    
            for(var k=0;k<recipe_data.length;k++){
              recipe_img=recipe_data[k]["recipe_img"]
              let recipeImage = document.createElement("div")
              recipeImage.setAttribute("class", "recipeImage")
              recipeImage.style.backgroundImage= "url("+recipe_img+")";


              let recipeName = document.createElement("h2")
              recipe_name=recipe_data[k]["name"]
              fruit_name = recipe_data[k]["fruit_name"];
              recipe_name= "<a href="+"http://127.0.0.1:8080/detail?"+fruit_name+" style='color: black'>"+recipe_name+"</a>";
              recipeName.innerHTML = recipe_name;
    
              let recipeInstruction = document.createElement("p")
              recipe_info=recipe_data[k]["how to make"]
              info_string = ""
              console.log(recipe_data[k])
              for(var j=0;j<recipe_info.length;j++){
                var order = j+1
                info_string=info_string+"<b>"+order+". "+"</b>"+ recipe_info[j] +"<br><br>";
              }
              recipeInstruction.innerHTML = info_string;
              let line = document.createElement("div")
              line.setAttribute("class", "line")
              recipeType.appendChild(recipeImage)
              recipeType.appendChild(recipeName)
              recipeType.appendChild(recipeInstruction)
        

              recipeBox.appendChild(recipeType)
              recipeType.appendChild(line)
            }
          }
          
 
        }
    
      }
      if(count==0){
        let recipeType = document.createElement("div")
        recipeType.setAttribute("class", "recipeType")
        let recipeName = document.createElement("h2")
        recipeName.innerHTML = "There are No Liked Recipe!";
        let line = document.createElement("div")
        line.setAttribute("class", "line")
        recipeType.appendChild(recipeName)
        recipeBox.appendChild(recipeType)
        recipeType.appendChild(line)
      }
      $('.recipes').fadeIn(1000) //
      
      
    })


}



