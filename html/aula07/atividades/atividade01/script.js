const user = document.querySelector("#user")

function getValue() {
    console.log(user.value)
}

user.addEventListener("keydown", getValue)