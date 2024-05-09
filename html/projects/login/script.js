const form = document.querySelector(".form")
const email_input = document.querySelector(".email")
const pwd_input = document.querySelector(".pwd")
const submit_btn = document.querySelector(".submit")
let logged_in = false

const users = [
    ["joao@gmail.com", "123456"],
    ["abel@gmail.com", "234567"],
    ["maria@gmail.com", "345678"],
    ["antonio@gmail.com", "456789"],
    ["ana@gmail.com", "567890"],
    ["test", "123"]
]

function form_reset() {
    email_input.focus()
    email_input.value = ""
    pwd_input.value = ""
}

function verify(event) {
    event.preventDefault()
    // const valuesSent = [email_input.value, pwd_input.value]
    // console.log(valuesSent)

    for (let values of users) {
        if (values[0] === email_input.value && values[1] === pwd_input.value) {logged_in = true; break}
        else {logged_in = false; form_reset}
    }

    console.log(logged_in)
}

form.addEventListener("submit", verify)