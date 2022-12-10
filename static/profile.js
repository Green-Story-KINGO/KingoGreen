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

    $('.recipes').fadeOut(100) //

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

    $('.recipes').fadeOut(100) //

    $('.recipes').fadeIn(1000) //

}