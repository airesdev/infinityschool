// const p = window.document.querySelector("p");
// const createP = window.document.createElement("p")

// ARRAYS
    // const pessoa = ["aires", 15]

// editar
    // pessoa[1] = 16
    // p.innerHTML = `${pessoa}`

// .PUSH => adiciona
    // pessoa.push("gabriel")
    // p.innerHTML = `${pessoa}`

// exercício 01
    // const lista = []
    // for (let i = 0; i != 5; i++) {
    //     const input = prompt("informe o nome de um veículo:")
    //     lista.push(input)
    // }
    // console.log(lista)

// .POP => remove*
    // pessoa.pop()
    // p.innerHTML = `${pessoa}`

// *e pode guardar
    // const removido = pessoa.pop()
    // p.innerHTML = `${pessoa}, (${removido})`

// .SORT => ordena
    // const valores = ["q", "h", "d", "v", "y", "e", "o", "m"]
    // valores.sort()

// .INDEXOF => pega index do elemento
    // pessoa.indexOf("aires")

// teste
    // for (letra of valores) {
    //     if (letra === "a" || letra === "e" || letra === "i" || letra === "o" || letra === "u") {
    //         console.log(letra)
    //     }
    // }

// atividade 01
    // const pares = []
    // const impares = []

    // for (let i = 0; i < 20; i++) {
    //     const input = prompt('informe um número:')

    //     if (input % 2 === 0) {pares.push(input)}
    //     else if (input % 2 !== 0) {impares.push(input)}
    //     else {alert(`${input} é um valor inválido, ultilize apenas números`)}
    // }
    // console.log(pares)
    // console.log(impares)

// atividade 03 (~30 lines)

const perguntas = [1, 2, 3, 4, 5]
const respostas = []
let positivo = 0
let negativo = 0

function processar() {
    if (positivo === 5) {
        console.log("Assassino")
        // turn to let later!!!
    } else if (positivo = 2) {
        console.log("Suspeito")
    } else {
        console.log("Cúmplice")
    }
}

for (pergunta of perguntas) {
    const input = prompt(`${perguntas[perguntas.indexOf(pergunta)]}`)
    respostas.push(input.toLowerCase)
}

// i could have used length too
for (resposta of respostas) {
    if (resposta === "y") {
        positivo++
    } else if (resposta === "n") {
        negativo++
    } else {
        alert('respostas inválidas, ultilize apenas y/n')
    }
}

processar(positivo)
