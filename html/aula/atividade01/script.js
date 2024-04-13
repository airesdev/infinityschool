const fruits = ["Maçã", "Banana", "Uva", "Melancia", "Abacaxi"]

// const filter = fruits.filter((fruit) => fruit !== "Banana")
const filter = fruits.filter((fruit) => !fruit.toLocaleLowerCase().includes("banana"))
const list = document.createElement("ul")
document.body.appendChild(list)

function addItem(fruit) {
    const newItem = document.createElement("li")
    newItem.textContent = fruit
    newItem.classList.add("item")
    list.append(newItem)
}

filter.map((fruit) => addItem(fruit))