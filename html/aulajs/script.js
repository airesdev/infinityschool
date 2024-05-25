// const section = document.querySelector("#products")

// async function getProducts(section) {
//     const requisition = await fetch("https://fakestoreapi.com/products/")
//     const items = await requisition.json()

//     for (let item of items) {
//         const novo_item = document.createElement("div")
//         const novo_img = document.createElement("img")
//         const novo_title = document.createElement("p")
//         const novo_price = document.createElement("p")

//         novo_item.classList.add("item")
//         novo_img.classList.add("item-image")
//         novo_title.classList.add("item-title")
//         novo_price.classList.add("item-price")

//         novo_img.src = item.image
//         novo_title.textContent = item.title
//         novo_price.textContent = item.price

//         section.append(novo_item)
//         section.append(novo_img)
//         section.append(novo_title)
//         section.append(novo_price)
//     }
// }

// getProducts(section)
const section = document.querySelector("#products")

async function get(dir) {
    const requisition = await fetch("https://fakestoreapi.com/" + dir)
    const items = await requisition.json()
    console.log(items)
    return items
}

async function showItems(dir, target) {
    const items = await get(dir)

    for (let item of items) {
        const novo_item = document.createElement("div")
        const novo_img = document.createElement("img")
        const star = document.createElement("img")
        const novo_title = document.createElement("p")
        const novo_price = document.createElement("p")
        const novo_rating = document.createElement("p")

        novo_item.classList.add("item")
        novo_img.classList.add("item-image")
        star.classList.add("star")
        novo_title.classList.add("item-title")
        novo_price.classList.add("item-price")
        novo_rating.classList.add("item-rating")

        novo_img.src = item.image
        star.src = ""
        // to add star img
        novo_title.textContent = item.title
        novo_price.textContent = item.price
        novo_rating.textContent = item.rating.rate

        target.append(novo_item)
        target.append(novo_img)
        target.append(star)
        target.append(novo_title)
        target.append(novo_price)
        target.append(novo_rating)
    }
}

showItems("products", section)