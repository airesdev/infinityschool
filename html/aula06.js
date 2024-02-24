// Revisão de arrays:

// frutas = []

// while (true) {
//     const user = prompt('O que deseja fazer? \n 1 - Adicionar fruta \n 2 - Ver todas as frutas \n 3 - Remover fruta \n 0 - Sair')

//     if (user === "1") {
//         const fruta = prompt('Informe a fruta a adicionar:')
//         frutas.push(fruta)
//         alert(`${fruta} foi adicionada com sucesso!`)
//     } else if (user === "2") {
//         let msg = "lista de frutas: \n"
//         for (fruta of frutas) {msg += fruta + "\n"}
//         alert(msg)
//     } else if (user === "3") {
//         const fruta = prompt('Informe a fruta a remover:')
//         frutas.splice(frutas.indexOf(fruta))
//         alert(`${fruta} foi removida com sucesso!`)
//     } else if (user === "0") {
//         alert('Fim do programa')
//         break
//     } else {
//         alert('valor inválido! use apenas os valores indicados.')
//     }
// }

// Funções

// function funcao (nome) {return `bem vindo ${nome}!`}

// user = prompt('informe seu nome:')
// alert(funcao(user))

// atividade 01

function stringFilter (string, filter, debug) {
    // string(<str>, <str>, "debug"?)
    let total = 0
    let value = 0
    const letras = []

    for (const letra of string) {
        total++
        for (const element of filter) {
            if (letra === element) {
                letras.push(letra)
                value++
            }
        }
    }

    return [total, value, letras]
}

string = prompt('informe uma palavra: ')
filter = prompt('informe as letra a contar: ')
alert(stringFilter(string, filter))

// atividade 02

// function square (number) {
//     return number ** number
// }

// atividade 03

// function circle (r, fixed, value) {
//     // circle(<radius>, "fixed?", <fractionDigits>)

//     const a = Math.PI * r**2
//     const p = 2 * Math.PI * r

//     if (fixed === "fixed") {
//         return [a.toFixed(value), p.toFixed(value)]
//     } else {
//         return [a, p]
//     }
// }

// atividade 04

