const addBookForm = document.querySelector("#addBookForm")

addBookForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const title = document.querySelector("#title").value
    const author = document.querySelector("#author").value
    const cover = document.querySelector("#cover").value
    const genre = document.querySelector("#genre").value
    const year = document.querySelector("#year").value

    addBook(title, author, cover, genre, year)
});

const list = []
const book = {
    title: "title",
    author: "author",
    cover: "cover",
    genre: "genre",
    year: "year",
    stars: 0
}

function addBook (title, author, cover, genre, year) {
    const newBook = Object.create(book)
    newBook.title = title
    newBook.author = author
    newBook.cover = cover
    newBook.genre = genre
    newBook.year = year
    list.push(newBook)
    console.log(list)
}

function search (search) {

}

function comment (comment, stars) {

}