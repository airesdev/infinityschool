const form = document.querySelector(".form")
const email_input = document.querySelector("#email")
const pwd_input = document.querySelector("#pwd")
let logged_in = false

const users = [
    ["experiment@email.com", "123456"]
]

function form_reset() {
    email_input.focus()
    email_input.value = ""
    pwd_input.value = ""
}

function verification(event) {
    event.preventDefault()
    for (let values of users) {if (values[0] === email_input.value && values[1] === pwd_input.value) {logged_in = true; window.location.href = "../index.html";}}
}

form.addEventListener("submit", verification)