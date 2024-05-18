const n1 = Number(prompt("Insira um número:"))
const n2 = Number(prompt("Insira um segundo número:"))
const n3 = Number(prompt("Insira mais um número:"))

const p1 = Number(prompt("Insira um peso:"))
const p2 = Number(prompt("Insira um segundo peso:"))
const p3 = Number(prompt("Insira mais um peso:"))

function mediaPonderada (n1, p1, n2, p2, n3, p3) {
    return (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)
}

console.log(mediaPonderada (n1, p1, n2, p2, n3, p3))