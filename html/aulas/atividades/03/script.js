const form = document.querySelector("#form")
const list = document.querySelector("#list")

function add (event) {
    event.preventDefault()

    const input = document.querySelector("#text")

    const new_el = document.createElement("li")
    new_el.textContent = input.value
    list.appendChild(new_el)
    input.value = ""
    input.focus
}

form.addEventListener("submit", add)