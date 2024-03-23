const form = document.querySelector("#forms")

function check (event) {
    event.preventDefault()

    const name = document.querySelector("#name")
    const email = document.querySelector("#email")
    const pwd = document.querySelector("#pwd")

    if (name.value === "" || email.value === "" || pwd.value === "") {
        alert("No values sent!")
        name.focus
    }
}

form.addEventListener("submit", check)