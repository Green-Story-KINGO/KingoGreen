<<<<<<< HEAD
function newPage() {
  window.location.href = "detail.html";
=======

function fillHeart() {

    $('#heart').empty()
    let heart = document.getElementById("heart")

    let fill = document.createElement("span")
    fill.setAttribute("class", "bi bi-heart-fill")
    fill.style.color = "red";
    fill.style.height = "40px";

    heart.appendChild(fill)
    
}

function newRecipe() {
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
  titleText.setAttribute("placeholder", "Write a Title")

  temp.appendChild(titleWrite)
  temp.appendChild(titleText)

  let photoTitle = document.createElement("div")
  photoTitle.setAttribute("class", "photoTitle")
  photoTitle.innerHTML = "Photo"

  let photoInput = document.createElement("div")
  photoInput.setAttribute("class", "photoInput")
  photoInput.setAttribute("style", "background-image:url(/img/camera.png)")

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
  pageFinish.innerHTML = "Finish"

  buttonAgain.appendChild(pageFinish)

  temp.appendChild(buttonAgain)

  recipeBox.appendChild(temp)

  pageFinish.addEventListener("click" , addFunction)


  

   
}

function addFunction() {



    $('.temp').remove()


>>>>>>> 4499c01a46484d25a60987c3a24b3cc36f272615

}