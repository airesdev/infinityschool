const input = document.querySelector("#user")
const div = document.querySelector("#divTarefas")
const form = document.querySelector("#forms")


function add(event) {
    event.preventDefault()
    // prevenir de reiniciar página
    console.log(event)
    // mostrar event
    const newItem = document.createElement("p")
    // criar elemento
    newItem.textContent = input.value
    // elemento tera o conteúdo do input
    div.appendChild(newItem)
    // adicionando à div
    input.value = ""
    // esvasiando o input
    input.focus() 
    // focando no input
}

form.addEventListener("submit", add)