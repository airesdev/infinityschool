const form = document.querySelector("#form")
const input = document.querySelector("#number")

const numbers = []
let soma = 0

function add (event) {
    event.preventDefault()

    numbers.push(parseInt(input.value))

    for (const number of numbers) {soma += number}

    return soma
}

form.addEventListener("submit", add)