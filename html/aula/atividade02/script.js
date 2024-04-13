const list = [15, 29, 35, 17, 61, 18, 33, 25, 21, 10]
const listFilter = list.filter((el) => el >= 18)
const div = document.createElement("div")
document.body.appendChild(div)
div.classList.add("caixinha")

function addP(el) {
    const p = document.createElement("p")
    p.textContent = el
    div.append(p)
}

listFilter.map((el) => addP(el))