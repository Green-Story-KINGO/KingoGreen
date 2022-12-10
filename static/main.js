
function fillHeart() {

    $('#heart').empty()
    let heart = document.getElementById("heart")

    let fill = document.createElement("span")
    fill.setAttribute("class", "bi bi-heart-fill")
    fill.style.color = "red";
    fill.style.height = "40px";

    heart.appendChild(fill)
    
}


