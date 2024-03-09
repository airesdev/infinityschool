// const input = document.querySelector("#user")
// const btn = document.querySelector("#btn")
// const resultado = document.querySelector("#resultado")

// function exibirEmail() {
//     resultado.textContent += input.value
// }

// btn.addEventListener("click", exibirEmail)

const input = document.querySelector("#user")
const btn = document.querySelector("#btn")
const resultado = document.querySelector("#resultado")

btn.addEventListener("click", () => resultado.textContent = input.value)