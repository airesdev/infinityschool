const input = document.querySelector("#username")
const form = document.querySelector("#form")
const section = document.querySelector("#section")

document.addEventListener("submit", (e)=>{
    e.preventDefault()
    getUser()
})

async function getUser() {
    try {
        const requisition = await fetch(`https://api.github.com/users/${input.value}`)
        const resposta = await requisition.json()

        if (resposta.message != "Not Found") {
            showUser(resposta)
        } else {
            console.log(resposta.message)
        }
    } catch (error) {
        console.log(error)
        console.log("the API triped on a rock and fell, oops...")
    }
}

function showUser(resposta) {
    const pfp = document.createElement("img")
    pfp.src = resposta.avatar_url
    section.appendChild(pfp)

    const name = document.createElement("h1")
    name.textContent = resposta.name
    section.appendChild(name)
    
    const bio = document.createElement("p")
    bio.textContent = resposta.bio
    section.appendChild(bio)

    // const location = document.createElement("p")
    // location.textContent = resposta.location
    // section.appendChild(location)

    // const html = document.createElement("a")
    // html.href = resposta.html_url
    // section.appendChild(html)

    // const repos = document.createElement("a")
    // a.href = resposta.html_url
    // section.appendChild(location)

    // const blog = document.createElement("a")
    // a.href = resposta.html_url
    // section.appendChild(location)
}