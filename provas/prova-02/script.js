const peso = Number(prompt("Insira o peso:"))
const altura = Number(prompt("Insira o altura:"))

function imc (peso, altura) {return peso / (altura * altura)}

function classificar (imc) {
    if (imc < 16) {
        return "Baixo peso muito grave"
    } else if (imc < 17) {
        return "Baixo peso grave"
    } else if (imc < 18.5) {
        return "Baixo peso"
    } else if (imc < 25) {
        return "Peso normal"
    } else if (imc < 30) {
        return "Sobrepeso"
    } else if (imc < 35) {
        return "Obesidade grau I"
    } else if (imc < 40) {
        return "Obesidade grau II"
    } else if (imc >= 40) {
        return "Obesidade grau III"
    }
}

console.log(classificar(imc(peso, altura)))

let idade = 18;
let status = (idade >= 18) ? "Maior de idade" : "Menor de idade";