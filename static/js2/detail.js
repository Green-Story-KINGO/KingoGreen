var card_name = location.href.split('?')[1];
card_name = card_name.replace('%20', ' ');
console.log(card_name);
let curname = window.localStorage.getItem("curUser");
card_recipe_name = "";
card_recipe_info = null;

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
  
  var info = fruit_data[card_name]['info'];
  var nutrient = fruit_data[card_name]['nutrient'];
  var how_pick = fruit_data[card_name]['how to choose'];
  var best_time_from = "";
  var best_time_to = "";
  switch(fruit_data[card_name]['best time'][0]){
    case 1:
      best_time_from="January";
      break;
    case 2:
      best_time_from="February";
      break;
    case 3:
      best_time_from="March";
      break;
    case 4:
      best_time_from="April";
      break;
    case 5:
      best_time_from="May";
      break;
    case 6:
      best_time_from="June";
      break;
    case 7:
      best_time_from="July";
      break;
    case 8:
      best_time_from="August";
      break;   
    case 9:
      best_time_from="September";
      break;
    case 10:
      best_time_from="October";
      break;
    case 11:
      best_time_from="November";
      break;
    case 12:
      best_time_from="December";
      break;}
    switch(fruit_data[card_name]['best time'][1]){
      case 1:
        best_time_to="January";
        break;
      case 2:
        best_time_to="February";
        break;
      case 3:
        best_time_to="March";
        break;
      case 4:
        best_time_to="April";
        break;
      case 5:
        best_time_to="May";
        break;
      case 6:
        best_time_to="June";
        break;
      case 7:
        best_time_to="July";
        break;
      case 8:
        best_time_to="August";
        break;   
      case 9:
        best_time_to="September";
        break;
      case 10:
        best_time_to="October";
        break;
      case 11:
        best_time_to="November";
        break;
      case 12:
        best_time_to="December";
        break;}
  var season =  "";
  if(best_time_from=="January" && best_time_to=="December"){
    season = "All year around";
  }
  else{
    season = best_time_from+" ~ "+best_time_to;
  }
  
  var best_time_from = fruit_data[card_name]['best time'][0];
  var best_time_to = fruit_data[card_name]['best time'][1];
  var effect = fruit_data[card_name]['effect'];
  var img_path = fruit_data[card_name]['img'];
  var video_path = fruit_data[card_name]['youtube'];

  var recipe= fruit_data[card_name]['rec_recipe'];
  var recipe_name = recipe[0]["name"];
  var recipe_info = recipe[0]["how to make"];
  card_recipe_name=recipe_name;
  card_recipe_info=recipe_info;

  document.getElementById("detail_name").innerText = card_name;
  document.getElementById("detail_nutrients").innerText = nutrient[0]+', '+nutrient[1];
  document.getElementById("detail_pick").innerText = how_pick;
  document.getElementById("datail_season").innerText = season;
  document.getElementById("foodImage").style.backgroundImage = "url("+img_path+")";
  document.getElementById("detail_info").innerText=info;
  console.log(img_path);
  document.getElementById("detail_benefit1").innerText = effect[0];
  document.getElementById("detail_benefit2").innerText = effect[1];
  document.getElementById("detail_benefit3").innerText = effect[2];
  document.getElementById("detail_benefit4").innerText = effect[3];
  document.getElementById("more_button").href = "http://172.30.1.100:8080/morerecipe?"+card_name;
  
  var info = "<h3 id='r_name'>"+recipe_name+"</h3>"+"<br><br>";
  for(var i=0;i<recipe_info.length;i++){
    order = i+1;
    info = info +order+". "+recipe_info[i]+"<br><br>";
  }
  document.getElementById("detail_recipe_name").innerHTML = info;
  document.getElementById("video_path1").innerHTML = video_path[0];
  document.getElementById("video_path2").innerHTML = video_path[1];

})
var check =0;
readJSON("./static/user.json", function(text){
  var user_data = JSON.parse(text);
  
  var json_length=Object.keys(user_data).length;
  for(let i=0;i<json_length;i++){
    
    if(user_data[Object.keys(user_data)[i]]["user_name"]==curname){
      var liked_recipe_length=user_data[Object.keys(user_data)[i]]["liked_recipe"].length
      for(let j=0;j<liked_recipe_length;j++){
        if(user_data[Object.keys(user_data)[i]]["liked_recipe"][j]["fruit_name"]==card_name){
          check =1;
          break
        }
      }
      
    }
  }

  //$('#heart').remove()
  let heart = document.createElement("button")
  heart.style.position="relatve"; 
  heart.style.left="320px";
  heart.style.height="40px";
  heart.setAttribute("class", "btn btn-link" )
  heart.setAttribute("id", "heart")
  heart.addEventListener("click", fillHeart);
  //let r_name = document.getElementById("r_name")
  let fill = document.createElement("span")
  if(check==1){
    fill.setAttribute("class", "bi bi-heart-fill")
  }
  else{
    fill.setAttribute("class", "bi bi-heart")
  }
  
  fill.style.color = "red";
  fill.style.height = "40px";
  //fill.onclick="fillHeart()"
  

  heart.appendChild(fill)
  a=document.getElementById("r_name");
  a.appendChild(heart)
});


function fillHeart() {
  var new_info ={"recipe":card_recipe_info};
  $.ajax({
    type:'POST',
    url:'http://172.30.1.100:8080/updatefav',
    data:{
      "user_name": window.localStorage.getItem("curUser"),
      "fruit_name": card_name,
      "recipe_name": card_recipe_name,
      "recipe_info": JSON.stringify(new_info),
    },
    dataType: 'json',

    success:function(data)
    { 
      $('#heart').remove()
      let heart = document.createElement("button")
      heart.style.position="relatve"; 
      heart.style.left="320px";
      heart.style.height="40px";
      heart.setAttribute("class", "btn btn-link" )
      heart.setAttribute("id", "heart")
      heart.addEventListener("click", fillHeart);
      //let r_name = document.getElementById("r_name")
      let fill = document.createElement("span")
      if(data['exist']==1){
        fill.setAttribute("class", "bi bi-heart-fill")
      }
      else{
        fill.setAttribute("class", "bi bi-heart")
      }
      
      fill.style.color = "red";
      fill.style.height = "40px";
      //fill.onclick="fillHeart()"
    
  
      heart.appendChild(fill)
      a=document.getElementById("r_name");
      a.appendChild(heart)
      
    },

    error: function() {
        alert('error');
    }
    });
  //   var check =0;
  // readJSON("./static/user.json", function(text){
  //     var user_data = JSON.parse(text);
    
  //   var json_length=Object.keys(user_data).length;
  //   for(let i=0;i<json_length;i++){
      
  //     if(user_data[Object.keys(user_data)[i]]["user_name"]==curname){
  //       var liked_recipe_length=user_data[Object.keys(user_data)[i]]["liked_recipe"].length
  //       for(let j=0;j<liked_recipe_length;j++){
  //         console.log(user_data[Object.keys(user_data)[i]]["liked_recipe"][j]["fruit_name"])
  //         console.log(card_name);
  //         if(user_data[Object.keys(user_data)[i]]["liked_recipe"][j]["fruit_name"]==card_name){
  //           check =1;
  //           break
  //         }
  //       }
        
  //     }
  //   }
  
    
    
  // });
  
}