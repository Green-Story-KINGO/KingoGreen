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

    $("#recipes").empty()

    let recipeBox = document.getElementById("recipes");

    let recipeImage = document.createElement("div")
    recipeImage.setAttribute("class", "recipeImage")


    let recipeType = document.createElement("div")
    recipeType.setAttribute("class", "recipeType")

    let recipeName = document.createElement("h2")
    recipeName.innerHTML = "Cabbage Greens"

    let recipeInstruction = document.createElement("p")
    recipeInstruction.innerHTML = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat aperiam molestias ratione tenetur voluptatum expedita sint, quaerat facere tempora amet officiis maiores eaque pariatur dolorum reiciendis? Obcaecati maiores possimus quas.";

    let line = document.createElement("div")
    line.setAttribute("class", "line")

    recipeType.appendChild(recipeName)
    recipeType.appendChild(recipeInstruction)

    recipeBox.appendChild(recipeImage)
    recipeBox.appendChild(recipeType)
    recipeBox.appendChild(line)

    $('.recipes').fadeOut(200);
    $('.recipes').fadeIn(1000) //

}

function favRecipe() {



    $('#recipes').empty()

    let recipeBox = document.getElementById("recipes");

    let recipeImage = document.createElement("div")
    recipeImage.setAttribute("class", "recipeImage")


    let recipeType = document.createElement("div")
    recipeType.setAttribute("class", "recipeType")

    let recipeName = document.createElement("h2")
    recipeName.innerHTML = "Bananan Smoothie"

    let recipeInstruction = document.createElement("p")
    recipeInstruction.innerHTML = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat aperiam molestias ratione tenetur voluptatum expedita sint, quaerat facere tempora amet officiis maiores eaque pariatur dolorum reiciendis? Obcaecati maiores possimus quas.";

    let line = document.createElement("div")
    line.setAttribute("class", "line")

    recipeType.appendChild(recipeName)
    recipeType.appendChild(recipeInstruction)

    recipeBox.appendChild(recipeImage)
    recipeBox.appendChild(recipeType)
    recipeBox.appendChild(line)

    $('.recipes').fadeOut(200);
    $('.recipes').fadeIn(1000) //

}


readJSON("static/fruits.json", function(text){
  var fruit_data = JSON.parse(text);
  
  
  var best_time_from = fruit_data[card_name]['best time'][0];
  var best_time_to = fruit_data[card_name]['best time'][1];
  var effect = fruit_data[card_name]['effect'];
  var how_eat = fruit_data[card_name]['how to eat'];
  var why_eat = fruit_data[card_name]['why to eat'];
  document.getElementById("detail_name").innerText = card_name;
  document.getElementById("detail_nutrients").innerText = nutrient[0]+', '+nutrient[1];
  document.getElementById("detail_pick").innerText = how_pick;
  document.getElementById("datail_season").innerText = season;
  
  document.getElementById("detail_benefit1").innerText = effect[0];
  document.getElementById("detail_benefit2").innerText = effect[1];
  document.getElementById("detail_benefit3").innerText = effect[2];
  document.getElementById("detail_benefit4").innerText = effect[3];
})
