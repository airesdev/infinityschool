const cat = document.querySelector("#cat")
const dog = document.querySelector("#dog")
const pig = document.querySelector("#pig")
const image = document.querySelector("#image")

function change(item){
    image.setAttribute("src", item)
}

cat.addEventListener("click", change("cat.jpg"))