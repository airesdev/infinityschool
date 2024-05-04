// CRUD

const form = document.querySelector("#form")
const nameInput = document.querySelector("#input-name")
const numberInput = document.querySelector("#input-number")
const emailInput = document.querySelector("#input-email")

let counter = 0
const list = [
    {
        "id": 0,
        "name": "You",
        "number": "0",
        "email": ""
    }
]

document.addEventListener("submit", (e)=>{
    e.preventDefault()
    addContact(nameInput.value, numberInput.value, emailInput.value)
    updateList()
    nameInput.value = ""
    numberInput.value = ""
    emailInput.value = ""

})

function addContact (name, number, email) {
    const newContact = {
        "id": counter += 1,
        "name": name,
        "number": number,
        "email": email
    }
    list.push(newContact)
}

function updateList () {
    document.remove(section)
    const section = document.createElement("section")
    section.classList.add("list")

    for (const contact of list) {
        const newDiv = document.createElement("div")
        newDiv.classList.add("contact")

        const nameP = document.createElement("p")
        nameP.classList.add("name")
        nameP.textContent = contact.name
        newDiv.appendChild(nameP)

        const numberP = document.createElement("p")
        numberP.classList.add("number")
        numberP.textContent = contact.number
        newDiv.appendChild(numberP)

        const emailP = document.createElement("p")
        emailP.classList.add("email")
        emailP.textContent = contact.email
        newDiv.appendChild(emailP)

        const editButton = document.createElement("a")
        editButton.classList.add("edit-button")
        editButton.href = "./"
        newDiv.appendChild(editButton)

        const deleteButton = document.createElement("a")
        deleteButton.classList.add("delete.button")
        newDiv.appendChild(deleteButton)

        section.appendChild(newDiv)
    }

    document.append(section)
}

function editContact () {
    
}

function deleteContact () {

}