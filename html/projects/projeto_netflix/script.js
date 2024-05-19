async function get(list, key, lang){
    try{
        const requisicao = await fetch("https://api.themoviedb.org/3/movie/" + list + "?api_key=" + key + "&language=" + lang)
        const resposta = await requisicao.json()
        return resposta
    }catch(error){
        console.log("Error ao acessar a API")
    }
}

function adicionar(id, type) {

    // título
    const titulo = document.createElement("h2")
    titulo.textContent = id.title
    titulo.classList.add("titulo")

    // imagem
    const img = document.createElement("img")
    img.src = "https://image.tmdb.org/t/p/w500" + id.poster_path
    img.classList.add("poster")

    // rating
    const rating = document.createElement("img")
    rating.classList.add("rating")

    if (id.adult = true) {rating.src = "/content/adulto.png"}
    else {rating.src = "/content/livre.png"}

    // votos
    const votos = document.createElement("div")
    votos.classList.add("votos")

    const estrela = document.createElement("img")
    estrela.src = "/content/star.png"
    votos.append(estrela)
    const average = document.createElement("p")
    average.textContent = id.vote_average
    votos.append(average)

    // year
    const year = document.createElement("p")
    year.textContent = id.release_date
    year.classList.add("year")

    // const reminder = document.createElement("button")
    // const more = document.createElement("button")

    // poster
    const poster = document.createElement("div")
    // poster.classList.add("filme")

    if (type = "vertical") {
        poster.classList.add("vertical")
    }else if (type = "horizontal") {
        poster.classList.add("horizontal")
    }else if (type = "upcoming") {
        poster.classList.add("upcoming")
    }else if (type = "top") {
        poster.classList.add("top")
    }else {
        console.log("Erro no tipo de poster")
    }

    // append
    poster.appendChild(titulo)
    poster.appendChild(img)
    poster.appendChild(rating)
    poster.appendChild(votos)
    poster.appendChild(year)

    document.appendChild(poster)
}

const popular = get("popular", "77c4e2b070a2e1396500d0b42ebf7cec", "pt-BR").results

for (let id of popular) {
    adicionar(id, "vertical")
}